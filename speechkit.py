import requests
#from creds import get_creds # модуль для получения токенов
from config import IAM_TOKEN, FOLDER_ID

# ФУНКЦИЯ ПРИНИМАЕТ ТЕКСТ ПЕРЕВОДИТ В ЗВУК:
def text_to_speech(text: str):
# Токен, Folder_id для доступа к Yandex SpeechKit
#    iam_token, folder_id = get_creds()  # получаем iam_token и folder_id
    iam_token = IAM_TOKEN
    folder_id = FOLDER_ID

# Аутентификация через IAM-токен
    headers = {
        'Authorization': f'Bearer {iam_token}',
    }
    data = {
        'text': text,  # текст, который нужно преобразовать в голосовое сообщение
        'lang': 'ru-RU',  # язык текста - русский
        'voice': 'filipp',  # голос Филиппа
        'folderId': folder_id,
    }
    # Выполняем запрос
    response = requests.post('https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize',
                             headers=headers,
                             data=data
                             )

    if response.status_code == 200:
        return True, response.content  # Возвращаем голосовое сообщение
    else:
        return False, "При запросе в SpeechKit возникла ошибка"

# ФУНКЦИЯ ПРИНИМАЕТ ЗВУК ПЕРЕВОДИТ В ТЕКСТ:
def speech_to_text(data):
    # Токен, Folder_id для доступа к Yandex SpeechKit
#    iam_token, folder_id = get_creds()  # получаем iam_token и folder_id
    iam_token = IAM_TOKEN
    folder_id = FOLDER_ID
    # Указываем параметры запроса
    params = "&".join([
        "topic=general",  # используем основную версию модели
        f"folderId={folder_id}",
        "lang=ru-RU"  # распознаём голосовое сообщение на русском языке
    ])

    # Аутентификация через IAM-токен
    headers = {
        'Authorization': f'Bearer {iam_token}',
    }

    # Выполняем запрос
    response = requests.post(
        f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{params}",
        headers=headers,
        data=data
    )

    # Читаем json в словарь (читаем ответ от сервера в формате JSON и преобразуем его в словарь Python для удобной обработки)
    decoded_data = response.json()
    # Проверяем, не произошла ли ошибка при запросе (С помощью метода get достаём значение по ключу из словаря. Если ключа нет, возвращаем None)
    # Метод get достаёт значение по ключу из словаря. Если ключа нет, то он возвращает None.
    if decoded_data.get("error_code") is None:
        return True, decoded_data.get("result")  # Возвращаем статус и текст из аудио
    else:
        return False, "При запросе в SpeechKit возникла ошибка"

# ВЫПОЛНЯЕМ--ТЕКСТ В ГОЛОС------------------------------------------------------------
'''
if __name__ == "__main__":
    # Текст, который хочешь преобразовать в голос
    text = "Привет! Я учусь работать с API SpeechKit. Это очень интересно!"

    # Вызываем функцию и получаем результат
    success, response = text_to_speech(text)

    if success:
        # Если все хорошо, сохраняем аудио в файл на свой комп

        # with open("output.ogg", "wb") as audio_file: – эта строка открывает файл с именем output.ogg для записи 
        # ("wb" означает "write binary", то есть запись в бинарном режиме). 
        # Бинарный режим используется, потому что аудиофайл – это не текст, а набор байтов. 
        # as audio_file говорит, что мы будем ссылаться на открытый файл как на audio_file
        
        with open("output.ogg", "wb") as audio_file:
            audio_file.write(response)
        print("Аудиофайл успешно сохранен как output.ogg")
    else:
        # Если возникла ошибка, выводим сообщение об ошибке
        print("Ошибка:", response)
        
    '''

# ВЫПОЛНЯЕМ--ГОЛОС В ТЕКСТ------------------------------------------------------------
'''
if __name__ == "__main__":
    # Укажи путь к аудиофайлу, который хочешь распознать
    # Если положить аудиофайл в одну папку с Python-файлом, который мы запускаем,
    # то в переменной audio_file_path  можно написать просто его имя
    audio_file_path = "путь/к/твоему/аудиофайлу.ogg"

    # Открываем аудиофайл в бинарном режиме чтения
#    Допустим, что наше аудио содержится в файле формата .ogg. Но передать файл нам нужно в бинарном виде.
#    Параметр "rb" в функции open  означает «read binary», 
#    то есть «прочесть бинарно» — чтение в бинарном режиме. Прямо то, что нам нужно! 

    with open(audio_file_path, "rb") as audio_file:
        audio_data = audio_file.read()

    # Вызываем функцию распознавания речи
    success, result = speech_to_text(audio_data)

    # Проверяем успешность распознавания и выводим результат
    if success:
        print("Распознанный текст: ", result)
    else:
        print("Ошибка при распознавании речи: ", result)
    
'''