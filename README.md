# Django Test Application for Fogstream

Это небольшое тестовое Python/Django-приложение написано для Fogstream в качестве (вероятнее всего) проверки моих базовых навыков веб-программирования вообще и владения Django framework-ом в частности.

## Deployment

Для запуска этого приложения вам необходимо иметь:
- Python 2.7
- Django 1.11

Но вы также можете (и это рекомендуется) установить virtualenv и запускать приложение из виртуальной среды:
```
~/django_test$ . venv/bin/activate
~/django_test$ cd testproj
~/django_test/testproj$ python manage.py migrate
~/django_test/testproj$ python manage.py runserver
```

База данных будет создана автоматически, поэтому вам придется создавать учетную запись администратора самостоятельно.
```
~/django_test/testproj$ python manage.py createsuperuser
```
Итак, вы запустили приложение. Отлично! Сайт доступен по http://localhost:8000. Теперь вы можете слать письма администраторам (они указаны в ADMINS внутри testproj/settings.py).

## Email configs

EMAIL_BACKEND по умолчанию настроен на отображение писем в консоли.

На панели администратора история отправленных сообщений доступна по http://localhost:8000/admin/email_sender/usermessage/
