from typing import List
from bs4 import BeautifulSoup
import regex as re


def parse_reviews(session, headers, soup) -> List[str]:
    reviews_texts = []
    reviews_link = soup.find("a", class_="btn btn-success")["href"]
    reviews_link = "https://findanime.net/reviews/" + reviews_link.replace(
        "/internal/review/create/", ""
    )
    response = session.get(reviews_link, headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    review_links = [
        "https://findanime.net" + tag["href"]
        for tag in soup.find_all("a", class_="more-link")
    ]
    for link in review_links:
        response_one = session.get(link, headers=headers)
        html_content_one = response_one.content
        soup = BeautifulSoup(html_content_one, "html.parser")
        text = soup.find("div", class_="description manga-description").text
        reviews_texts.append(text)
    return reviews_texts


def parse_quotes(session, headers, soup_one) -> List[str]:
    quotes_texts = []
    quotes_container = soup_one.find_all("blockquote", class_="manga-quote")
    if len(quotes_container) < 0:
        quotes_texts = [tag.text for tag in quotes_container]
    else:
        quotes_link = (
            "https://findanime.net"
            + soup_one.find("div", id="tab-quotes").find_all("a")[-1]["href"]
        )
        if "quotes" in quotes_link:
            response_one = session.get(quotes_link, headers=headers)
            html_content_one = response_one.content
            soup_one = BeautifulSoup(html_content_one, "html.parser")
            quote_tags = soup_one.find_all("blockquote", class_="manga-quote")
            quotes_texts = [tag.find("p").text for tag in quote_tags]
    return quotes_texts


def similar_anime(soup):
    similar_tags = soup.find_all("div", class_="tab-content")[1].find_all(
        "div", class_=re.compile(r"tile col-sm-6 col-md-5 swiper-slide*")
    )
    similar = [
        tag.find("div", class_="desc").find("a")["title"] for tag in similar_tags
    ]
    return similar


def feedback(soup):
    marks = soup.find("div", class_="rightContent").find_all(
        "div", class_="rightBlock"
    )[-3]
    mark_info = [tag.text for tag in marks.find_all("strong")]
    if len(mark_info) == 3:
        in_process = mark_info[0] if mark_info else 0
        viewed = mark_info[1] if mark_info else 0
        in_favor = mark_info[2] if mark_info else 0
    else:
        in_process, viewed, in_favor = 0, 0, 0
    return in_process, viewed, in_favor


def parse_tags(soup):
    tags_map = {
        "categories": "elem_category",
        "genres": "elem_genre",
        "authors": "elem_author",
        "studios": "elem_studio",
        "directors": "elem_director",
        "screenwriters": "elem_screenwriter",
        "designers": "elem_characters",
        "characters": "elem_character",
        "seiyuu": "elem_voice",
        "translators": "elem_translator",
        "tags": "elem_tag",
    }

    tags = {}
    for key, val in tags_map.items():
        tags[key] = [tag.find("a").text for tag in soup.find_all("span", class_=val)]

    return tags
