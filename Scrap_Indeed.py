#Finding job information and required skills for each jobs 

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.indeed.com")

#Click US employement information
# US_server=driver.find_element_by_xpath("/html/body/div/div[7]/div[1]/p/a")
US_server=driver.find_element_by_xpath("/html/body/div/div[7]/div[1]/span/a")
US_server.click()

#Type job title, keywords, or company
search_job=driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div/form/div[1]/div[1]/div/div[2]/input")
search_job.send_keys(['aerospace engineering'])

#click 'find jobs' button
initial_search_button=driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div/form/div[3]/button")
initial_search_button.click()

#Sort by company name, 



#showing job title, company name, Basic Qualifications, Desired skills 
#if job post doesn't have above contents, declude them from the list 


#Need to declude if requirements sections has a word 'US citizen/US citizenship



