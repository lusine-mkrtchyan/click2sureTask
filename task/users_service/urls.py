from django.conf.urls import url
from rest_framework import routers
from users_service import views
from django.urls import path

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)



urlpatterns = [
    url(r'upload/', views.FileUploadView.as_view()),
    url(r'encoded-upload/', views.EncodedFileUploadView.as_view()),
]

urlpatterns += router.urls
