Introduction
------------
This is manual how to create your ouw Python + Flask application for Heroku.

Steps
-----

* Regiter at Heroku https://heroku.com and install Heroku CLI
* Create folder `my_app` and create file `app.py` in this folder with the following content:

```
    from flask import Flask
    
    app = Flask(__name__)
    
    
    @app.route('/')
    def my_app_endpoint():    
        return ''
    
    
    if __name__ == '__main__':
        app.run()
```

* Create file `Procfile` in the same folder with the following content:

```
    web: gunicorn app:app --preload
```

* Create file `requirements.txt`:

```
    Flask
    gunicorn
```
 
* Deploy your application:

```
    heroku login
    git init
    heroku git:remote -a my_first_heroku_app
    heroku config:set FLASK_APP=app.py
    heroku config:set WEB_CONCURRENCY=3
    git add .
    git commit -am "Added first version of app"
    git push heroku master
```
