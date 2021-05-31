import selenium
from selenium import webdriver
from selenium.webdriver import ChromeOptions

class AnimeEntry:
    def __init__(self, title, imageHTML, rank):
        self.title = title
        self.imageHTML = imageHTML
        self.rank = rank

def find_list(type):
    #TODO specify web driver path
    #e.g. PATH = "D:\Coding\Python_Stuff\Chrome Driver\chromedriver.exe"
    PATH = _________

    chrome_options = ChromeOptions() 
    chrome_options.add_argument('headless');
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options, executable_path=PATH)

    top_airing = "//*[@id='content']/div[2]/article[1]/div/div/ul/child::*"
    top_upcoming = "//*[@id='content']/div[2]/article[3]/div/div/ul/child::*"
    top_alltime = "//*[@id='content']/div[2]/article[5]/div/div/ul/child::*"

    top_elements = []

    driver.get("https://myanimelist.net/")
    driver.implicitly_wait(5)

    if(type == "top_airing"):
        top_elements = driver.find_elements_by_xpath(top_airing)
    elif(type == "top_upcoming"):
        top_elements = driver.find_elements_by_xpath(top_upcoming)
    elif(type == "top_alltime"):
        top_elements = driver.find_elements_by_xpath(top_alltime)

    top_list = []

    rank = 1
    for i in top_elements:
        srcset = i.find_element_by_xpath("./p/a/img").get_attribute("data-srcset")
        imagesrc = srcset.split(",")[1][:-3]
        print(imagesrc)
        title = i.find_element_by_xpath("./div/h3/a").text
        top_list.append(AnimeEntry(title, imagesrc, rank)) 
        rank += 1
    driver.quit()
    
    return top_list



