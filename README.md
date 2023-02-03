# LAB - 34

## Project: DRF API / Frontend Template

### Author: Oliver Speir

### Description

- Template for project that includes API app and Frontend app
    - Features:
      - JWT authorization for API
      - Custom User Model 
      - Login authentication for frontend

### Setup

Run:
- clone and cd into directory
- `docker compose up`
- or run outside of container by:
  - clone and create venv then activate venv `pip install -r requirements.txt`
  - then run `gunicorn project.wsgi:application --bind 0.0.0.0:8000 --workers 4` or `python manage.py runserver` for development server
- superuser will be auto set based on .env variables

Test:
- While server is running  is running:
- `curl -d '{"username":"dev", "password":"dev"}' -H 'Content-Type: application/json' -X POST http://127.0.0.1:8000/api/token/`
- `docker-compose run web python manage.py test` if docker or `python manage.py test` if not
### Resources

- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [postgresql](https://www.postgresql.org/)
- [Green Unicorn (gunicorn)](https://gunicorn.org/)
- [WhiteNoise](https://whitenoise.evans.io/en/latest/)
