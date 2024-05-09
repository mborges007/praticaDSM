

No ambiente Windows:

```console

cd pratica
=====Para iniciar ambiente virtual
python -m venv myworld
myworld\Scripts\activate.bat

=====Instalar requirements
pip install -r requirements.txt
cd agenda/
python manage.py migrate
python manage.py test

python manage.py makemigrations --> apos mudar algo no models

****TESTES*****
coverage run --source='.' manage.py test 
coverage report ----> Porcentagem de erros 
coverage html 

python manage.py runserver




