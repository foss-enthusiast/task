# Тестовое задание  
Тестовое задание на гитхабе.  
Приложение выводит древовидное меню. Оно позволяет добавлять, редактировать и выводить меню.  

### Запуск:  
`python3 manage.py runserver`  

### Интерфейс:  
localhost:8000/admin/ - админка.  
- логин: admin  
- пароль: admin  

localhost:8000/ - тестовое меню.  

### Создать своё меню:  
1. Зайти в админку  
2. Перейти по ссылке localhost:8000/admin/catalog/menu/add/  
3. Запонить все поля именем меню и нажать кнопку 'SAVE'  
   
4. Перейти по ссылке localhost:8000/admin/catalog/item/add/  
5. Добавить произвольное количество объектов по типу:  
- title: `заголовок`  
- menu name: `имя меню`  
- parent node: `родительский узел` (здесь можно указать любой элемент из того же меню, либо само меню)  
6. Нажать кнопку 'SAVE'  

Самое интересное расположено в файле: catalog/templatetags/menus_tag.py  
