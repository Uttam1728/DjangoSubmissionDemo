from django.urls.conf import include, path
from .POSTViewSet import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('PostViewSet/', PostViewSet,
                basename='SubmissionViewSet')

urlpatterns = [

    path('', include(router.urls))
]
