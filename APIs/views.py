from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

from .models import Submission, Attachment
from .serializer import SubmissionSerializer, AttachmentSerializer

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def GetAllSubmission(request):
    submissions = Submission.objects.all()
    submission_serializer = SubmissionSerializer(submissions, many=True)
    return Response(submission_serializer.data)


@api_view(['GET'])
def GetSubmission(request, id=2):
    try:
        submission = Submission.objects.get(SubmissionID=id)
        submission_serializer = SubmissionSerializer(submission, many=False)
        return Response(submission_serializer.data)
    except Submission.DoesNotExist:
        return Response("submission data not exist")


@api_view(['PATCH'])
def AddSubmission(request):
    submission_serializer = SubmissionSerializer(data=request.data)
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


@csrf_exempt
def SaveFile(request):
    file = request.FILES['attachment']
    file_name = default_storage.save(file.name, file)
    return JsonResponse("Add Successfully: "+file_name, safe=False)
