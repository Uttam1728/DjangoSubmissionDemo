
from APIs import views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^SaveFile$', views.SaveFile),
    url(r'^submissionlist$', views.GetAllSubmission),
    url(r'^submissionDetail/([0-9]+)/$', views.GetSubmission),
    url(r'^AddsubmissionDetail$', views.AddSubmission),
    url(r'^EditsubmissionDetail/([0-9]+)$', views.EditSubmission),
    url(r'^DeletesubmissionDetail/([0-9]+)$', views.DeleteSubmission)

]+static(settings.MEDIA_URL, document_roor=settings.MEDIA_ROOT)
