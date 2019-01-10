import base64
import json
import os

from django.test import TestCase
from rest_framework import status, viewsets
from rest_framework.test import APITestCase, APIRequestFactory

from users_service.models import User

from users_service.serializers import UserSerializer
import csv, io, json

from users_service.views import EncodedFileUploadView


class TestUserService(APITestCase):
    class UserViewSet(
        viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerializer

        # some properties omitted

    def setUp(self):
        self.view = self.UserViewSet.as_view(actions={'get': 'list'})

    def test_filter_query(self):
        instance = User.objects.create(
            **{'first_name': 'Lighergh', 'last_name': 'alexanyan', 'email': 'alex@gmail.com'})
        request = APIRequestFactory().get('/api/v1/users/?email=lus', content_type='application/json')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response.render()
        json_dict = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_dict[0]['first_name'], instance.first_name)


# csv file as base64 string put request test
class TestFileUploadAsJsonString(APITestCase):

    def setUp(self):
        self.view = EncodedFileUploadView.as_view()
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'users.csv')

        file = open(file_path, 'rb')
        file_content = file.read()
        self.base64_sting = base64.b64encode(file_content).decode()
        # csv_strings = []
        # with open(file_path, 'r') as f:
        #     file_reader = csv.reader(f, delimiter=',')
        #     for row in file_reader:
        #         csv_strings.append(','.join(row))
        #     self.csv_string = ''.join(csv_strings)
        # file_data = csv.DictReader(io.StringIO(csv_string))
        # self.json_data = json.dumps(list(file_data))
        # self.base64_string = base64.b64encode(self.json_data.encode('utf-8'))
        # print(self.base64_string)

    def test_file_upload(self):
        # self.assertEqual(type(self.base64_sting),'str')
        factory = APIRequestFactory()
        print(type(self.base64_sting))
        request = factory.put('/api/v1/encoded_upload/', {'file': self.base64_sting})
        response = self.view(request)
        response.render()
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
