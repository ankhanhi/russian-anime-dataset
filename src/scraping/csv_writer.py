import csv


def write_to_csv(anime_list):
    with open(
        "../findanime/data/raw_data/findanime.csv", "a", newline="", encoding="utf-8"
    ) as csvfile:
        writer = csv.writer(csvfile)
        # Add Headers
        writer.writerow(
            [
                "Title",
                "Short title",
                "Href",
                "Translation",
                "Description",
                "Count episodes",
                "Genres",
                "Rating",
                "Rating count",
                "World rating",
                "Characters rating",
                "Plot rating",
                "In_process",
                "Viewed",
                "In_favor",
                "Categories",
                "Year of release",
                "Authors",
                "Studios",
                "Directors",
                "Character designers",
                "Characters",
                "Seiyuu",
                "Translators",
                "Tags",
                "Popularity",
                "Reviews",
                "Quotes",
                "Similar anime",
                "Image src",
            ]
        )
        # Add Data
        writer.writerows(anime_list)
