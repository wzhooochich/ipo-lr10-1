# библиотеки
import requests # для запросов в интернете
from bs4 import BeautifulSoup # чтобы парсить данные 
import json # для работы в json

# переменные , одна содержит url , вторая get запрос к этому url
url='https://quotes.toscrape.com/'
page = requests.get(url)

# переменные json и html файлов
file_json='data.json'
file_html='index.html'

# списки
quote_list= [] # цитаты
author_list = [] # авторы
result_list = [] # список для json файла

# парсинг json информации
soup= BeautifulSoup(page.text, 'html.parser')
# сбор цитат с помощью тегов 'span' 'text' , авторов - 'small' 'author'
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

# добавление авторов и цитат в списки
for quote in quotes :
    quote_list.append(quote.text)
for author in authors :
    author_list.append(author.text)

# вывод результата
for i in range(len(quote_list)):
    print(f"{i + 1}. Quote: {quote_list[i]}; Author: {author_list[i]};")

# запись в json файл
with open(file_json,'w+',encoding='utf-8') as file:
    for i in range(len(quote_list)):
        info=(f"Quote: {quote_list[i]}; Author: {author_list[i]};")
        result_list.append(info)
    json.dump(result_list, file, indent=5, ensure_ascii=False)

# оформление таблицы и запись в html файл информации из json файла 
with open(file_html, "w+", encoding="utf-8") as file:


    file.write("<tbody>\n")

    with open(file_json, "r", encoding="utf-8") as input:
        data_writer = json.load(input)
        for i, line in enumerate(data_writer):
            if isinstance(line, str):
                file.write(
                    f"<tr>\n<td style='padding: 8px; text-align:center;'>{i+1}</td>\n<td style='padding: 8px;'>{line}</td>\n</tr>\n"
                )
            else:
                print(f"Обнаружен нестроковый тип данных в data.json: {line}")


    file.write("</tbody>\n")
