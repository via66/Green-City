# Django-Unchained
![Codeship Status](https://www.codeship.io/projects/8c5b7870-96cf-0132-19b3-76c54edd661d/status)

The proc file is used by heroku to determine how to run the project.

It needs the requirements.txt file so that it can install all the necessary python libraries.

If you look in the settings file, the database is set based on the development_type evironment variable.
In heroku, that variable is set to "PRODUCTION", so on the heroku server it sets the database based on the "DATABASE_URL" which gives
the user_id and password and db url and port.
This is a comment to test Integrated Deployment

Project URL:
http://team-django-unchained.herokuapp.com


