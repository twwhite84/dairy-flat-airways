python -m venv myenv
myenv/scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata airline/fixtures/airports.json
python manage.py loaddata airline/fixtures/customers.json
python manage.py loaddata airline/fixtures/planes.json
python manage.py loaddata airline/fixtures/routes.json
python manage.py loaddata airline/fixtures/flights.json
