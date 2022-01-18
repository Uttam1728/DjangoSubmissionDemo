from rest_framework import viewsets

from .models import Submission, Attachment
from .serializer import SubmissionSerializer, AttachmentSerializer


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
