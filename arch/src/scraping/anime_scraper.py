# Importing required libraries
import csv
from bs4 import BeautifulSoup
import regex as re
from requests_html import HTMLSession
import numpy as np

# Create an HTML session object
session = HTMLSession()

# URL of the webpage to scrape
page_url = "https://findanime.net/list?sortType=USER_RATING&offset="

# headers to include in the request
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.1.1138 Yowser/2.5 Safari/537.36",
}

# Create a list to store the anime information
anime_list = []

for i in range(1, 80):
    # Send a GET request to the website using the session and headers
    response = session.get(page_url + str(i * 70), headers=headers)
    html_content = response.content

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the main container for the list of anime
    anime_container = soup.find("div", {"class": "tiles row"})

    # Find all the anime items in the container
    anime_items = anime_container.find_all(class_=re.compile(r"tile col-sm-6 *"))

    # Loop through each anime item and extract the necessary information
    for anime_item in anime_items:
        anime_title = anime_item.find("img")["title"]
        anime_short_title = anime_item.find("div", {"class": "desc"}).find("a")["title"]
        anime_href = (
            "https://findanime.net"
            + anime_item.find("a", {"class": "non-hover"})["href"]
        )
        anime_image = anime_item.find("a", {"class": "non-hover"}).find("img")[
            "data-original"
        ]
        anime_tags = anime_item.find_all("span", {"class": "badge badge-light"})
        anime_tags = [tag.text for tag in anime_tags]
        anime_translation = anime_item.find(
            "span", {"class": "mangaTranslationCompleted"}
        )
        anime_description = anime_item.find(
            "div", {"class": "manga-description"}
        ).text.strip()
        anime_count_ep = anime_item.find(
            "span", {"class": "badge badge-secondary amount-badge"}
        )
        if anime_count_ep:
            anime_count_ep = int(anime_count_ep.text)
        else:
            anime_count_ep = 0
        if anime_translation:
            anime_translation = anime_translation.text
        else:
            anime_translation = "нет перевода"
        anime_rating = anime_item.find("b", {"class": "rate-value"})
        # anime_rating = float(anime_rating.text[10] + anime_rating.text[28:30])

        # Add the extracted information to the anime list
        anime_list.append(
            [
                anime_title,
                anime_short_title,
                anime_href,
                anime_image,
                anime_tags,
                anime_translation,
                anime_description,
                anime_count_ep,
                anime_rating,
            ]
        )

# Write the anime list to a CSV file
anime_list = np.asarray(anime_list, dtype=object)

# Write as a CSV file with headers on first line
with open("findanime.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    # Add Headers
    writer.writerow(
        [
            "Title",
            "Short title",
            "Href",
            "Image src",
            "Tags",
            "Translation",
            "Description",
            "Count episodes",
            "Rating",
        ]
    )
    # Add Data
    writer.writerows(anime_list)
