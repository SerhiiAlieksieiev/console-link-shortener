# Console link shortener

Скрипт позволяет укоротить ссылку и узнать количество кликов по ней. Использует Bitly API.
 
### Запуск
1. Скачайте репозиторий командой

  	```sh
  	git clone https://github.com/SerhiiAlieksieiev/console-link-shortener.git
	```
	
2. Сделайте виртуальное окружение командой

	```sh
    python -m venv --copies /полный/путь/до/папки/виртуального/окружения 
    ```
	
3. Установите зависимости  командой 

	```sh
    py -m pip install -r requirements.txt
    ```
4. Добавьте [переменные окружения](https://github.com/SerhiiAlieksieiev/console-link-shortener#%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F)


5. Запустите скрипт командой с вашей ссылкой

	```sh
    python main.py https://bit.ly/3vMfewL
    ```
 
### Переменные окружения
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом  с `main.py` и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

Доступна 1 переменная:
- `BITLY_TOKEN` — персональный токен, гайд как найти [здесь](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-generate-an-OAuth-access-token-for-the-Bitly-API-).


### Цели проекта
Код написан в учебных целях — это урок в [курсе](https://dvmn.org/referrals/QKsVjuJwMKRj1Gvnum1MQwuvFh1iwkewxPkO3W5g/) по Python и API веб-сервисов на сайте [Devman](https://dvmn.org/referrals/eC72w2BASG9Zj3T7iMTSsxDbHXthCmJmeLKBNfwf/).
