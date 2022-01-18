from django.db import models

STATUS = (
    (0, "Submited"),
    (1, "Approved"),
    (2, "Published")
)


class Post(models.Model):
    PostId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    Discription = models.JSONField()
    CreatedOn = models.DateField(auto_now_add=True)
    LastUpdatedOn = models.DateField(auto_now=True)

    def __str__(self):
        return self.Title


class Attachment(models.Model):
    AttachmentID = models.AutoField(primary_key=True)
    CreatedOn = models.DateTimeField(auto_now_add=True)  # Date of creation
    URL = models.CharField(max_length=500)
    Post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
        db_column='PostID')
    AlterTitle = models.CharField(max_length=500, default="alter")

    def __str__(self):
        return self.AlterTitle
