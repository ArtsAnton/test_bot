 Урок №1 и №2. Скрипт для отслеживания статуса проверки работ. 

Скрипт [bot.py](https://github.com/ArtsAnton/devman_hw/blob/main/bot/les_1/bot.py) оповещает зарегистрированного студента курсов [devmn.org](https://dvmn.org/modules/chat-bots/) 
о результатах проверки сданных работ сообщением в телеграм.

### Полезные ссылки:
* [Python 3.6.9;](https://www.python.org/downloads/)
* [Библиотека requests 2.25.0;](https://requests.readthedocs.io/en/master/)
* [Библиотека python-telegram-bot.](https://github.com/python-telegram-bot/python-telegram-bot#installing)

### Запуск бота
* Сделайте fork;
* Зарегистрируйтесь на [dvmn.org](https://dvmn.org), создайте бота, узнайте id вашего чата в telegram;  
* Зарегистрироваться на [heroku.com](https://www.heroku.com);
* Установите консольный клиент [heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
* [Heroku CLI Commands](https://devcenter.heroku.com/articles/heroku-cli-commands)
* Создайте приложение на heroku.com;
* Не изменяйте и не удаляйте файл [Procfile](https://github.com/ArtsAnton/test_bot/blob/main/Procfile). Определяет скрипт для запуска на heroku.com - [bot.py](https://github.com/ArtsAnton/test_bot/blob/main/bot.py);   
* На вкладке  Deploy проекта подключитесь к репозиторию с ботом;


![images1](https://github.com/ArtsAnton/test_bot/blob/main/images/connect.png)

* На вкладке Settings проекта добавьте config vars (telegram chat id, telegram token, devman token);

![images2](https://github.com/ArtsAnton/test_bot/blob/main/images/vars.png)

* На вкладке Deploy проекта нажмёте Deploy Branch;
* Бот запущен.

После запуска:
* Посмотреть список ваших приложени в heroku: heroku apps;
* Посмотреть логи запущенного бота: heroku logs -a app_name.

### Цель проекта

Код написан в образовательных целях в рамках выполнения уроков № 1 и № 2 онлайн-курса для веб-разработчиков [devmn.org](https://dvmn.org/modules/chat-bots/).
