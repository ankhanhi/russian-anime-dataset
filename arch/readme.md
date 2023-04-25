# Web Scraping - Anime List on Russian
### Introduction
This project uses web scraping techniques to extract information about anime from the website https://findanime.net. The information extracted includes the title, short title, image source, tags, translation status, description, count of episodes, and rating of each anime. The extracted information is then saved as a CSV file.
![animes](https://user-images.githubusercontent.com/78269149/217189991-4f03a26d-1380-4826-98d9-b47dbd1330d9.png)

### Requirements
The following libraries are required to run the code in this project:

tool | task
--- | ---
`Python 3` | program language
`csv` | For writing the scraped data to a CSV file.
`requests` | To send HTTP requests to the website.
`bs4` | For parsing the HTML content of the website.
`regex` | For compiling regular expressions.
`requests_html` | To create an HTML session object for sending HTTP requests.
`numpy` | For converting a list to a numpy array.

### Usage
1. Clone the repository or download the script file findanime_scraper.ipynb.
2. Install the required libraries by running the following command in your terminal or command prompt:

```
pip install requests bs4 requests_html
```
3. Run a Jupyter Notebook on a local or remote server
4. The resulting CSV file anime.csv will be created in the same directory as the script file.

### Code
The code starts by importing the required libraries and creating an HTML session object using the requests_html library. The URL of the webpage to scrape is then specified, along with the headers to include in the request.

Next, a list `anime_list` is created to store the information about each anime. A for loop is used to send a `GET` request to the website using the session and headers for each page of the anime list. The HTML content of the response is then parsed using the `BeautifulSoup` library.

The main container for the list of anime on each page is found, and all the anime items in the container are extracted. For each anime item, the necessary information is extracted and added to the `anime_list`. This includes the title, short title, href, image source, tags, translation status, description, count of episodes, and rating of each anime.

Finally, the `anime_list` is converted to a numpy array and written to a CSV file with headers on the first line.

### Conclusion
This project demonstrates the use of web scraping techniques to extract information from a website and save it as a CSV file. The techniques used in this project can be adapted and applied to other similar use cases.

### Limitations
- The script only collects information from Findanime.net anime page list.
- The script does not handle cases where the website structure changes, so it may stop working if the website changes its HTML structure.
- The script does not handle errors that may occur when making a request to the website or parsing the HTML content.

### Contributions
Feel free to fork the repository and make any necessary changes or improvements. If you have any suggestions or find any bugs, please open an issue in the repository.
