# click2sureTask

## Post/Put requests 

For user create/update operations, body must be of the following structure:
```buildoutcfg
  {
    "first_name": "Lusine",
    "last_name": "Mkrtchyan",
    "email": "laus@mail.com"
  }

```
As I was not able to find the csv file for user data. I have used a casv file in the format of users.csv, which is present in directory 

## api/v1/upload/

127.0.0.1:8000/api/v1/upload/ put file

## Unit testing
To run unit tests, run following command:

```buildoutcfg
python manage.py test users_service.tests

```
