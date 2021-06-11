# Телеграм-бот для моніторингу подій смарт-контрактів
## Телеграм
Для взаємодії з Телеграмом використовується бібліотека [pyTelegramBotAPI.](https://github.com/eternnoir/pyTelegramBotAPI)
## MongoDB
Для взаємодії з MongoDB використовується бібліотека [pymongo.](https://github.com/mongodb/mongo-python-driver)
## Ethereum
Для взаємодії з Ethereum використовується бібліотека [Web3.py.](https://github.com/ethereum/web3.py)
## Infura
Для отримання адреси API Ethereum скористайтесь [Infura.](https://infura.io/login)
## Getting started
Переконайтеся, що ви замінили TOKEN на власний маркер API в файлі .
```
bot = telebot.TeleBot("TOKEN")
```
Та переконайтесь що замінили Blockchain на адресу API отриману від Infura.
```
blockchain = web3.Web3(web3.Web3.HTTPProvider('Blockchain'))
```
