# Dairy Flat Airways
## Assignment for Massey 159.352 Advanced Web Development

To build and run from a local development server on Windows:
1. Open Powershell
2. Run "./BuildWindows.ps1"
3. Run "python manage.py runserver"

The build script will create a virtual environment and switch to it, install packages specified in requirements.txt, apply the migrations and then populate the database from the fixtures.
