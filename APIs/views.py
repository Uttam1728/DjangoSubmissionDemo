from django.core.files.storage import default_storage

from RestAPIDemo.settings import MEDIA_URL
from .models import Attachment, Submission
from .serializer import AttachmentSerializer, SubmissionSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def GetAllSubmission(request):
    submissions = Submission.objects.all()
    submission_serializer = SubmissionSerializer(submissions, many=True)
    return Response(submission_serializer.data)


@api_view(['GET'])
def GetSubmission(request, id=0):
    try:
        submission = Submission.objects.get(SubmissionID=id)
        submission_serializer = SubmissionSerializer(submission, many=False)
        return Response(submission_serializer.data)
    except Submission.DoesNotExist:
        return Response("submission data not exist")


@api_view(['POST'])
def AddSubmission(request):
    response_msg = ""
    is_file_exist = len(request.FILES)

    # If file exist in request than First Save and Create Attachment Obj.
    if is_file_exist:
        file_name = SaveFile(request)
        if file_name == "not uploaded":
            return Response("File Upload Failed")
        attachment = dict()
        attachment["URL"] = "api" + MEDIA_URL + file_name
        attachment["AlterTitle"] = file_name

    submission = dict()
    submission["Title"] = request.data["Title"]
    submission["Discription"] = request.data["Discription"]
    submission_serializer = SubmissionSerializer(data=submission)

    if submission_serializer.is_valid():
        submission_serializer.save()
        response_msg += " Submission Saved SuccsessFully"
        if is_file_exist:
            attachment["Submission"] = submission_serializer.data["SubmissionID"]
            attachment_serializer = AttachmentSerializer(data=attachment)
            if attachment_serializer.is_valid():
                attachment_serializer.save()
                response_msg += ", Attachment Saved SuccsessFully"
            else:
                Response(data=attachment_serializer.errors)
        return Response(response_msg)
    else:
        return Response(data=submission_serializer.errors)


@api_view(['PATCH'])
def EditSubmission(request, id=0):
    try:
        submission = Submission.objects.get(SubmissionID=id)
        submission_serializer = SubmissionSerializer(
            instance=submission, data=request.data)

        if submission_serializer.is_valid():
            submission_serializer.save()
            return Response(submission_serializer.data)
        else:
            return Response(data=submission_serializer.errors)

    except Submission.DoesNotExist:
        return Response("submission data not exist")


@api_view(['DELETE'])
def DeleteSubmission(request, id=0):
    try:
        submission = Submission.objects.get(SubmissionID=id)
        submission.delete()
        return Response("submission DELETED.")

    except Submission.DoesNotExist:
        return Response("submission data not exist")


def SaveFile(request):
    try:
        file = request.FILES['attachment']
        file_name = default_storage.save(file.name, file)
        return file_name
    except Exception:
        return "not uploaded"


@api_view(['GET'])
def GetAllAttachments(request):
    attachments = Attachment.objects.all()
    attachment_serializer = AttachmentSerializer(attachments, many=True)
    return Response(attachment_serializer.data)


@api_view(['GET'])
def GetAttachments(request, id=0):
    try:
        attachment = Submission.objects.get(AttachmentID=id)
        attachment_serializer = AttachmentSerializer(attachment, many=False)
        return Response(attachment_serializer.data)
    except Submission.DoesNotExist:
        return Response("attachment data not exist")
