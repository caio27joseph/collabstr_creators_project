from django.shortcuts import render
from .models import Creator, Content
from django.db.models import Subquery, OuterRef


def creator_list_view(request):
    creators = (
        Creator.objects.prefetch_related("content_set")
        .annotate(
            first_content_url=Subquery(
                Content.objects.filter(creator=OuterRef("pk")).order_by("pk").values("url")[:1]
            )
        )
        .order_by("-rating")[:30]  # Limit the number of creators to 30
    )
    for creator in creators:
        if creator.first_content_url:
            creator.is_video = creator.first_content_url.split(".")[-1].lower() in ["mov", "mp4"]
        else:
            creator.is_video = False
    return render(request, "creators.html", {"creators": creators})
