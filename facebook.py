from selenium import webdriver
from getpass import getpass 
from time import  sleep
from bs4 import BeautifulSoup
import webbrowser

usr=input('Enter Email Id >')
pwd=getpass('Enter Password >')

driver = webdriver.Chrome('/home/prakash/Downloads/chromedriver') 
driver.get('https://www.facebook.com/') 
print ("Opened facebook\n")
sleep(1)

user_Email_Name_box = driver.find_element_by_id('email')
user_Email_Name_box.send_keys(usr)
print ("Email Id entered\n") 
sleep(1)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print ("Password entered\n")

login_box = driver.find_element_by_id('loginbutton')
login_box.click()

FB_data_titals=[]
FB_data_links=[]
response = driver.execute_script('return document.documentElement.outerHTML')
soup =BeautifulSoup(response,'html.parser')
FB_data_links.append(soup.find('div',class_='_1k67 _cy7').find('a').get('href'))
name = soup.find('div',class_='_1k67 _cy7')
FB_data_titals.append("Profile "+name.text)

Mesanger = soup.find('div',{'id':'universalNav','class':'homeSideNav'})
Mesanger_li =Mesanger.findAll('li',class_='clearfix sideNavItem stat_elem')
for li in Mesanger_li:
	FB_data_links.append("https://www.facebook.com"+li.find('a').get('href'))
	FB_data_titals.append(li.text)
driver.quit()
print('\033[1;31m*####\033[1;m'+'\033[1;34m*****\033[1;m'+'\033[1;31m####*\033[1;m '+'WELCOME'+' \033[1;31m*####\033[1;m'+'\033[1;34m*****\033[1;m'+'\033[1;31m####*\033[1;m')
run=1
for titals in FB_data_titals:
	print(run,titals)
	run+=1
def play(FB):
	user=int(input('Enter the your choice >'))
	play=webbrowser.open(FB[user-1])
	print(play)
play(FB_data_links)

