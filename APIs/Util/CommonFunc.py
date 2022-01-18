from re import sub
from APIs.models import Submission
from POSTS.serializer import PostSerializer, AttachmentSerializer
from POSTS.models import Post, Attachment as Post_Attachment
from APIs.models import Attachment as Sub_Attachment


def CreatePost(queryset, request):

    submision: Submission
    for submision in queryset.all():
        print(submision.Title)
        attachments = submision.attachment_set
        post = dict()
        post["Title"] = submision.Title
        post["Discription"] = submision.Discription
        post_serializer = PostSerializer(data=post)
        if post_serializer.is_valid():
            post_serializer.save()
            attachment: Sub_Attachment
            for attachment in attachments.all():
                temp = dict()
                temp["URL"] = attachment.URL
                temp["AlterTitle"] = attachment.AlterTitle
                temp["Post"] = post_serializer.data["PostId"]
                attachment_serializer = AttachmentSerializer(data=temp)
                if attachment_serializer.is_valid():
                    attachment_serializer.save()
                else:
                    attachment_serializer.errors
