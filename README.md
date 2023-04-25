# Web Scraping - Anime List on Russian
### Introduction
This project utilizes web scraping methods to extract information about anime from the website https://findanime.net. The extracted data includes the anime's title, short title, image source, tags, translation status, description, episode count, and its rating across 30 features. The extracted information is then saved as a CSV file.
![animes](https://user-images.githubusercontent.com/78269149/217189991-4f03a26d-1380-4826-98d9-b47dbd1330d9.png)

# Anime Scraper

This code scrapes anime information from a certain website using the BeautifulSoup library, regex library, and numpy library. The scraper will loop through every page of anime, extract information about each anime in the page, and write it to a CSV file using the csv_writer utility.

## Getting Started

The following command should be run to install the dependencies:

```pip install -r requirements.txt```

To use this scraper, simply run the scrape function in src/scraping/main.py with the desired session, URL, and headers. The function will loop through every page of anime, extract information about each anime in the page, and write it to a CSV file.

## Functionality

The scraper will extract the following information for each anime:

1. Title
2. Short Title
3. URL
4. Translation
5. Description
6. Number of Episodes
7. Genres
8. Rating Value
9. Ratings Count
10. World Rating
11. Characters Rating
12. Plot Rating
13. In Process Feedback
14. Viewed Feedback
15. In Favor Feedback
16. Categories
17. Release Year
18. Authors
19. Studios
20. Directors
21. Designers
22. Characters
23. Seiyuu
24. Translators
25. Tags
26. Popularity
27. Reviews
28. Quotes
29. Similar Anime
30. Image Source URL

Note that if any of the information is missing, the corresponding column will contain "None" or "нет перевода" for Translation.

### Conclusion
This project demonstrates the use of web scraping techniques to extract information from a website and save it as a CSV file. The techniques used in this project can be adapted and applied to other similar use cases.

### Limitations
- The script does not handle cases where the website structure changes, so it may stop working if the website changes its HTML structure.
- The script does not handle errors that may occur when making a request to the website or parsing the HTML content.

### Contributions
Feel free to fork the repository and make any necessary changes or improvements. If you have any suggestions or find any bugs, please open an issue in the repository.
