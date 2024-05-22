import requests
import config
import sqlite3
import iam_token_generation

def count_tokens(prompt_or_answer):
    """
    ФУНКЦИЯ ДЛЯ ПОТЩЕТА ТОКЕНОВ ИСПОЛЬЗОВАННЫХ ПОЛЬЗОВАТЕЛЕМ
    """
    headers = {
        'Authorization': f'Bearer {iam_token_generation.create_new_token()}',
        'Content-Type': 'application/json'
    }
    data = {
       "modelUri": f"gpt://{config.folder_id}/yandexgpt/latest",
       "maxTokens": config.MAX_TOKENS,
       "text": prompt_or_answer
    }
    return len(
        requests.post(
            "https://llm.api.cloud.yandex.net/foundationModels/v1/tokenize",
            json=data,
            headers=headers
        ).json()['tokens']
    )

def SUM():
    connection = sqlite3.connect('users.db')
    cur = connection.cursor()
    results = cur.execute(f'SELECT SUM(tokens) FROM users3')
    for res in results:
        if res[0] != None:
            summ = res[0]
        else:
            summ = 0
        return summ

def count_tokens_in_project(message):
    count = 0
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    results = cursor.execute(f'SELECT SUM(tokens) FROM users3;')
    for result in results:
        if result[0] == None:
            count = 0
        else:
            count += result[0]
    if count >= config.MAX_TOKENS_FOR_PEOPLE:
        a = "Вы израсходовали все, данные вам, токены!"
        return False, a
    else:
        return "Все хорошо"

