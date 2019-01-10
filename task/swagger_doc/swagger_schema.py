from rest_framework.decorators import renderer_classes, api_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework import response
import coreapi
import coreschema

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):

    schema = coreapi.Document(
        url='http://127.0.0.1:8000/',
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
                'query': coreapi.Link('/api/v1/users/{id}/', action='delete', fields=[
                    coreapi.Field(name='id', location='path', required=True)
                ]),

                'body': coreapi.Link('/api/v1/users/{id}/', action='put', fields=[
                    coreapi.Field(name='id', location='path', required=True),
                    coreapi.Field(name='example', location='body', schema=coreschema.String(description='ThOne of: api, json'))
                ]),
                'path': coreapi.Link('/api/v1/users/{id}/', fields=[
                    coreapi.Field(name='id', location='path', required=True)
                ]),
                'form': coreapi.Link('/api/v1/users/', action='post', encoding='application/json', fields=[
                    coreapi.Field(name='example', location='body')
                ]),
            },
            'file_upload': {
                # 'multipart': coreapi.Link('/multiupload/', action='post', encoding='multipart/form-data', fields=[
                #     coreapi.Field(name='a', required=True),
                #     coreapi.Field(name='b')
                # ]),
                'multipart-body': coreapi.Link('/api/v1/upload/', description='classifies url of a file', action='put', encoding='multipart/form-data', fields=[
                    coreapi.Field(name='file', location='form', type='file')
                ]),
                'body': coreapi.Link('/api/v1/encoded-upload/', action='put', fields=[
                    coreapi.Field(name='file', location='body')
                ]),
                # 'urlencoded': coreapi.Link('/encoding/urlencoded/', action='post', encoding='application/x-www-form-urlencoded', fields=[
                #     coreapi.Field(name='a', required=True),
                #     coreapi.Field(name='b')
                # ]),
                # 'upload': coreapi.Link('/encoding/upload/', action='post', encoding='application/octet-stream', fields=[
                #     coreapi.Field(name='example', location='body', required=True)
                # ]),
            }
        }
    )
    return response.Response(schema)