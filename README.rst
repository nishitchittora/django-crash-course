===================
Django Crash Course
===================

Crash Course is a Django app to create an online course generation website.

Each course can contain multiple chapters and each chapter can contain multiple sections.

The section contains actual content in form of text and images.

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
