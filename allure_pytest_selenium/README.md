PyTest + Selenium + Allure Reports
----------------------------------
Здесь вы можете найти пример того, как можно 
интегрировать PyTest, Selenium и Allure Reports.


Как запустить
-------------

Для запуска этих тестов вам потребуется скачать файл Geko-Driver для
управления браузером Google Chrome.
Скачать файл можно здесь:

https://chromedriver.storage.googleapis.com/index.html?path=2.43/

После того, как вы скачаете этот файл, вам нужно установить
все зависимости:

    pip3 install -r requirements.txt
    
И после всего этого уже можно запускать тесты:

    python3 -m pytest -v --driver Chrome --driver-path /tests/chrome

Обратите внимание, что в данном случае я положил скачанный 
на первом шаге дравер для браузера в папку /tests/ -
(chrome - это имя бинарного файла). При запуске тестов вам нужно
будет указать полный путь до этого драйвера.


Как получить Allure Report
--------------------------

Самая простая версия, с использованием докер контейнера:

```bash
docker run --rm -it --name allure --volume $(pwd)"/allure_report:/home/allure/" solutis/allure:latest allure generate /home/allure/ -o /home/allure/report
```

После этого в папке allure_report/report будет лежать сгененированный отчет

Более сложная версия, с генерацией в самой системе:

Для генерации красивого Allure отчета вам нужно:

1) Установить NodeJS (https://nodejs.org/en/download/)
2) Установить Allure Console (https://www.npmjs.com/package/allure-commandline)
3) Запустить тесты, указав в качестве дирректории с результатами
папку ./allure_report
4) Сгененировать HTML отчет и открыть его:


    allure generate ./allure_report  &&  allure open allure-report


После выполнения всех 5ти шагов в браузере должен открыться Allure отчет.

Конечно, вы так же можете сгенерировать HTML Allure отчет
используя плагины для Jenkins / TeamCity.


Как установить Allure на MacOS
------------------------------

Для установки Allure на MacOS нужно выполнить следующие команды:

    brew install node
    npm install -g allure-commandline --save-dev
