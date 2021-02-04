import logging
import os
import time

import requests
import telegram

logger = logging.getLogger(__file__)


class BotLogsHandler(logging.Handler):
    def __init__(self, bot, chat_id):
        super().__init__()
        self.bot = bot
        self.chat_id = chat_id

    def emit(self, record: logging.LogRecord):
        log_entry = self.format(record)
        self.bot.send_message(chat_id=self.chat_id, text=log_entry)


def get_task_description(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def create_message_for_user(description, devman_url):
    message = 'У Вас проверили работу "{}"! \n {} \n {}'
    if description['is_negative']:
        lesson_status = 'Задача решена неверно!'
    else:
        lesson_status = 'Задача решена успешно!'
    lesson_title = description['lesson_title']
    lesson_url = devman_url.format(description['lesson_url'])
    return message.format(lesson_title, lesson_status, lesson_url)


def main():
    TG_CHAT_ID = os.environ['TG_CHAT_ID']
    TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
    DEVMAN_TOKEN = os.environ['DEVMAN_TOKEN']

    bot = telegram.Bot(token=TELEGRAM_TOKEN)

    logger.setLevel(logging.INFO)
    logger.addHandler(BotLogsHandler(bot, TG_CHAT_ID))

    devman_url = 'https://dvmn.org{}'
    devman_api_url = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': 'Token {}'.format(DEVMAN_TOKEN)}
    params = {'timestamp': time.time()}

    msg_for_error = 'Бот упал с ошибкой:'

    logger.info('Бот запущен!')

    while True:
        task_description = get_task_description(devman_api_url, headers, params)
        try:
            if task_description["status"] == "found":
                bot.send_message(
                    chat_id=TG_CHAT_ID,
                    text=create_message_for_user(
                        task_description['new_attempts'][0],
                        devman_url,
                    ),
                )
                params = {'timestamp': task_description['last_attempt_timestamp']}
            else:
                params = {'timestamp': task_description['timestamp_to_request']}
        except requests.exceptions.HTTPError:
            logger.exception(msg_for_error)
        except requests.exceptions.ReadTimeout:
            logger.exception(msg_for_error)
        except requests.exceptions.ConnectionError:
            logger.exception(msg_for_error)
            time.sleep(60)


if __name__ == '__main__':
    main()
