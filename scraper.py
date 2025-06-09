import requests
from bs4 import BeautifulSoup
from Objects.course_code import *
from Objects.course import *
from Objects.coordinator import *
from Objects.degree import *
from Objects.degree_plan import *
# from Objects import *

"""
Beautiful Soup Documentation:
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-the-tree

Install Dependancies at top level before running:
    pip install requests
    pip install beautifulsoup4
"""
class Scraper:
    def __init__(self):
        self.degreesArray = {}
        self.coursesArray = []

    def getSitemap(self):
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

    def scrapInfo(self, urls: dict):
        print("scraping")
        # setting up variables
        degree_name = ""

        for url in urls:
            array = url.split("/")

            soup = self.getHtml(url) #get url html data in html format
            
            if len(array) <= 8:
                degree_name = soup.find('h1').text.lstrip()
                print(degree_name)
                degree = Degree()
                degree.setDegreeName(degree_name)
                self.degreesArray[degree_name] = degree
                # grabbing course information
                entry_info = soup.find(class_="qf-wrapper__inner")
                if entry_info != None:
                    entry_info = entry_info.find_all("div")
                    for i in range(0, len(entry_info), 1):
                        print("".join(entry_info[i].text.split()))
                        self.scrapEntryInfo(entry_info[i].text, degree_name)
                        # print(entry_info[i].text)
                    # for ei in entry_info:
                    #     print("".join(ei.text.split()))
                        # print(ei.text.lstrip().rstrip())

                
            elif array[8].startswith("bp"):
                print("getting degree plan info")
                degree_name = soup.find('h1').text.split("-")[1].split(" ")
                print(degree_name[2])
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
                    # testlink = link
                    childsoup = self.getHtml(link)
                    self.scrapCourseData(childsoup)

                    print(name + " :" + link)
                # childsoup = getHtml(testlink)
            # for i in range(0, 5):
            #     print(coursesArray[i].getCode() + ": " + coursesArray[i].getCampus())



    def getHtml(self, url):
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        # text = soup.get_text(separator="\n", strip=True)
        # cleaned = "\n".join(text.splitlines()[:25])
        # result += f"\n--- {url} ---\n{cleaned}\n"
        return soup

    def scrapCourseData(self, childsoup):
        data = childsoup.find(class_="contentArea")#.find_all("p")
        # getting course code information
        term = data.find("table")
        if term != None:
            rows = term.find_all("tr")
            for row in rows:
                c = Course_Code()
                col = row.find_all("td")
                if row.find("p") != None:
                    code = col[0].find("p").text
                    campus = col[1].find("p").text
                    career = col[2].find("p").text
                    school = col[3].find("p").text
                    learning_mode = col[4].find("p").text
                    c.setCode(code)
                    c.setCampus(campus)
                    c.setCareer(career)
                    c.setSchool(school)
                    c.setLearningMode(learning_mode)
                    self.coursesArray.append(c)
                    # print(code + ": " + campus + ", " + career + ", " + school + ", " + learning_mode)
            # print(coursesArray)
            # for j in range(0, len(coursesArray)):
            #     print(coursesArray[j].getCode() + ": " + coursesArray[j].getCampus())

        # getting course information
        for d in data.find_all("p"):
            data_title = d.find("strong")
            if data_title != None:
                for dt in data_title:
                    key = dt.text
                    print(key)
                    
                    if d.text.startswith(key):
                        print(d.text[len(key):])
                    elif len(d.text) == len(key):
                        break
                    else:
                        print(d.text)
            # else:
            #     print(d.text)

    def scrapEntryInfo(self, data: str, degree_name: str):
        print(data)
        info = data.split(":")
        degree: Degree = self.degreesArray.get(degree_name)

        print(info[0])
        if info[0] == "Student type":
            print(info[1])
            # types = info[1].split()
        elif info[0] == "Entry score":
            print()
        elif info[0] == "Duration":
            print()
        elif info[0] == "Fees":
            print()
        elif info[0] == "Next intake":
            print()
        elif info[0] == "Location":
            print()
        

    # run script
    # if __name__ == '__main__':
    #     print("main")
    #     # test data
    #     urls = {}
    #     urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162"] = "2025-01-13"
    #     urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/admissions-transparency"] = "2024-06-21"
    #     urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/apply-now"] = "2025-03-11"
    #     urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/bp162oauscy"] = "2024-07-03"
    #     urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/bp162p23auscy"] = "2024-07-03"
    #     degreesArray = {}
    #     coursesArray = []
        
    #     #run scraper
    #     scrapInfo(urls)