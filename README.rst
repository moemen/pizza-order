pizza
=====

Order our Pizza! This is a sample django project for my work. It only include basic staff like:

- Basic django project structure. It have initialized using cookiecutter django, and then added my customization.
- Use Docker in development and make it close to be ready for production (Just didn't tested yet).
- Data Modeling
- RESTful API
- Unit and Functionality testing

And DO NOT include (yet at least):

- Authentication
- Any frontend staff

:License: GPLv3


Development
------------

Installation
^^^^^^^^^^^^

This project used `Docker`_ and `Docker Compose`_. You will need to install them on you machine before continuing.

.. _Docker: https://docs.docker.com/engine/installation/
.. _Docker Compose: https://docs.docker.com/compose/install/

Then you will need to build project using ``docker-compose -f dev.yml build``.

Quick reference for Docker commands
"""""""""""""""""""""""""""""""""""

There is two docker compose configuration files ``dev.yml`` for development environment and ``docker-compose.yml`` for production environment. You will need to add ``-f dev.yml`` to every command that run in development.

To build project:

    docker-compose -f dev.yml build

To Run the project:

    docker-compose -f dev.yml up

You can add ``-d`` to run in in back ground. You can continue check containers logs like this:

    docker-compose -f dev.yml logs -f django

All Django commans that you need to run, including the next commands should be formated like: ``djangoc-ompose -f dev.yml run <CONTAINER_NAME> <COMMAND>``

Check Docker and Docker Compose documentation for more information.

Makfile
"""""""

I have added ``Makefile`` to shortcut the frequently used commands like ``docker-compose -f dev.yml up -d`` became ``make up``. Check ``Makefile`` for more commands.

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

$ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

$ coverage run manage.py test
$ coverage html
$ open htmlcov/index.html


Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

.. _mailhog: https://github.com/mailhog/MailHog

Container mailhog will start automatically when you will run all docker containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``
