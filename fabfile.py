from fabric.api import local, prefix, cd, env, run
from prettyconf import config

env.hosts = config('PRODUCTION_MACHINES',
                   cast=config.list,
                   default='yourproductionmachine')


def deploy():
    local('git push')
    with prefix('source ~/.virtualenvs/chapi/bin/activate'):
        with cd('~/chapi'):
            run('git pull')
            run('bower install')
            run('python manage.py collectstatic --noinput')
            run('python manage.py migrate')
            run('supervisorctl restart chapi')


def download_db():
    remote_host = env.hosts[0]
    local('scp {}:~/chapi/db.sqlite3 .'.format(remote_host))


def download_media():
    remote_host = env.hosts[0]
    remote_media_path = config('REMOTE_MEDIA_PATH')
    local('rsync -avh --delete {}:{}/ media/'.format(remote_host,
                                                     remote_media_path))
