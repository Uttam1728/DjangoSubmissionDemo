from django.core.files.storage import default_storage

from .models import Submission
from .serializer import SubmissionSerializer


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
    if len(request.FILES) > 0:
        SaveFile(request)
    submission = dict()
    submission["Title"] = request.data["Title"]
    submission["Discription"] = request.data["Discription"]
    submission_serializer = SubmissionSerializer(data=submission)
    if submission_serializer.is_valid():
        submission_serializer.save()
        return Response(submission_serializer.data)
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
        return True
    except Exception:
        return False
