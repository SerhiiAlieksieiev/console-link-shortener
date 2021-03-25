# Console link shortener

Скрипт позволяет укоротить ссылку и узнать количество кликов по ней. Использует Bitly API и Telegram.
 
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

4. Запустите скрипт командой 

	```sh
    python main.py
    ```
 
### Переменные окружения
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом  с `main.py` и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

Доступна 1 переменная:
- `BITLY_TOKEN` — персональный токен, гайд как найти [здесь](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-generate-an-OAuth-access-token-for-the-Bitly-API-).


### Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org/referrals/eC72w2BASG9Zj3T7iMTSsxDbHXthCmJmeLKBNfwf/).
