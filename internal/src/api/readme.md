```
GET     /shows - получить список всех выставок
GET     /shows/{show_id}/result - получить результаты выставки
GET     /shows/{show_id}/animals - получить список участников выставки
PATCH    /shows/{show_id} - изменить статус выставки
PATCH    /show/{show_id}/registration - изменение записей на выставку
```

```
POST    /scores - оценить участника
```

```
GET     /animals - получить список животных
POST    /animals - создать животное
GET     /animals/{animal_id} - получить информацию о животном по его идентификатору
DELETE  /animals/{animal_id} - удалить животное
PUT     /animals/{animal_id} - обновить информацию о животном
GET     /animals/{animal_id}/shows - получить список выставок, в которых участвует животное
```

```
POST    /users - создать пользователя
GET     /users - получить всех пользователей
GET     /users/{user_id} - получить информацию о пользователе по его идентификатору
PUT     /users/{user_id} - обновить информацию о пользователе
GET     /users/{user_id}/animals - получить список животных владельца
GET     /users/{user_id}/shows - получить список животных владельца
```

```
POST    /auth/jwt/autorization - авторизация
```