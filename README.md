# Dairy Flat Airways
## Assignment for Massey 159.352 Advanced Web Development

UPDATE 23-01-25: Site is offline for now as my free credit period has expired.

This is a simple server-side rendered web app developed using Django and using a SQLite database. The site is deployed live at https://gentle-ocean-42215677ebf04e34a4856bf087c26ea9.azurewebsites.net/

To build and run from a local development server on Windows:
1. Open Powershell
2. Run "./BuildWindows.ps1"
3. Run "python manage.py runserver"

The build script will create a virtual environment and switch to it, install packages specified in requirements.txt, apply the migrations and then populate the database from the fixtures.

Once the server is running, visit the address shown at the command line, this is usually localhost on port 8000. Debug mode is currently disabled. The package whitenoise is being used to serve static assets, so images and css formatting should display regardless.
