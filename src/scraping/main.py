from requests_html import HTMLSession
from scraping_all_anime import scrape


def main():
    # Create an HTML session object
    session = HTMLSession()

    # URL of the webpage to scrape
    url = "https://findanime.net/list?sortType=USER_RATING&offset="

    # headers to include in the request
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.1.1138 Yowser/2.5 Safari/537.36",
    }
    scrape(session, url, headers)


if __name__ == "__main__":
    main()
