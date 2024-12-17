# библиотеки
import requests # для запросов в интернете
from bs4 import BeautifulSoup # чтобы парсить данные 
import json # для работы в json

# переменные , одна содержит url , вторая get запрос к этому url
url='https://quotes.toscrape.com/'
page = requests.get(url)

# переменные json и html файлов
file_json='data.json'
file_html='website.html'

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
    file.write("<!DOCTYPE html>\n")
    file.write('<html lang="ru">\n')
    file.write("<head>\n")
    file.write("<meta charset='UTF-8'>\n")
    file.write("<title>Quotes</title>\n")
    file.write("</head>\n")
    file.write("<body>\n")

    file.write(
        '<h1><p align="center"> <a href="https://quotes.toscrape.com/" style="color:#2196F3;">Великие цитаты</a></h1></p>\n'
    )
    file.write('<body bgcolor="#F0F8FF">\n')

    file.write(
        '<table cellspacing="2" bordercolor="#9C27B0" BGCOLOR="#E1BEE7" border="1" align="center" style="width:80%; font-family: Arial, sans-serif;">\n'
    )
    file.write("<thead>\n")
    file.write("<tr>\n")
    file.write(
        '<th style="padding:10px; color:#4A148C; font-size: 1.1em;">Номер</th>\n'
    )
    file.write(
        '<th style="padding:10px; color:#4A148C; font-size: 1.1em;">Цитата и Автор</th>\n'
    )
    file.write("</tr>\n")
    file.write("</thead>\n")
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
    file.write("</table>\n")
    file.write("</body>\n")
    file.write("</html>\n")
