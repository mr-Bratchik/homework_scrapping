import requests
from bs4 import BeautifulSoup

# Ключевые слова для поиска ('bash', 'mac')
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

# URL страницы со статьями
URL = "https://habr.com/ru/articles/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'lxml')
articles = soup.select("article.tm-articles-list__item")

filtered_articles = []

for article in articles:
    # Извлечение заголовка
    title_element = article.select_one("h2.tm-title.tm-title_h2")
    title = title_element.text.strip() if title_element else None

    # Извлечение превью-текста
    preview_element = article.select_one("div")
    preview_text = preview_element.text.strip() if preview_element else None

    # Извлечение даты публикации
    date_element = article.select_one("time")
    date = date_element["datetime"] if date_element else None

    # Извлечение ссылки
    link_element = title_element.select_one("a")
    link = f"https://habr.com{link_element['href']}" if link_element else None

    content = f"{title} {preview_text}".lower()

    for keyword in KEYWORDS:
        if keyword.lower() in content:
            filtered_articles.append(f"{date} – {title} – {link}")

for article in filtered_articles:
    print(article)
