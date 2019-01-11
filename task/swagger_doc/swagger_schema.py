from rest_framework.decorators import renderer_classes, api_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework import response
import coreapi
import coreschema

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):

    schema = coreapi.Document(
        url='http://18.223.188.159:8000/',
        title='DOCUMENTATION',
        content={

            'users_crud': {
                'simple_link': coreapi.Link('/api/v1/users/', description='users list', fields=[
                    coreapi.Field(name='filter', location='query', required=False)]),
                'path': coreapi.Link('api/v1/?url={url}&type={type}', description='classifies file',
                                     fields=[
                                         coreapi.Field(name='url', location='path', required=True),
                                         coreapi.Field(name='type', location='path', required=True)]
                                     ),
                'query': coreapi.Link('/api/v1/users/{id}/', action='delete', description='delete user', fields=[
                    coreapi.Field(name='id', location='path', required=True)
                ]),

                'body': coreapi.Link('/api/v1/users/{id}/', action='put', description='update user info', fields=[
                    coreapi.Field(name='id', location='path', required=True),
                    coreapi.Field(name='example', location='body', schema=coreschema.String(description='ThOne of: api, json'))
                ]),
                'path': coreapi.Link('/api/v1/users/{id}/', fields=[
                    coreapi.Field(name='id', location='path', required=True)
                ]),
                'form': coreapi.Link('/api/v1/users/', action='post', encoding='application/json', description='creates user', fields=[
                    coreapi.Field(name='example', location='body')
                ]),
            },
            'file_upload': {

                'multipart-body': coreapi.Link('/api/v1/upload/', description='upload users csv file', action='put', encoding='multipart/form-data', fields=[
                    coreapi.Field(name='file', location='form', type='file')
                ]),
                'body': coreapi.Link('/api/v1/encoded-upload/', action='put', fields=[
                    coreapi.Field(name='file', location='body')
                ]),
            }
        }
    )
    return response.Response(schema)