Setup:
source venv/bin/activate

Option 1:
pip3 install -r requirements.txt

Option 2:
pip3 install django==2.2 graphene-django==2.2.0 django-filter==2.0.0 django-graphql-jwt==0.1.5
pip3 install psycopg2-binary
pip3 install django-cors-headers 
pip3 install spotipy
pip3 install pandas
pip3 install redis
pip3 install -U scikit-learn

Execution:
python3 pixelstarmusic/manage.py runserver