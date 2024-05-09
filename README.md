

No ambiente Windows:

```console
cd pratica
python -m venv myworld
cd venv
cd scripts
activate.bat
cd ..
cd ..
pip install -r requirements.txt
cd agenda/
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test 
coverage html
python manage.py runserver

