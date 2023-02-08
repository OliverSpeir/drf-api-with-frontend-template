# DRF API with Frontend markup
- Django Default user Authentication 
- JWT Authorization
- Custom User Model
- Static files from WhiteNoise
- Gunicorn Production Server
- Styled Login, User Create, and basic CRUD forms 
- Docker auto migrates 
- 

## To Do:
- put a create super user migration in accounts that pulls from .env
  - [stack over flow describng process](https://stackoverflow.com/questions/72131424/django-create-a-superuser-in-a-data-migration)
- Decide if docker should auto migrate on startup
- fix auto fill in create new

### References

- https://docs.djangoproject.com/en/4.1/ref/forms/widgets/


### Setup

-  `python -c "import secrets; print(secrets.token_urlsafe())"`
  - makes secret key 