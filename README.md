# CHAPI

## CHArlas formativas orientadas a Profesorado de Informática

Como profesorado de informática somos conscientes de la importancia de una formación continua en el tiempo, y adaptada y orientada a las necesidades de la realidad laboral. De esta necesidad surge CHAPI.

CHAPI es un evento de un día al estilo de "píldoras formativas", donde podemos participar como oyentes y/o ponentes a charlas con diferente temática orientadas al profesorado de informática.

- Está invitado a participar todo el profesorado que imparte clases de informática.
- Para participar como oyente/ponente debes rellenar un formulario para que podamos organizar el evento.
- El tema de cada charla la elige el ponente, pero teniendo como objetivo final, que sirva de ayuda/información al profesorado de informática.
- La duración de cada charla será de un máximo de 25 minutos. En el caso de impartir un taller la duración será de 1 hora máxima. Este límite se podrá ampliar si existiera disponibilidad de tiempo. 

## Modo de uso

~~~console
$ mkvirtualenv --python=python2.7 chapi
$ workon chapi
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ bower install
$ python manage.py runserver
~~~
