# DjangoCMS


This Django project is designed to provide a platform for blogging. It includes features for creating blogs, making posts, managing user accounts, and commenting on posts.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ceciluz/DjangoCMS/

   pip install -r requirements.txt
## Configuration
### Settings
Base Directory:
- BASE_DIR: The base directory of the Django project.
- Crispy Forms Configuration:
- CRISPY_TEMPLATE_PACK: Specifies the template pack to use for crispy forms.
- Installed Apps
- The project includes the following installed Django apps:

    - django.contrib.admin: Django administration panel.
    - django.contrib.auth: Django authentication system.
    - django.contrib.contenttypes: Django content types framework.
    - django.contrib.sessions: Django session framework.
    - django.contrib.messages: Django messaging framework.
    - django.contrib.staticfiles: Django static files management.
    - django_extensions: Additional Django extensions.
    - crispy_forms: Django forms helper.
    - tinymce: TinyMCE WYSIWYG editor.
    - create_blog: Custom app for creating blogs.
    - posts: App for managing blog posts.
    -  users: App for managing user authentication and profiles.
## Templates and Static Files
- Templates:
The project uses Django template engine with template directories specified in TEMPLATES.
- Static Files:
Static files such as CSS, JavaScript, and images are served from directories specified in STATICFILES_DIRS.
## Media Files
- Media Settings:
- MEDIA_URL: URL prefix for user-uploaded media files.
- MEDIA_ROOT: Directory where user-uploaded media files are stored.
## Authentication and Password Validation
### Authentication:
Django's authentication system is used for user management.
## Password Validation:
### Password validation settings are specified in AUTH_PASSWORD_VALIDATORS.
## Additional Configuration
### TinyMCE Configuration:
### Default configuration for the TinyMCE WYSIWYG editor is specified in TINYMCE_DEFAULT_CONFIG.
## Usage
### Run the Development Server:
- bash
- Copy code
- python manage.py runserver
- Access the Application:Open a web browser and go to http://127.0.0.1:8000/ to access the landing page.
### Login and Create Content:
- Users can create an account or login to create blogs, make posts, and interact with other users.
### Admin Panel:
- Access the Django administration panel at http://127.0.0.1:8000/admin/ to manage application data.
- Contributing
- Contributions are welcome! Please feel free to submit issues and pull requests.

