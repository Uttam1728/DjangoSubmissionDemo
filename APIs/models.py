from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

STATUS = (
    (0, "Submited"),
    (1, "Approved"),
    (2, "Published")
)


class Submission(models.Model):
    SubmissionID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    Discription = models.JSONField()
    Status = models.IntegerField(choices=STATUS, default=0)
    CreatedOn = models.DateField(auto_now_add=True)
    LastUpdatedOn = models.DateField(auto_now=True)
    ApprovedOn = models.DateField(blank=True, null=True)
    ApprovedBy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="ApprovedBy", blank=True, null=True)

    def __str__(self):
        return self.Title


class Post(models.Model):
    PostId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    Discription = models.JSONField()
    Status = models.IntegerField(choices=STATUS, default=0)
    CreatedOn = models.DateField(auto_now_add=True)
    LastUpdatedOn = models.DateField(auto_now=True)

    def __str__(self):
        return self.Title


class Attachment(models.Model):
    AttachmentID = models.AutoField(primary_key=True)
    CreatedOn = models.DateTimeField(auto_now_add=True)  # Date of creation
    URL = models.CharField(max_length=500)
    Submission = models.ForeignKey(
        "Submission",
        on_delete=models.CASCADE,
        db_column='SubmissionID')
    AlterTitle = models.CharField(max_length=500, default="alter")

    def __str__(self):
        return self.AlterTitle
