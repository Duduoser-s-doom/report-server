# report-server

This project was created with [django](https://www.djangoproject.com) and [rest-framework](https://www.django-rest-framework.org). Include API for client.

## API

### api/reports

### `get`

Query: name, group, page(required), count(required)
Return: {reports: Report[], count: number}

### `post`

Data: {reports: ReportRaw[]}
Return: {success: boolean}

### `put`

Data: {reports: ReportRaw[]}
Return: {success: boolean}

### `delete`

Data: {reports: Report[]}
Return: {success: boolean}

## Steps for success launch

### `.\ourvenv\Scripts\activate`

Need for activate virtual env python

### `python manage.py makemigrations`

This command make migrations in your db

### `python manage.py migrate`

And this one migrate all changes

### `python manage.py runserver`

Is run server

### `pip install <package_name>`

If package isn't install, run this
The web framework for perfectionists with..
www.djangoproject.com
