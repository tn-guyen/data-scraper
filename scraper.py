import requests
from bs4 import BeautifulSoup

"""
Beautiful Soup Documentation:
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-the-tree

Install Dependancies at top level before running:
    pip install requests
    pip install beautifulsoup4
"""

def main():
    print("main")
    # test data
    urls = {}
    urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162"] = "2025-01-13"
    urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/admissions-transparency"] = "2024-06-21"
    urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/apply-now"] = "2025-03-11"
    urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/bp162oauscy"] = "2024-07-03"
    urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/bp162p23auscy"] = "2024-07-03"

    #run scraper
    scrapInfo(urls)

def getSitemap():
    xml_dict = {}

    r = requests.get("https://rmit.edu.au/sitemap.xml")
    xml = r.text

    soup = BeautifulSoup(xml, "lxml")
    urls = soup.find_all("url")

    print(f"The number of sitemaps are {len(urls)}")

    for url in urls:
        loc, lastmod = url.find_next("loc").text, url.find_next("lastmod").text
        # xml_dict[sitemap.findNext("loc").text] = sitemap.findNext("lastmod").text
        array = loc.split("/")
        if len(array) > 5 and array[5] == "undergraduate-study":
            xml_dict[loc] = lastmod

    print(len(xml_dict))

def scrapInfo(urls: dict):
    print("scraping")
    degree = ""
    for url in urls:
        array = url.split("/")

        soup = getHtml(url) #get url html data in html format
        
        if len(array) <= 8:
            degree = soup.find('h1').text.lstrip()
            print(degree)

            print("getting degree information")
            
        elif array[8].startswith("bp"):
            print("getting degree plan info")
            data = soup.find(class_="rmit-bs plan-page both")
            text = data.get_text(separator="\n", strip=True)
            cleaned = "\n".join(text.splitlines()[:200])
            # result += f"\n--- {url} ---\n{cleaned}\n"
            # print(text)

            courses = data.find_all(class_="courseLine")
            testlink = ""
            for course in courses:
                tag = course.find_next("a")
                name = tag.text
                link = tag.find_next(href=True)["href"]
                testlink = link
                print(name + " :" + link)
            childsoup = getHtml(testlink)
            print(childsoup)


def getHtml(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    # text = soup.get_text(separator="\n", strip=True)
    # cleaned = "\n".join(text.splitlines()[:25])
    # result += f"\n--- {url} ---\n{cleaned}\n"
    return soup

# run script
main()