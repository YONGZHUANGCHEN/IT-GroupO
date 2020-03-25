how to deploy this project
===

# python
python >= 3.7.4

# create virtualenv and activate it
```shell script
python -m venv env
source env/bin/activate
```
# install packages

```shell script
pip install -r requirements.txt
```

# migrations

```shell script
python manage.py makemigrations user_profile CPUNerd
python manage.py migrate
```

# populate example data

```shell script
python manage.py loaddata db.json
```

# run develop server
```shell script
python manage.py runserver
```
need comment `STATIC_ROOT = os.path.join(BASE_DIR, "static")` in `settings.py`

# collect static files
```shell script
python manage.py collectstatic
```
need uncomment `# STATIC_ROOT = os.path.join(BASE_DIR, "static")` in `settings.py`

# for social login with Facebook
### # the Facebook auth key and secrete
edit `fb_secrete.py`

### # the web site must running in https, and all related urls have to be supplied to Facebook develop site
look this <https://stackoverflow.com/questions/49489888/cant-load-url-the-domain-of-this-url-isnt-included-in-the-apps-domains-djan>
