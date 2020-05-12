Introduction
------------

This repository contains many examples of QA Automation
tasks and code snippets. You can use it as a reference,
copy and paste the code and change as you wish.

I'm using these examples just to teach other QA engineers
to write good automated tests.

Best examples can be found in folder qa_python.


Задачи по Python
----------------

1) Посчитать количество слов в предложении

   Дано:
   
       s = "This is simple sentense."
   
   Ожидаемый результат:
   
       4

2) Найти и вывести на экран самое длинное слово в строке

   Дано:
   
       s = "This is simple sentense."
   
   Ожидаемый результат:
   
       sentense

3) Перевернуть строку задом-наперед, заменить все заглавные символы на строчные, и удалить все знаки препинания

   Дано:
   
       s = "This is simple sentense. This is not so simple sentense - but you will manage to revert this, right?"
   
   Ожидаемый результат:
   
       thgir siht trever ot eganam lliw uoy tub  esnetnes elpmis os ton si siht esnetnes elpmis si siht

4) Дан массив чисел, небоходимо удалить из него все отрицательные числа

   Дано:
   
       a = [1, 23, 56.6, -5, 23, -1, 0, 445445453]
   
   Ожидаемый результат:
   
       [1, 23, 56.6, 23, 0, 445445453]
       
5) Дан массив чисел, необходимо отсортировать его в обратном порядке

   Дано:
   
       a = [1, 23, 56.6, -5, 23, -1, 0, 445445453]
   
   Ожидаемый результат:
   
       [445445453, 56.6, 23, 23, 1, 0, -1, -5]

6) Дан массив чисел, необходимо удалить из массива все повторяющиеся элементы, оставив только уникальные элементы

   Дано:
   
       a = [1, 23, 56.6, -5, 23, -1, 0, 445445453]
   
   Ожидаемый результат:
   
       [1, 56.6, -5, -1, 0, 445445453]

7) Дана строка, самый часто встречаемый символ в строке необходимо заменить на *

   Дано:
   
       s = 'This world is amaizing place and we should be all happy.'
   
   Ожидаемый результат (самый частый символ - пробел, он встречается 10 раз):
   
       This*world*is*amaizing*place*and*we*should*be*all*happy.

8) Дан список словарей, необходимо упорядочить список по значению 'value':

    Дано:
   
       a = [{'title': 'ABC', 'value': 100}, {'title': 'EEE', 'value': 5}, {'title': '1W', 'value': 67}]
   
    Ожидаемый результат:
   
       [{'title': 'EEE', 'value': 5}, {'title': '1W', 'value': 67}, {'title': 'ABC', 'value': 100}]

9) Дан список чисел, необходимо удалить все элементы, значение которых меньше 
   среднего арифметического для данного массива:
   
    Дано:
   
       a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, -4]
   
    Ожидаемый результат:
   
       [6, 7, 8, 9, 10, 15]

10) Написать функцию, которая рисует елочку заданной высоты:

    Дано:
   
       height = 3
   
    Ожидаемый результат:
   
           *
          ***
           *
         *****
           *
        *******
           *

11) Установить библиотеку requests с помощью pip и отправить GET запрос на https://google.com, вывести на экран status_code.
