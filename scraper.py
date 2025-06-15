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
    ----------Windows----------
    pip install requests
    pip install beautifulsoup4
    pip install lxml
    ------------Mac------------
    pip3 install requests
    pip3 install beautifulsoup4
    pip3 install lxml

    for dcnc codebase add to requirements.txt if needed
"""

class Scraper:
    def __init__(self):
        self.degreesArray = {}
        self.coursesArray = {}
        self.coursesCodeArray = {}
        self.coordinators = {}

    def getSitemap(self):
        xml_dict = {}

        r = requests.get("https://rmit.edu.au/sitemap.xml")
        xml = r.text

        soup = BeautifulSoup(xml, features="xml")
        urls = soup.find_all("url")

        print(f"The number of sitemaps are {len(urls)}")

        for url in urls:
            loc, lastmod = url.find_next("loc").text, url.find_next("lastmod").text
            xml_dict[loc] = lastmod

        # print(len(xml_dict))
        return xml_dict

    def scrapInfo(self, urls: dict):
        print("scraping")
        # setting up variables
        degree_name = ""

        for url in urls:
            array = url.split("/")

            soup = self.getHtml(url) #get url html data in html format
            degree_name = soup.find('h1').text.lstrip()

            if degree_name in self.degreesArray.keys():
                degree = self.degreesArray.get(degree)
            else:
                degree = Degree()

            if len(array) > 0:
                if degree_name not in self.degreesArray.keys():
                    print(degree_name)
                    # print(degree_name + " - " + str(url))

                    degree.setDegreeName(degree_name)
                    self.degreesArray[degree_name] = degree
                    degree.setLevelOfStudy(array[6].replace("-", " "))
                    # grabbing course information
                    print("    getting entry information")
                    entry_info = soup.find(class_="qf-wrapper__inner")
                    if entry_info != None:
                        entry_info = entry_info.children
                        for ei in entry_info:
                            self.scrapEntryInfo(ei.text, degree_name)
                        print("        completed")
                else:
                    print("degree exists: " + str(degree_name))

                plans_url = soup.find_all(text="View plan")

                for pu in range(0, int(len(plans_url) / 2)):
                    plan = DegreePlan()
                    href = "https://www.rmit.edu.au" + plans_url[pu].find_next(href=True)["href"]
                    print(href)
                    plansoup = self.getHtml(href)
                    # print("    getting degree plan info: " + plansoup.find('h1').text.lstrip())
                    if len(plansoup.find('h1').text.split("-")) > 1:
                        degree_plan = plansoup.find('h1').text.split("-")[1].split(" ")
                        degree_name = plansoup.find('h1').text.split("-")[0].rstrip()
                        # degree = self.degreesArray.get(degree_name.lstrip())
                        plan.setDegreeName(degree_name)
                        plan.setPlanCode(degree_plan[2])
                        print(degree_plan[2])
                        # data = plansoup.find(class_="rmit-bs plan-page both")
                        # if data == None:
                        #     data = plansoup.find(class_="rmit-bs plan-page ")
                        # text = data.get_text(separator="\n", strip=True)
                        # cleaned = "\n".join(text.splitlines()[:200])
                        # result += f"\n--- {url} ---\n{cleaned}\n"
                        # print(text)
                        require_tables = plansoup.find_all(class_="requirementRequirementHTML")
                        for rt in require_tables:
                            section = rt.find_previous_sibling(class_="requirementDescription").text
                            print(section)
                            courses = rt.find_all(class_="courseLine")
                            for course in courses:
                                columns = course.find_all("td")
                                if len(columns) > 2:
                                    code = columns[2].text
                                    tag = course.find_next("a")
                                    name = tag.text
                                    link = tag.find_next(href=True)["href"]
                                    if code not in self.coursesArray:
                                        # print("   getting course: " + str(code))
                                        if link != "/":
                                            childsoup = self.getHtml(link)
                                            self.scrapCourseData(childsoup)
                                            # changed i made
                                            # self.scrapCourseData(childsoup, code)

                                    else:
                                        # print("   course scrapped already: " + str(code))
                                        pass
                                else:
                                    # print("    multiple course code - double up")
                                    pass
                                self.planSection(section, code, plan)
                        if degree != None:
                            degree.setDegreePlans(plan)

                        # courses = data.find_all(class_="courseLine")
                        # for course in courses:
                        #     columns = course.find_all("td")
                        #     if len(columns) > 2:
                        #         code = columns[2].text
                        #         tag = course.find_next("a")
                        #         name = tag.text
                        #         link = tag.find_next(href=True)["href"]
                        #         if code not in self.coursesArray:
                        #             print("   getting course: " + str(code))
                        #             childsoup = self.getHtml(link)
                        #             self.scrapCourseData(childsoup)
                        #             print("        completed")
                        #         else:
                        #             print("   course scrapped already: " + str(code))
                        #     else:
                        #         print("    multiple course code - double up")
                        #         pass
            # elif array[8].startswith("bp"):
            # else:
            #     print("getting degree plan info: " + soup.find('h1').text)
            #     if len(soup.find('h1').text.split("-")) > 2:
            #         degree_plan = soup.find('h1').text.split("-")[1].split(" ")
            #         degree_name = soup.find('h1').text.split("-")[0].rstrip()
            #         degree = self.degreesArray.get(degree_name)
            #         print(degree_plan[2])
            #         data = soup.find(class_="rmit-bs plan-page both")
            #         text = data.get_text(separator="\n", strip=True)
            #         cleaned = "\n".join(text.splitlines()[:200])
            #         # result += f"\n--- {url} ---\n{cleaned}\n"
            #         # print(text)

            #         courses = data.find_all(class_="courseLine")
            #         testlink = ""
            #         for course in courses:
            #             columns = course.find_all("td")
            #             code = columns[2].text
            #             tag = course.find_next("a")
            #             name = tag.text
            #             link = tag.find_next(href=True)["href"]
            #             # testlink = link
            #             if code not in self.coursesArray:
            #                 print("   getting course: " + str(code))
            #                 childsoup = self.getHtml(link)
            #                 self.scrapCourseData(childsoup)
            #             else:
            #                 print("   course scrapped already: " + str(code))

                    # print(name + " :" + link)
                # childsoup = getHtml(testlink)
            # for i in range(0, 5):
            #     print(coursesArray[i].getCode() + ": " + coursesArray[i].getCampus())
        return self.degreesArray, self.coursesArray, self.coursesCodeArray, self.coordinators

    def getHtml(self, url):
        try:
            response = requests.get(url, timeout=15)
            soup = BeautifulSoup(response.text, "html.parser")
            # text = soup.get_text(separator="\n", strip=True)
            # cleaned = "\n".join(text.splitlines()[:25])
            # result += f"\n--- {url} ---\n{cleaned}\n"
            return soup
        except:
            return None


    def scrapCourseData(self, childsoup):
        # changed i made
    # def scrapCourseData(self, childsoup, code):
        if childsoup != None:
            data = childsoup.find(class_="contentArea")#.find_all("p")
            course = Course()
            heading = childsoup.find("h2").next_sibling
            course_name = heading.text.lstrip("Course Title: ")
            # course_name = childsoup.find(text="Course Title: ").parent.next_sibling
            course.setCourseTitle(course_name)
            try:
                points_string = heading.next_sibling
                # points_string = childsoup.find(text="Credit Points: ").parent.next_sibling
                points = int(points_string.text.lstrip("Credit Points: "))
            except ValueError:
                points = 0
            course.setCreditPoints(points)

            # getting course code information
            term = data.find("table")

            if term != None:
                rows = term.find_all("tr")
                for row in rows:
                    c = CourseCode()
                    col = row.find_all("td")
                    if row.find("p") != None and len(col) > 3:
                        code = col[0].find("p").text
                        campus = col[1].find("p").text
                        career = col[2].find("p").text
                        school = col[3].find("p").text
                        learning_mode = col[4].find("p").text
                        c.setName(course_name)
                        c.setCode(code)
                        c.setCampus(campus)
                        c.setCareer(career)
                        c.setSchool(school)
                        c.setLearningMode(learning_mode)
                        self.coursesCodeArray.update({code : c})
                        course.updateCourseCode(c)
                        # print(code + ": " + campus + ", " + career + ", " + school + ", " + learning_mode)
                # print(coursesArray)
                # for j in range(0, len(coursesArray)):
                #     print(coursesArray[j].getCode() + ": " + coursesArray[j].getCampus())

            # getting course coordinator information
            coordinator = Coordinator()
            for d in data.find_all("p"):
                d_text = d.text
                if ":" in d_text:
                    info = d_text.split(":")
                    if info[0] == "Course Coordinator":
                        coordinator.setCoordinatorName(info[1].lstrip())
                    elif info[0] == "Course Coordinator Phone":
                        coordinator.setCoordinatorPhone(info[1].lstrip())
                    elif info[0] == "Course Coordinator Email":
                        coordinator.setCoordinatorEmail(info[1].lstrip())
                    elif info[0] == "Course Coordinator Location":
                        coordinator.setCoordinatorLocation(info[1].lstrip())
                    elif info[0] == "Course Coordinator Availability":
                        coordinator.setCoordinatorAvailability(info[1].lstrip())
                elif d == "Pre-requisite Courses and Assumed Knowledge and Capabilities":
                    line = childsoup.find(text=d_text).next_sibling
                    while "<strong>" not in line:
                        print(line.text)
                        line = childsoup.find(text=line.text).next_sibling
                    print()
            self.coordinators.update({coordinator.getCoordinatorName() : coordinator})
            course.setCourseCoordinator(coordinator.getCoordinatorName())
            self.coursesArray.update({course_name : course})

            # changed i made
            # course_code = course.getCourseCode()
            # if course_code:
            #     self.coursesArray[course] = course

    def scrapEntryInfo(self, data: str, degree_name: str):
        # print(data)
        if ":" in data:
            degree: Degree = self.degreesArray.get(degree_name)

            info = data.split(":")
            heading = " ".join(info[0].split())
            value = " ".join(info[1].split())
            if heading == "Student type":
                types = value.split(" ")
                for t in types:
                    degree.setAvailability(t.lower(), True)
            elif heading == "Learning mode":
                if degree.getLearningMode().get("domestic") == None:
                    degree.setLearningMode("domestic", value)
                else:
                    degree.setLearningMode("international", value)
            elif heading == "Entry score":
                if degree.getEntryScore().get("domestic") == None:
                    degree.setEntryScore("domestic", value)
                else:
                    degree.setEntryScore("international", value)
            elif heading == "Duration":
                if degree.getDuration().get("domestic") == None:
                    degree.setDuration("domestic", value)
                else:
                    degree.setDuration("international", value)
            elif heading == "Fees":
                if degree.getFees().get("domestic") == None:
                    degree.setFees("domestic", value)
                else:
                    degree.setFees("international", value)
            elif heading == "Next intake":
                if degree.getNextIntake().get("domestic") == None:
                    degree.setNextIntake("domestic", value)
                else:
                    degree.setNextIntake("international", value)
            elif heading == "Location":
                if degree.getLocation().get("domestic") == None:
                    degree.setLocation("domestic", value)
                else:
                    degree.setLocation("international", value)

    def planSection(self, section, course: str, plan: DegreePlan):
        if "Year" in section:
            plan.setCoreUnits(section, course)
        else:
            spl_sec = section.split(":")
            if len(spl_sec) > 1:
                type = spl_sec[0]
                name = spl_sec[1].lstrip()
                if type == "Major":
                    plan.setMajorOptions(section, course)
                elif type == "Minor":
                    plan.setMinorOptions(section, course)
            else:
                plan.setOtherOptions(section, course)

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