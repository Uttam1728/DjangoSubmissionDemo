from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.options import (
    csrf_protect_m,
    HttpResponseRedirect,
    unquote
)

from APIs.models import Submission, Attachment as sub_attachment
from POSTS.models import Post, Attachment as post_attachment
from APIs.Util.AdminActions import make_published, make_submitted, create_Post


class AttachmentInCartInline(admin.TabularInline):
    model = sub_attachment
    extra = 0


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    model = Submission
    list_display = ('SubmissionID', 'Title', 'Status',
                    'CreatedOn', 'ApprovedBy')
    list_filter = ('SubmissionID', 'Title', 'Status',
                   'CreatedOn', 'ApprovedBy')
    search_fields = ('Title',)
    change_form_template = 'admin/custom_change_form.html'
    inlines = (AttachmentInCartInline,)
    actions = [make_published, make_submitted]

    @csrf_protect_m
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        if request.method == 'POST' and '_make_published' in request.POST:
            obj = self.get_object(request, unquote(object_id))
            create_Post(request, obj)
            return HttpResponseRedirect(request.get_full_path())

        return admin.ModelAdmin.changeform_view(
            self, request,
            object_id=object_id,
            form_url=form_url,
            extra_context=extra_context,
        )


# admin.site.register(Submission)
admin.site.register(sub_attachment)
admin.site.register(Post)
admin.site.register(post_attachment)
