import requests
from bs4 import BeautifulSoup
import csv

class DataExtractor:
    def __init__(self, html_content):
        self.html_content=html_content

    def extract(self):
        soup=BeautifulSoup(self.html_content,"html.parser")
        title=soup.find("title").text
        description=soup.find("meta",{"name":"description"})
        if description:
            description=description.get("content")
        else:
            description=None

            keyword=soup.find("meta",{"name":"keyword"})
            internship_titles=[h3.text for h3 in soup.select("section.internship h3")]
            return(title,description,keyword,",".join(internship_titles))
        """class DataSaver:
            def _init_(self,data):
                self.data=data

            def save(self,filename):
                with open(filename, mode="w", newline="", encoding="utf-8") as file:
                    writer=csv.writer(file)
                    writer.writerow(["Tittle","Description","Keywords","Internship","Titles"])
                    writer.writerows([self.data])
                    """
class DataSaver:
    def __init__(self, data):
        self.data = data

    def save(self, filename):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Description", "Keywords", "Internship Titles"])
            writer.writerows([self.data])
class WebRequester:
    def __init__(self, url):
        self.url = url

    def request(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                print(f"Sending GET request to {self.url}")
                print(f"Response status code: {response.status_code}")
                return response.text
            else:
                raise Exception(f"Failed to fetch data. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching URL: {e}")
def main():
    url = "https://www.shadowfox.in/"
    requester = WebRequester(url)
    try:
        html_content = requester.request()
        print("Website content fetched successfully")
        if html_content:
            extractor = DataExtractor(html_content)
            data = extractor.extract()
            saver = DataSaver(data)
            saver.save("scraped_data.csv")
            print("Data extraction completed and saved to scraped_data.csv")
        else:
            print("Failed to fetch website content.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()