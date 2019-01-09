# click2sureTask

## api/v1/users/
get http://127.0.0.1:8000/api/v1/users/1 get user by id
post /api/v1/users/ with body   create user
 {
    "first_name": "Lusine",
    "last_name": "Mkrtchyan",
    "email": "laus@mail.com"
}

put api/v1/users/1/ updates user info
{
    "first_name": "Lusinehn",
    "last_name": "Mkrtchyan",
    "email": "lus@mail.com"
}

delete http://127.0.0.1:8000/api/v1/users/1

this endpoint returns users list, for further filtering you can make filtering to the same endpoint with queryparams.
Some examples are
```buildoutcfg
  api/v1/users/?email=lus
  api/v1/users/?first_name=Ki
  
```


## api/v1/upload/

127.0.0.1:8000/api/v1/upload/ put file