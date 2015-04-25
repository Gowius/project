# coding: utf-8
import os
from fabric.api import run, env, cd, roles, lcd, local, sudo

# Списком можно перечислить несколько серверов, которые у вас считаются "продакшеном"
env.roledefs['gowius'] = ['andrew@77.123.135.100']

def gowius_env():
    """Окружение для продакшена"""
    env.user = 'andrew'  # На сервере будем работать из под пользователя "git"
    env.password = "iloveJesus1612"

def g():
    lcd('/var/www/project_name/www')
    local('sudo git add .')
    local("sudo git commit -a")
    local("sudo git push origin master")

@roles('gowius')
def d():
    gowius_env()  # Инициализация окружения
    with cd('/var/www/project_name/www'):  # Заходим в директорию с проектом на сервере
        # sudo('git commit -a')
        sudo('git pull loc master')  # Пуляемся из репозитория
        sudo('kill `cat /tmp/project_name.pid`')
        sudo('find /var/www/project_name/www -name "*.pyc" -exec rm -rf {} \;')

@roles('gowius')
def u():
    gowius_env()  # Инициализация окружения
    with cd('/var/www/project_name/www/cms'):
        sudo('/var/www/env/project_name/bin/python manage.py syncdb')
        sudo('/var/www/env/project_name/bin/python manage.py migrate')
        # sudo('/var/www/env/project_name/bin/python manage.py update_translation_fields')

@roles('gowius')
def c():
    gowius_env()  # Инициализация окружения
    with cd('/var/www/project_name/www/cms'):
        sudo('/var/www/env/project_name/bin/python manage.py project_script')

@roles('gowius')
def r():
    gowius_env()  # Инициализация окружения
    sudo('reboot')



@roles('gowius')
def deploy():
    gowius_env()  # Инициализация окружения
    with cd('/var/www/project_name/data/www'):  # Заходим в директорию с проектом на сервере
        sudo('git pull loc master')  # Пуляемся из репозитория
        sudo('kill `cat /tmp/project_name.pid`')
        sudo('find /var/www/project_name/data/www -name "*.pyc" -exec rm -rf {} \;')

@roles('gowius')
def us():
    gowius_env()  # Инициализация окружения
    with cd('/var/www/project_name/data/www/cms'):
        sudo('/var/www/env/project_name/bin/python manage.py syncdb')
        sudo('/var/www/env/project_name/bin/python manage.py migrate')

def git_push():
    lcd('/Users/a1/Desktop/Python/project_name/www')
    local('sudo git add .')
    local("sudo git commit -a")
    local("sudo git push origin master")
