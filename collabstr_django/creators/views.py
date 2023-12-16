from django.http import HttpResponse
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Content, Creator
from .serializers import ContentSerializer, CreatorSerializer


class CreatorListCreateView(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 30  # Set the number of items per page

        platform = request.query_params.get("platform")
        if platform:
            creators = Creator.objects.filter(platform=platform)
        else:
            creators = Creator.objects.all()

        result_page = paginator.paginate_queryset(creators, request)
        serializer = CreatorSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = CreatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreatorRetrieveUpdateDeleteView(APIView):
    def get_object(self, pk):
        try:
            return Creator.objects.get(pk=pk)
        except Creator.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        creator = self.get_object(pk)
        if creator is None:
            return HttpResponse(status=404)
        serializer = CreatorSerializer(creator)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        creator = self.get_object(pk)
        if creator is None:
            return HttpResponse(status=404)
        serializer = CreatorSerializer(creator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        creator = self.get_object(pk)
        if creator is None:
            return HttpResponse(status=404)
        creator.delete()
        return HttpResponse(status=204)


class ContentListCreateView(APIView):
    def get(self, request, creator_id, *args, **kwargs):
        contents = Content.objects.filter(creator_id=creator_id)
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)

    def post(self, request, creator_id, *args, **kwargs):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator_id=creator_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContentRetrieveUpdateDeleteView(APIView):
    def get_object(self, creator_id, pk):
        try:
            return Content.objects.get(pk=pk, creator_id=creator_id)
        except Content.DoesNotExist:
            return None

    def get(self, request, creator_id, pk, *args, **kwargs):
        content = self.get_object(creator_id, pk)
        if content is None:
            return HttpResponse(status=404)
        serializer = ContentSerializer(content)
        return Response(serializer.data)

    def put(self, request, creator_id, pk, *args, **kwargs):
        content = self.get_object(creator_id, pk)
        if content is None:
            return HttpResponse(status=404)
        serializer = ContentSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, creator_id, pk, *args, **kwargs):
        content = self.get_object(creator_id, pk)
        if content is None:
            return HttpResponse(status=404)
        content.delete()
        return HttpResponse(status=204)
