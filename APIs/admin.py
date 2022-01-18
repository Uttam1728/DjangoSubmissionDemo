from django.contrib import admin
from django.contrib.admin.decorators import register

from APIs.models import Submission, Attachment as sub_attachment
from POSTS.models import Post, Attachment as post_attachment
from APIs.Util.AdminActions import make_published, make_submitted


class AttachmentInCartInline(admin.TabularInline):
    model = sub_attachment


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    model = Submission
    list_display = ('SubmissionID', 'Title', 'Status',
                    'CreatedOn', 'ApprovedBy')
    list_filter = ('SubmissionID', 'Title', 'Status',
                   'CreatedOn', 'ApprovedBy')
    search_fields = ('Title',)

    inlines = (AttachmentInCartInline,)
    actions = [make_published, make_submitted]


# admin.site.register(Submission)
admin.site.register(sub_attachment)
admin.site.register(Post)
admin.site.register(post_attachment)
