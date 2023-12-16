from django.db import models


class Creator(models.Model):
    # Choices for different platforms
    PLATFORM_CHOICES = [("IG", "Instagram"), ("TT", "TikTok"), ("UGC", "User-Generated Content")]

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    platform = models.CharField(max_length=3, choices=PLATFORM_CHOICES)

    def __str__(self):
        return self.name


class Content(models.Model):
    creator = models.ForeignKey(
        Creator,
        on_delete=models.CASCADE,
        related_name="content_set",
        related_query_name="content",
    )  # Define the ForeignKey relationship
    url = models.URLField()

    def __str__(self):
        return f"Content by {self.creator.name}"
