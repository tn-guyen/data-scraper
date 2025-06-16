from scraper import *
from dbwriter import *

from Objects.course_code import *
from Objects.course import *
from Objects.coordinator import *
from Objects.degree import *
from Objects.degree_plan import *
# from Objects.course_contact import *

if __name__ == '__main__':
    # initialise scraper
    scraper = Scraper()

    # test level of studies
    # levels_of_study = ["pre-university-study", "vocational-study", "undergraduate-study", "postgraduate-study", "research-programs", "online"]
    levels_of_study = ["undergraduate-study", "postgraduate-study", "online"]

    # getting sitemap
    site_map = scraper.getSitemap()

    # dictionary for filtering relelvant urls
    urls = {}
    urls_to_ignore = ["admissions-transparency", "apply-now", "success", "industry-snapshots", "register-your-interest", "register-industry-snapshot"]
    # filtering urls
    for url in site_map:
        array = url.split("/")
        if len(array) > 5 and array[5] in levels_of_study:
            # print(url)
            if len(array) > 7 and array[-1] not in urls_to_ignore and array[-2] not in urls_to_ignore:
                urls.update({url : site_map.get(url)})

    #run scraper
    degreesArray, coursesArray, coursesCodeArray, coordinators = scraper.scrapInfo(urls) #live sitemap scraper

    # initialise dbwriter
    db_path = "dcnc.db"
    db_writer = DBWriter(db_path)

    # save scraped data
    db_writer.writeCoordinator(coordinators)
    db_writer.writeCourseCode(coursesCodeArray)
    db_writer.writeCourses(coursesArray)
    db_writer.writeDegree(degreesArray)