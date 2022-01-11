from rest_framework import serializers
from APIs.models import Submission, Attachment


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ('AttachmentID', 'CreatedOn',
                  'URL', 'Submission', 'AlterTitle')
