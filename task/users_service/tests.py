import base64
import os
from unittest.mock import patch

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
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                 'users.csv')

        file = open(file_path, 'rb')
        file_content = file.read()
        self.base64_sting = base64.b64encode(file_content).decode()

    @patch('users_service.views.add_user.apply_async')
    def test_file_upload(self, mock_send):
        factory = APIRequestFactory()
        print(type(self.base64_sting))
        request = factory.put('/api/v1/encoded_upload/', {'file': self.base64_sting})
        response = self.view(request)
        response.render()
        print(response.content)
        self.assertTrue(mock_send.called)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
