import requests
from bs4 import BeautifulSoup

def scrape_coindesk():
    url = "https://www.coindesk.com/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article")

        for article in articles:
            title = article.find("h3", class_="heading").text.strip()
            author = article.find("a", class_="author").text.strip()
            date = article.find("time").text.strip()
            link = article.find("a", class_="fade").get("href")

            # Fetch full article content
            article_response = requests.get(link)
            if article_response.status_code == 200:
                article_soup = BeautifulSoup(article_response.text, "html.parser")
                content = article_soup.find("div", class_="article-content").text.strip()

                print("Title:", title)
                print("Author:", author)
                print("Date:", date)
                print("Link:", link)
                print("Content:", content)
                print("-" * 50)
            else:
                print("Failed to fetch full article:", link)

    else:
        print("Failed to fetch data")

if __name__ == "__main__":
    scrape_coindesk()
