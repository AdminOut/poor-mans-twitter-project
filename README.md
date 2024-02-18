# pmtweets
Just for fun

## Run django app

```
pipenv --python=3.9
pipenv shell
pipenv install
```

- Note: You can setup Python interpreter for Pycharm following directions: https://www.jetbrains.com/help/pycharm/pipenv.html#pipenv-existing-project
- Add `DJANGO_SETTINGS_MODULE=poormanstwitter.settings` to system settings (eg. .bashrc for Linux/Ubuntu)
- Run: `python manage.py runserver` and check `http://127.0.0.1:8000/`



### Linting & formatting using PEP8

```
# Check linting errors:
flake8

# Format code
black .
```
