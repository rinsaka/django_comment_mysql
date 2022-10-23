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


## MySQL

~~~
$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.30-0ubuntu0.22.04.1 (Ubuntu)

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

mysql>
mysql> CREATE DATABASE django_comments;
Query OK, 1 row affected (0.01 sec)

mysql>
mysql> CREATE USER 'comments_user'@'localhost' IDENTIFIED BY 'xxxx';
Query OK, 0 rows affected (0.01 sec)

mysql> GRANT ALL PRIVILEGES ON django_comments.* TO 'comments_user'@'localhost';
Query OK, 0 rows affected (0.00 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.00 sec)

mysql>
~~~

- conda install
    - pip ではエラーになるので注意
~~~
$ conda install mysqlclient
$ conda install PyMySQL
~~~
