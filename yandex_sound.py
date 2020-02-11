# -*- coding: utf-8 -*-
# Подключаем нужные библиотеки

import requests

import time

import json

 
# Вставьте свой API-ключ 

key = 'Secret key from the cloud'

 
# Вставьте свой путь к файлу в бакете. Всё, что в ссылке стоит после знака вопроса, можно стереть — сервер всё равно это проигнорирует

filelink = 'https://storage.yandexcloud.net/soundyandexpython/speech.ogg'

 
# Показываем «Облаку», что мы будем распознавать именно длинное аудио

POST = "https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize"

 
# Формируем сам текст запроса

body ={

    "config": {

        "specification": {

            "languageCode": "ru-RU"

        }

    },

    "audio": {

        "uri": filelink

    }

}

 
# Формируем заголовок запроса, в котором ссылаемся на API-ключ

header = {'Authorization': 'Api-Key {}'.format(key)}

 
# Отправляем запрос на распознавание

req = requests.post(POST, headers=header, json=body)

 
# Получаем технический ответ от сервера и выводим его

data = req.json()

print(data)

 
# Получаем идентификатор запроса

id = data['id']

 
# Запрашиваем на сервере статус операции, пока распознавание не будет завершено

while True:

 
    # Ждём одну секунду

    time.sleep(1)

 
    # Пытаемся получить ответ по нашему идентификатору запроса

    GET = "https://operation.api.cloud.yandex.net/operations/{id}"

    req = requests.get(GET.format(id=id), headers=header)

    req = req.json()

 
    # Если готово — выходим из цикла

    if req['done']: break

 
    # Если не вышли из цикла — выводим сообщение

    print("Ещё не готово")

 
# Выводим готовый текст 

print("Текст:")

for chunk in req['response']['chunks']:

    print(chunk['alternatives'][0]['text'])
