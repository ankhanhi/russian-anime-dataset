from bs4 import BeautifulSoup
import regex as re
import numpy as np


from csv_writer import write_to_csv
from scraping_one_anime_functions import *


def scrape(session, url, headers):
    for number_page in range(0, 112):
        anime_list = []
        response = session.get(url + str(number_page * 70), headers=headers)
        html_content = response.content

        soup = BeautifulSoup(html_content, "html.parser")
        anime_container = soup.find("div", {"class": "tiles row"})
        anime_items = anime_container.find_all(class_=re.compile(r"tile col-sm-6 *"))

        # Loop through each anime item and extract the necessary information
        for anime_item in anime_items:
            title = anime_item.find("img")["title"]
            short_title = anime_item.find("div", {"class": "desc"}).find("a")["title"]
            href = (
                "https://findanime.net"
                + anime_item.find("a", {"class": "non-hover"})["href"]
            )
            image_src = anime_item.find("a", {"class": "non-hover"}).find("img")[
                "data-original"
            ]
            translation = anime_item.find(
                "span", {"class": "mangaTranslationCompleted"}
            )
            translation = translation.text if translation else "нет перевода"
            description = anime_item.find(
                "div", {"class": "manga-description"}
            ).text.strip()
            count_episodes = anime_item.find(
                "span", {"class": "badge badge-secondary amount-badge"}
            )
            count_episodes = int(count_episodes.text) if count_episodes else 0

            response_one = session.get(href, headers=headers)
            html_content_one = response_one.content
            soup_one = BeautifulSoup(html_content_one, "html.parser")

            rating_items = soup_one.find_all("meta", {"itemprop": "ratingValue"})
            rating_value, rating_count, world_rating, characters_rating, plot_rating = [
                item["content"] for item in rating_items[:5]
            ]
            release_year = soup_one.find("span", class_="elem_year")
            release_year = int(release_year.find("a").text) if release_year else None
            popularity = len(soup_one.find_all("i", class_="fa fa-lg fa-fire-alt"))
            tags = parse_tags(soup_one)
            reviews = parse_reviews(session, headers, soup_one)
            quotes = parse_quotes(session, headers, soup_one)
            similar = similar_anime(soup_one)
            in_process, viewed, in_favor = feedback(soup_one)

            anime_list.append(
                [
                    title,
                    short_title,
                    href,
                    translation,
                    description,
                    count_episodes,
                    tags["genres"],
                    rating_value,
                    rating_count,
                    world_rating,
                    characters_rating,
                    plot_rating,
                    in_process,
                    viewed,
                    in_favor,
                    tags["categories"],
                    release_year,
                    tags["authors"],
                    tags["studios"],
                    tags["directors"],
                    tags["designers"],
                    tags["characters"],
                    tags["seiyuu"],
                    tags["translators"],
                    tags["tags"],
                    popularity,
                    reviews,
                    quotes,
                    similar,
                    image_src,
                ]
            )

        # Write the anime list to a CSV file
        anime_list = np.asarray(anime_list, dtype=object)
        write_to_csv(anime_list)
