# DjangoUniversity - Assignment

This assignment involves creating the **DjangoUniversity** project and a new app called **campusApp** within it to practice Django project and app setup, modeling, and admin registration.

## Steps Completed

- Created a new app 'campusApp'.
- Added 'campusApp' to 'INSTALLED_APPS' in 'settings.py'.
- Defined the 'UniversityCampus' model in 'models.py' with these fields:
  - 'campus_name' (string)
  - 'state' (string, max length 2)
  - 'campus_id' (integer)
- Added a custom model manager.
- Configured the model’s Meta class to display as **“University Campus”** in the Django admin.
- Made and applied migrations for the model.
- Registered 'UniversityCampus' in 'campusApp/admin.py' to make it manageable via the admin interface.
- Ran the development server and added two sample 'UniversityCampus' entries via the admin panel.
- Included comments in code to clarify functionality.

This task helped reinforce Django app setup, model creation, migrations, and admin customization.