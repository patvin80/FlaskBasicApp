# FlaskBasicApp
A  Basic Flask App with Models and Docker Container defined

1. Start with the basics of a Flask App
2. Show the creation of a model
3. Show the db.create_all() mechanism
4. python FlaskBasicApp.py -- Brings up a server and runs the app at 127.0.0.1:5000
    1. Notice the test.db file being created
    2. Navigate through the Routes so that the Courses are Created and Courses are listed
    3. Talk about Templates and the Static Folder
5. Now lets create a more involved Flask App with some modifications    
    1. Move the models to a different file
    2. Import the file using the from models import * syntax
    3. Setup Config so that the config can have inheritance
    4. Include the config and do Import
    5. Now we have a way to configure whether the app will run in Dev config or Production Config
    6. Adding a Test Case
        1. Making sure that the pytest and pytest-Flask and Flask-testing are in the requirements
        2. py.test can be used to execute the test cases.
6. Lets Talk about AWS Code Star a Cool way to get your app to the Cloud and watch it being continuously being deployed in a CD Fashion
    0. Show the AWS Codestar Environment and all the configurations for the same.
    1. Navigate to the AWS Code Star Folder - Visual Studio Code
    2. Login into the AWS Console as VinitPat
    3. Make a Change and push the change in GIT
    4. Watch the change being propogated in AWS
    5. Talk about the Code now being hosted on Linux AMI and DB on an RDS instance and issue comes up and cannot be reproduced on MacBook
7. Dockerize the Environment -- https://github.com/tiangolo/uwsgi-nginx-flask-docker
    1. Docker File - Infrastructure as Code
    2. Docker File walkthrough -- Here is a Useful cheat sheet
        1. from specifies the image that you want to work with    
        2. COPY specifies that copy the contents of the current director to the app folder on the image
        3. RUN executes commands on the images
        4. Additional RUN Commands in the Dockerfile-dev to ensure that the uwsgi file is replaced appropriately.
    3. Apart from the Docker Files, docker also gives a Docker Compose mechanism to structure your infrastructure using yml syntax.
        1. services indicates the machines
        2. Dependency can be indicated
        3. Configuration of the Postgres environment is setup in the Postgres DB and ensures that all environments are consistent
    4. The image for Python Flask with UWSGI configuration needs uwsgi.ini file setup
        1. The Development environment has py-autoload set to 1 to ensure that the local code changes would be reflected immediately
        2. The Production environment has no entry for py-autoload
        3. The module and the app name have to be configured. The default value expected is "application" for callable.
        4. The callable is the file name in which the app is created in our case FlaskBasicAppWithConfig

## Useful Commands
### Development
1. docker-compose -f docker-compose-dev.yml build
2. docker-compose -f docker-compose-dev.yml up

### Production
1. docker-compose build
2. docker-compose up

