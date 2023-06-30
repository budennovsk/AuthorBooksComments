# AuthorBooksComments

## Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

* Deploy Railway
* 
___
## Тестовое задание от Fly Code 
Используя фреймворк Django:

* Реализовать сущности авторы, книги, комментарии
  * Связь Авторы-Книги (Many-To-Many)
  * Реализовать возможность оставлять от имени автора комментарий к книгам.
  * В сущность книги обязательно добавить флаг Archived, заархированные книги не выводить в публичной части.
* Реализовать административную часть
  * CRUD операции для авторов и книг
  * вывести список книг с обязательным указанием имени авторов в списке и кол-вом комментариев к этой книге
  * вывести список авторов с указанием кол-ва книг и кол-ва комментариев
* Реализовать публичную часть сайта с отображение авторов и их книг (простой вывод списка на странице)
  * Получение списка книг (только те книги, которые не являются заархивированными)
  * Получение списка книг выбранного автора (только те книги, которые не являются заархивированными)
  * Получение конкретной книги
  * Редактирование книги
  * Изменение флага Archived
  * Удаление книги
* Реализовать комментарии
  * Создание комментария к книге
  * Изменение комментария
  * Удаление комментария.
* Реализовать регистрацию и JWT авторизацию.*
  * Реализовать функционал  регистрации и JWT авторизации авторов
  * Получение списка книг (только те книги, которые не являются заархивированными), получить книги того автора, который авторизован в данный момент
  * Изменения/удаление/получение выбранной книги, только если она связана с автором
    
___

### Home 

![image](https://github.com/budennovsk/AuthorBooksComments/assets/97764479/ab6dacbf-60e9-43e9-b59c-40f7f64805bc)

### Авторизоция

![image](https://github.com/budennovsk/AuthorBooksComments/assets/97764479/f798dec9-1d73-4a0a-9c97-30a7a98212f3)


### Регистрация

![image](https://github.com/budennovsk/AuthorBooksComments/assets/97764479/9a787776-5e55-4033-8afc-9117ebc9ec6e)

### Postgres railway 

![image](https://github.com/budennovsk/AuthorBooksComments/assets/97764479/7629324c-b605-4431-8066-c5c93c5b1be3)

____

### Запуск проекта

* Перейти по ссылке https://authorbookscomments-production.up.railway.app/
* Авторизоваться можно либо на сайте либо в админке
* Добавление книг и авторов через админку
* Добавление комментариев через авторизованного пользователя


