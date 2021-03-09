# Tagup Backend Challenge
This is a RESTful API built using [Python Django](https://www.djangoproject.com/) + [Django REST Framework](https://www.django-rest-framework.org/)

## Using the API

### Getting a list of all records
```
curl https://backend-tagup.herokuapp.com/api/list/
```
### Getting a single record
```
curl https://backend-tagup.herokuapp.com/api/read/:id
```
### Creating a new record
```
curl -X POST -H 'Content-Type: application/json' -d '{"timestamp": 123456789, "value1": "value1", "value2": 1.0, "value3": true}' https://backend-tagup.herokuapp.com/api/create/
```
### Modifying a record
Modify a record by specifying an `id`. Partial updates are allowed.
```
curl -X PATCH -H 'Content-Type: application/json' -d '{"value1": "new test value for record #id"}' https://backend-tagup.herokuapp.com/api/modify/:id
```
### Deleting a record
Remove record by specifying an `id`
```
curl -X DELETE https://backend-tagup.herokuapp.com/api/remove/:id
```

## Development 
### Requirements
- Python (>3.5)
- Django (3.1.7)
- Django REST Framework (3.12.2)


Every endpoint is associated with a view that corresponds to the action the endpoint is responsible for.
For example, `read/:id` is associated with the `GetRecord` view in the `views.py` file. This makes maintaining and adding 
endpoints straightforward as each view is responsible for a single action.

### Adding new endpoints
- Navigate to the `myapi` directory. Open `urls.py`. Add an entry in the `urlpatterns` list to create a new endpoint.
If this new endpoint does not have any matching views, you must create one in order for the endpoint to have any affect.  
- Navigate to the `views.py` file and create a new class. The name of the class should reflect the desired action.
For example, for `create/`, the associated view is called `CreateRecord`. This ensures there's no ambiguity in what an endpoint and view are supposed to do.
