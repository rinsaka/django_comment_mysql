# Django - MySQL

Python Django で データベースに MySQL を利用する．なお，環境は Ubuntu 22.04

- star project

~~~
vagrant@ubuntu2204:~/Documents/django$ pwd
/home/vagrant/Documents/django
vagrant@ubuntu2204:~/Documents/django$ django-admin startproject django_comment_mysql
vagrant@ubuntu2204:~/Documents/django$

vagrant@ubuntu2204:~/Documents/django$ cd django_comment_mysql/
vagrant@ubuntu2204:~/Documents/django/django_comment_mysql$ ls
django_comment_mysql  manage.py
vagrant@ubuntu2204:~/Documents/django/django_comment_mysql$
~~~

- runserver

~~~
python manage.py runserver 192.168.56.101:8000
~~~