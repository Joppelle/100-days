# 100-days

## Day 1
**The Goal**
- Deploy a webapp on AWS
- Engage in activities for 100 days
  - Write code
  - Planning
  - Exploring and tinkering with new technology

**Purpose**
- To get better at programming.
- Apply Software engineering principles while doing it.

**What to use**
- Django

**References**
- [#100DaysOfCode](https://www.100daysofcode.com/)
- [django](https://www.djangoproject.com/)
- [Web Application Deployment: A Step-by-Step Guide using Amazon Web Services (AWS)](https://medium.com/@bilal325/web-application-deployment-a-step-by-step-guide-using-amazon-web-services-aws-a22e15c9d81e)

## Day 2

**Actions**
- Learning how to setup a django environment
  - python3 -m venv my_env
  - source my_env/bin/activate
  - pip install django
  - django-admin --version
  - django-admin startproject djangoproject
  - python manage.py migrate
- Testing with django
  - sudo ufw allow 8000
  - python manage.py runserver your_server_ip:8000
  - endpoints
    - http://127.0.0.1:8000
    - http://127.0.0.1:8000/admin/
  - Ctrl + C: stop the server

**References**
- [How To Install the Django Web Framework on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-22-04)

## Day 3

**Actions**
 - Firing up an old AWS account
 - Cleaning up old EC2 instances

**References**
- [Terminate Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html)

**Misc Reading**
- [Demystifying ifconfig and network interfaces in Linux](https://codewithyury.com/demystifying-ifconfig-and-network-interfaces-in-linux/)

## Day 4

**Actions**
- Back to Django.

**References**
- [Writing your first Django app, part 1](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
- [django-admin and manage.py](https://docs.djangoproject.com/en/5.0/ref/django-admin/#makemigrations)
- [FAQ: Getting Help](https://docs.djangoproject.com/en/5.0/faq/help/)
- [Django Project Structure: A Comprehensive Guide](https://medium.com/django-unleashed/django-project-structure-a-comprehensive-guide-4b2ddbf2b6b8)

## Day 5

**Actions**
- Back to Django.

**Notes**
 - sudo apt install sqlite3
 - sqlite3 db.sqlite3         # open sqlite database and interact with cli
   - .tables                  # see a list of tables in sqlite db

 - Django philosophy for models: Don’t repeat yourself (DRY)

 - After editing a model.py need to run below:
   - python manage.py makemigrations polls
   - polls could be another app or site

**References**
- [Writing your first Django app, part 2](https://docs.djangoproject.com/en/5.0/intro/tutorial02/)
- [Command Line Shell For SQLite](https://sqlite.org/cli.html)
- [Special commands to sqlite3 (dot-commands)](https://sqlite.org/cli.html#special_commands_to_sqlite3_dot_commands_)

## Day 6

**Actions**
- Back to Django: https://docs.djangoproject.com/en/5.0/intro/tutorial02/#playing-with-the-api
- Hackerrank: https://www.hackerrank.com/dashboard

**Notes**
