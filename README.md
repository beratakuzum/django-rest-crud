# django_rest_crud
 
django_rest_crud is an example REST API project to help understand Django Rest Framework.

## How to run?
You can simply run the project by creating a virtual environment, install the required packages and making the migrations. 
  ```sh
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ cd django_rest_crud/
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:80
```
## Project structure and and explanations
- The project has two apps: ```events``` and  ```sessions```. An event in the context of the project might be a gathering, conference, symposium etc. A session is a section of an event.
-  Events might have zero or more sessions. They can be created without specifying a session.
-  Sessions cannot exist and be created without an event. They have one-to-many relationship with an event.

##### Event Model Class
```python
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
class Event(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    time_zone = models.CharField(max_length=32, null=False, blank=False, choices=TIMEZONES)
```
##### Session Model Class
``` python
class Session(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    speaker = models.CharField(max_length=100, null=False, blank=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
```

## API Documentation
#### List Events
Retrieves all events in the database.
##### Request
```
Method: GET
Url: /events/
```
##### Successful Response
```
Response Code: 200
Body:   
[
    {
        "id": 2,
        "name": "Example Event",
        "start_date": "2020-12-15T18:00:26+03:00",
        "end_date": "2020-12-15T18:00:26+03:00",
        "time_zone": "UTC"
    }
]
```
#### Create Event
Creates a new event in the db
##### Request
```
Method: POST
Url: /events/
{
    "name": "Example Event",
    "start_date": "2020-12-15 18:00:26",
    "end_date": "2020-12-15 18:00:26",
    "time_zone": "UTC"
}
```
##### Successful Response
Retrieves the created reasource along with its database id.
```
Response Code: 201
Body:   
{
    "id": 2,
    "name": "Example Event",
    "start_date": "2020-12-15 18:00:26",
    "end_date": "2020-12-15 18:00:26",
    "time_zone": "UTC"
}
```
#### Read Event
Retrieves a single event
##### Request
```
Method: GET
Url: /events/<event_id>/
```
##### Successful Response
```
Response Code: 200
Body:   
{
    "id": 2,
    "name": "Example Event",
    "start_date": "2020-12-15 18:00:26",
    "end_date": "2020-12-15 18:00:26",
    "time_zone": "UTC"
}
```
#### Update Event
Updates a single event
##### Request
```
Method: PUT
Url: /events/<event_id>/
Body:
{
    "name": "Example Event",
    "start_date": "2020-12-15 18:00:26",
    "end_date": "2020-12-15 18:00:26",
    "time_zone": "Europe/London"
}
```
##### Successful Response
```
Response Code: 200
Body:   
{
    "id": 2,
    "name": "Example Event",
    "start_date": "2020-12-15T18:00:26+03:00",
    "end_date": "2020-12-15T18:00:26+03:00",
    "time_zone": "Europe/London"
}
```
#### Delete Event
Deletes a single event
##### Request
```
Method: DELETE
Url: /events/<event_id>/
```
##### Successful Response
```
Response Code: 204
```

#### List Sessions
Retrieves all sessions in the database including their event ids.
##### Request
```
Method: GET
Url: /sessions/
```
##### Successful Response
```
Response Code: 200
Body:   
[
    {
        "id": 2,
        "name": "Example Session",
        "start_date": "2020-12-15T18:00:26+03:00",
        "end_date": "2020-12-15T18:00:26+03:00",
        "speaker": "Berat",
        "event": 3
    }
]
```
#### Create Session
Creates a new session in the db
##### Request
```
Method: POST
Url: /sessions/
{
    "name": "Example Session",
    "start_date": "2020-12-15 18:00:26",
    "end_date": "2020-12-15 18:00:26",
    "time_zone": "UTC",
    "speaker": "Berat",
    "event": <event_id>
}
```
##### Successful Response
Retrieves the created reasource along with its database id.
```
Response Code: 201
{
    "id": 3,
    "name": "Example Session",
    "start_date": "2020-12-15T18:00:26+03:00",
    "end_date": "2020-12-15T18:00:26+03:00",
    "speaker": "Berat",
    "event": 3
}
```
#### Read Session
Retrieves a single session
##### Request
```
Method: GET
Url: /sessions/<session_id>/
```
##### Successful Response
```
Response Code: 200
Body:   
{
    "id": 3,
    "name": "Example Session",
    "start_date": "2020-12-15T18:00:26+03:00",
    "end_date": "2020-12-15T18:00:26+03:00",
    "speaker": "Berat",
    "event": 3
}
```
#### Update Session
Updates a single session
##### Request
```
Method: PUT
Url: /sessions/<session_id>/
Body:
{
    "name": "Different Session",
    "start_date": "2020-12-15T18:00:26+03:00",
    "end_date": "2020-12-15T18:00:26+03:00",
    "time_zone": "UTC",
    "speaker": "random_speaker",
    "event": 3
}
```
##### Successful Response
```
Response Code: 200
Body:   
{
    "id": 3,
    "name": "Different Session",
    "start_date": "2020-12-15T18:00:26+03:00",
    "end_date": "2020-12-15T18:00:26+03:00",
    "speaker": "random_speaker",
    "event": 3
}
```
#### Delete Session
Deletes a single session
##### Request
```
Method: DELETE
Url: /sessions/<session_id>/
```
##### Successful Response
```
Response Code: 204
```