from scraper import *
from dbwriter import *

from Objects.course_code import *
from Objects.course import *
from Objects.coordinator import *
from Objects.degree import *
from Objects.degree_plan import *

if __name__ == '__main__':
    print("main")

    # initialise scraper
    scraper = Scraper()

    # test level of studies
    # levels_of_study = ["pre-university-study", "vocational-study", "undergraduate-study", "postgraduate-study", "research-programs", "online"]
    # levels_of_study = ["pre-university-study", "vocational-study", "online"]
    levels_of_study = ["undergraduate-study"]

    # test data
    testing_urls = {}
    # testing_urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162"] = "2025-01-13"
    # testing_urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/admissions-transparency"] = "2024-06-21"
    # testing_urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/apply-now"] = "2025-03-11"
    # testing_urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/bp162oauscy"] = "2024-07-03"
    # testing_urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/bp162p23auscy"] = "2024-07-03"
    testing_urls["https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-physiotherapy-mc287"] = "2025-01-13"
    testing_urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/associate-degrees/associate-degree-in-aviation-professional-pilots-ad023"] = "2025-01-13"
    testing_urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-criminal-justice-bp023"] = "2025-01-13"
    testing_urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-psychology-honours-bh000/bh000ausbu"] = "2025-01-13"

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
                # print("  appending: " + str(url) + " - " + str(urls.get(url)))
                # print("    appending")
            else:
                # print("   not appending: " + str(url))
                # print("    not appending")
                pass
     
    #run scraper
    # degreesArray, coursesArray, coursesCodeArray, coordinators = scraper.scrapInfo(urls) #live sitemap scraper
    degreesArray, coursesArray, coursesCodeArray, coordinators = scraper.scrapInfo(testing_urls) #test scraper
    # scraper.scrapInfo(testing_urls)
    
    for degrees in degreesArray.values():
        print(degrees.getDegreeName())
        print(degrees.getDegreePlans().keys())
    
    