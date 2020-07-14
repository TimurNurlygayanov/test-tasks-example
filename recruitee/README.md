Введение
--------

Здесь описаны основные методы REST API для получения данных из системы Recruitee.


Получение списка всех вакансий
------------------------------

     curl -X GET "https://api.recruitee.com/c/28640/offers" \
         -H "Authorization: Bearer <token>" \
         -H "Content-Type: application/json"

Здесь 28640 - это ID компании.

Документация: https://api.recruitee.com/docs/index.html#offer-offer-get


Получение подробной информации по одной вакансии
------------------------------------------------

Получить подробные данные по одной вакансии (включая список кандидатов на эту вакансию): 

    curl -X GET "https://api.recruitee.com/c/28640/offers/340176" \
        -H "Authorization: Bearer <token>" \
        -H "Content-Type: application/json"

Здесь 28640 - это ID компании, 340176 - id конкретной вакансии (можно взять из списка вакансий).

Документация: https://api.recruitee.com/docs/index.html#offer-offer-get-1

Получение списка кандидатов, назначенных на вакансию:
    
    curl -X GET "https://api.recruitee.com/c/28640/candidates?offer_id=340176" \
        -H "Authorization: Bearer <token>" \
        -H "Content-Type: application/json"
    


Получение списка кандидатов
---------------------------

Получить список всех кандидатов в системе:

    curl -X GET "https://api.recruitee.com/c/28640/candidates" \
        -H "Authorization: Bearer <token>" \
        -H "Content-Type: application/json"

Здесь 28640 - это ID компании.
Документация: https://api.recruitee.com/docs/index.html#candidate-candidate-get


Получение подробной информации о кандидате
------------------------------------------

    curl -X GET "https://api.recruitee.com/c/28640/candidates/13725542" \
        -H "Authorization: Bearer <token>" \
        -H "Content-Type: application/json"
        
Здесь 28640 - это ID компании, 13725542 - ID конкретного сотрудника.
Документация: https://api.recruitee.com/docs/index.html#candidate-candidate-get-1

Получение истории кандидата (изменение статусов, назначение на другие вакансии и пр.):

    curl -X GET "https://api.recruitee.com/c/28640/tracking/candidates/13725542/activities" \
        -H "Authorization: Bearer <token>" \
        -H "Content-Type: application/json"
