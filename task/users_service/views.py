import io
import json
from django.core.files.base import ContentFile
from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from users_service.serializers import UserSerializer
from users_service.models import User
from rest_framework import filters
import csv
from django_filters.rest_framework import DjangoFilterBackend

from task.tasks import add_user

from helpers.csv_reader import read_csv

from users_service.enums import Filters
import base64


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('first_name', 'last_name', 'email')

    def get_queryset(self):
        queryset = User.objects.all()
        if self.request.query_params.get(Filters.FIRST_NAME.value, None):
            queryset = queryset.filter(
                first_name__icontains=self.request.query_params.get(Filters.FIRST_NAME.value, ''))
        if self.request.query_params.get(Filters.LAST_NAME.value, None):
            queryset = queryset.filter(last_name__icontains=self.request.query_params.get(Filters.LAST_NAME.value, ''))
        if self.request.query_params.get(Filters.EMAIL.value, None):
            queryset = queryset.filter(email__icontains=self.request.query_params.get(Filters.EMAIL.value, ''))
        return queryset


class FileUploadView(views.APIView):
    # parser_classes = (MultiPartParser,)
    parser_class = (FileUploadParser,)

    def put(self, request):
        if 'file' not in request.data:
            raise ParseError("Empty content")
        file_obj = request.data.get('file')
        file_obj.seek(0)
        print(file_obj)
        users = csv.reader(io.StringIO(file_obj.read().decode('utf-8')), delimiter=',')
        next(users)
        for user in users:
            add_user.delay(user)
        print(file_obj)
        return Response(status=204)


class EncodedFileUploadView(views.APIView):
    # parser_classes = (MultiPartParser,)
    parser_class = (FileUploadParser,)

    def put(self, request):
        if 'file' not in request.data:
            raise ParseError("Empty content")
        file_str = request.data.get('file')
        file_obj = base64.b64decode(file_str).decode("utf-8")
        print(file_obj.splitlines())
        users = file_obj.splitlines()
        print(users)
        for user in users[1:]:
            user = user.split(',')
            print(isinstance(user, list))
            print(user)
            add_user.delay(user)
        print(file_obj)
        return Response(status=200)
