import requests
import config
import iam_token_generation

def ask_gpt(text):
    headers = {
        'Authorization': f'Bearer {iam_token_generation.create_new_token()}',
        'Content-Type': 'application/json'
    }
    data = {
        "modelUri": f"gpt://{config.folder_id}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.4,
            "maxTokens": ""
        },
        "messages": [
            {
                "role": "user",
                "text": text
            }
        ]
    }

    response = requests.post("https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
                             headers=headers,
                             json=data)
    try:
        if response.status_code == 200:
            answer = response.json()["result"]["alternatives"][0]["message"]["text"]
            return answer
        else:
            return f"Ошибка: {response.status_code}"
    except:
        raise RuntimeError(
            'Invalid response received: code: {}, message: {}'.format(
                    {response.status_code}, {response.text}
            )
        )