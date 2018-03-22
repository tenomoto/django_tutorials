Django tutorials

# Install Django

Install Python 3.6. 

* [Official (Windows and Mac)](https://www.python.org/downloads/release/python-364/)
* [Miniconda (Windows, Mac and Linux)](https://conda.io/miniconda.html)

FreeBSD users may install python36 and python3 from ports/pkg.
```bash
# pkg install python36 python3
```

```bash
$ sudo pip install pipenv
$ pipenv install django
$ pipenv shell
```
# Project

```bash
$ django-admin startproject mysite
> python manage.py runserver # Windows
$ ./manage.py runserver # Linux, Mac and FreeBSD
```

# hello

This app prints strings in a template.

* Add `hello` to mysite/settings.py.
* Include `hello/urls.py` in `mysite/urls.py`.
* Create a template in `hello/templates/hello/index.html`.

# weather

Prints weather forecast for Japanese cities.

Data source: [livedoor Weather Hacks](http://weather.livedoor.com/weather_hacks/)

* When `/weather` is requsted, `index` in `weather/views.py`, then `get_loc` in `weather/weather.py` is called to parse XML and city lists are rendered in `weather/templates/weather/index.html`.
* The forecast for the requested city is rendered in `weather/templates/weather/detail.html` using data constrcted from JSON in `get_forecast` in `weather/views.py` through `detail` in `weather/views.py`.

# cv

Add affiliation entries from the admin interface and render them with templates.
