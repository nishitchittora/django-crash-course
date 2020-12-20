=====
Django Crash Course
=====

Polls is a Django app to conduct Web-based polls. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "crash_course" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'crash_course',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('crash_course/', include('crash_course.urls')),

3. Run ``python manage.py migrate`` to create the crash course models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a crash course (you'll need the Admin app enabled).
