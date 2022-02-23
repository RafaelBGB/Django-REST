# Django-REST

В файле usersapp/serializers.py, если установить значение атрибута 
fields = '__all__', при открытии страницы http://127.0.0.1:8000/api/users/
сервер падает с ошибкой:

Exception Value:	
    Could not resolve URL for hyperlinked relationship using view name 
    "permission-detail". You may have failed to include the related model 
    in your API, or incorrectly configured the `lookup_field` attribute on this 
    field.

При явном перечислении полей все работает нормально, но uid не преобразуется 
в url. Как это исправить не нашел.

Для заполнения базы создал два файла, первый (create_users_json) заполняет БД 
из другого файла json, второй (create_users_faker) заполняет БД при помощи 
factory_boy для работы которого нужно установить некоторые пакеты (все есть в 
requirements.txt).

