# Copilot Instructions for django-practice

## Project Overview
This is a Django project with a standard structure. The main app is `myapp`, located in `project/myapp/`. The project configuration is in `project/project/`. Models, views, forms, and templates are organized by feature.

## Architecture & Data Flow
- **Apps:** The main Django app is `myapp`. All business logic, models, and views are here.
- **Models:** Defined in `project/myapp/models.py`. Example: `Estudiante` model (see file for fields).
- **Templates:** HTML templates are in `project/myapp/template/`.
- **URLs:** App-level URLs in `project/myapp/urls.py`, project-level in `project/project/urls.py`.
- **Settings:** Project settings in `project/project/settings.py`.

## Developer Workflows
- **Run Server:**
  ```powershell
  python project/manage.py runserver
  ```
- **Migrations:**
  ```powershell
  python project/manage.py makemigrations
  python project/manage.py migrate
  ```
- **Tests:**
  ```powershell
  python project/manage.py test myapp
  ```
- **Admin:** Register models in `project/myapp/admin.py` to use Django admin.

## Conventions & Patterns
- **Templates:** Use the `template/` folder inside each app for HTML files.
- **Forms:** Custom forms in `project/myapp/forms.py`.
- **Migrations:** All migration files are in `project/myapp/migrations/`.
- **Naming:** Use singular for model class names (e.g., `Estudiante`).
- **Imports:** Use relative imports within apps when possible.

## External Dependencies
- **Pipenv:** Project dependencies managed via `Pipfile` and `Pipfile.lock`.
- **Django:** Core framework. See `Pipfile` for version.

## Integration Points
- **Admin Site:** Register models in `admin.py` for admin interface.
- **Forms & Templates:** Forms in `forms.py` are rendered in templates (see `registroEstudiante.html`).

## Key Files & Directories
- `project/myapp/models.py`: Data models
- `project/myapp/views.py`: View logic
- `project/myapp/forms.py`: Custom forms
- `project/myapp/template/`: HTML templates
- `project/myapp/urls.py`: App routes
- `project/project/settings.py`: Project settings
- `Pipfile`: Dependency management

## Example Patterns
- **Model Example:**
  ```python
  class Estudiante(models.Model):
      nombre = models.CharField(max_length=100)
      edad = models.IntegerField()
  ```
- **View Example:**
  ```python
  def registro_estudiante(request):
      # ...existing code...
  ```
- **Template Usage:**
  Reference templates with `render(request, 'template/registroEstudiante.html', context)`.

---
Update this file as project conventions evolve.
