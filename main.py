from scraper import *

if __name__ == '__main__':
    print("main")
    # test data
    urls = {}
    urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162"] = "2025-01-13"
    urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/admissions-transparency"] = "2024-06-21"
    urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/apply-now"] = "2025-03-11"
    urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/bp162oauscy"] = "2024-07-03"
    urls["https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162/bp162p23auscy"] = "2024-07-03"
    
    scraper = Scraper()
    #run scraper
    scraper.scrapInfo(urls)