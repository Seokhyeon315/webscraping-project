#This code is for webscrapping Linkedin job information 
#Import chrome webdriver
from selenium import webdriver

#My chrome drvier.exe is located in LOCAL DISK
PATH="C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

#Access from the chromedriver
#Open login page
# browser.get("https://www.linkedin.com/login?")

#Enter login information--> if we log in through selenium, we will face 'I am not a robot question'
# username='shyeon96@vt.edu'
# password='dreamHigh@0315'

# elementID=browser.find_element_by_id('username')
# elementID.send_keys(username)

# elementID=browser.find_element_by_id('password')
# elementID.send_keys(password)
# elementID.submit()

#Let's directly head to job search page of linkedin
browser.get("https://www.linkedin.com/jobs")

jobtitle="aerospace engineering" # it can be changed
location="United States"

elementID=browser.find_element_by_class_name("jobtitle")
elementID.send_keys(jobtitle)

elementID=browser.find_element_by_id("location")
elementID.send_keys(location)

elementID.submit()











