import io
from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from users_service.serializerd import UserSerializer
from users_service.models import User
from rest_framework import filters
import csv
from django_filters.rest_framework import DjangoFilterBackend

from task.tasks import add_user

from helpers.csv_reader import read_csv


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
        if self.request.query_params.get('first_name', None):
            queryset = queryset.filter(first_name__icontains=self.request.query_params.get('first_name',''))
        if self.request.query_params.get('last_name', None):
            queryset = queryset.filter(last_name__icontains=self.request.query_params.get('last_name',''))
        if self.request.query_params.get('email', None):
            queryset = queryset.filter(email__icontains=self.request.query_params.get('email', ''))
        return queryset


class FileUploadView(views.APIView):
    # parser_classes = (MultiPartParser,)
    parser_class = (FileUploadParser,)

    def put(self, request):
        if 'csv_file' not in request.data:
            raise ParseError("Empty content")
        file_obj = request.data.get('csv_file')
        file_obj.seek(0)
        users = csv.reader(io.StringIO(file_obj.read().decode('utf-8')), delimiter=',')
        next(users)
        for user in users:
            add_user.delay(user)
        print(file_obj)
        return Response(status=204)