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
**Setting up the environment**
- python3 -m venv my_env
- source my_env/bin/activate
- pip install django
- django-admin --version
- django-admin startproject djangoproject
- python manage.py migrate

**Testing**
- sudo ufw allow 8000
- python manage.py runserver your_server_ip:8000
- endpoints
  - http://your_server_ip:8000
  - http://your_server_ip:8000/admin/
- Ctrl + C: stop the server

*References**
- [How To Install the Django Web Framework on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-22-04)