# Django HTML5 Boilerplate

This is my vision of HTML5 Boilerplate integrated into Django. Much work was done by Mike Robinson in his [repo](https://github.com/mike360/django-html5-boilerplate)
I made some changes that I felt were more intuitive and generally "better" in my opinion.

## Introduction

This is a starting template for Django website projects using (a slightly modified version of)
[Paul Irish's HTML5 Boilerplate](http://html5boilerplate.com).


## Features

* A Django 1.3 project skeleton
* A slightly modified version of the HTML5 Boilerplate
* Custom development url patterns that allow Django to serve static media files in development (via django.contrib.statifiles)
* A `settings_local.py.ex` template file that allows you to set environment-specific settings
* A `test_all.py` script that allows you to run the unit tests for all applications in INSTALLED_APPS
* Included the [960 grid system](http://960.gs), both 12 and 24 column versions. 24 column is integrated with base template.


## HTML5 Boilerplate Modifications

Following are the modifications I've made from the original HTML5 Boilerplate (v1.0).
Some modifications are for Django-specific reasons, others are just personal preference.

* I've included the `crossdomain.xml` file for Flash but serving it needs to be configured. I don't work with Flash so haven't bothered.
* Removed robots.txt (check out [django-robots](https://github.com/jezdez/django-robots) )

## How to use the template

1. Download a copy of the django-html5-boilerplate template to your development environment
    
1. Follow the rest of this script:
    
        # set path
        cd <path-to-project>/
        
        # Rename the project folder 
        mv projectname <project_name>

        # copy settings_local.py
        cp settings_local.py.ex settings_local.py

        # Edit settings_local.py
        vi settings_local.py
        

        # edit databeses settings and other settings as you prefer

        DATABASES = {
            'default': {
                'ENGINE': '',                           # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': '',                             # Or path to database file if using sqlite3.
                'USER': '',                             # Not used with sqlite3.
                'PASSWORD': '',                         # Not used with sqlite3.
                'HOST': '',                             # Set to empty string for localhost. Not used with sqlite3.
                'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
            }
        }
    
        # Run the tests. Make sure they all pass
        ./test_all.py
    
        # start dev server
        ./manage.py runserver

