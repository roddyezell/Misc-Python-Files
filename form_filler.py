#! python3

import requests, openpyxl, csv, time, webbrowser, shutil, os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# Download new CSV
webbrowser.open('https://docs.google.com/spreadsheets/d/e/2PACX-1vRrBJytu9qNIpDcbgQdlun1z_61dvA7sX8yz4WwbiBEpfQ6AinqahkdlJ5aNp7VgwEMrEUmXVBxKZGi/pub?gid=1199397185&single=true&output=csv')

time.sleep(10)

shutil.move('C:\\Users\\Roddy\\Downloads\\responses - MyCAA Application Form.csv', 'C:\\Automated_WE\\responses.csv')

res = open('responses.csv')
read_data = csv.reader(res)
data = list(read_data)
row_count = len(data)

fname_lst, lname_lst, phone_lst = [], [], []
email_lst, program_lst, mycaa_lst = [], [], []
token = []

for i in range(1,row_count,1):
    mycaa_lst.append(data[i][0])
    program_lst.append(data[i][4])
    fname_lst.append(data[i][6])
    lname_lst.append(data[i][7])
    phone_lst.append(data[i][8])
    email_lst.append(data[i][11])
    token.append(data[i][13])

# merge last and first names
name_lst = [m+' '+str(n) for m,n in zip(fname_lst,lname_lst)]

# read the token value stored in the saved_token.txt file
f = open('saved_token.txt','r')
saved_token = f.read()
f.close()

# find the index value in the CSV for the token value saved in the .txt file
saved_token_index = token.index(saved_token)

# find the token value in the last cell of the CSV
last_token = token[row_count-2]

# print the index value for the token value in the last cell of the CSV file
last_token_index = token.index(token[row_count-2])

diff = last_token_index - saved_token_index

def open_form(fname, lname, email, phone, mycaa, program, saved_token, last_token):
    
    EMAILFIELD = (By.ID, "i0116")
    PASSWORDFIELD = (By.ID, "i0118")
    NEXTBUTTON = (By.ID, "idSIButton9")

    browser = webdriver.Chrome()
    browser.get('https://worldeducation.net/admin/login.html')

    # Login to the form
    button = browser.find_element_by_id('login')
    button.click()
    
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys("roddy.ezell@worldeducation.net")
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys("*293ii60")
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

    no_button = browser.find_element_by_id('idBtn_Back')
    no_button.click()

    time.sleep(10)
    
    # submit next lead until end of loop
    for i in range(saved_token+1, last_token+1, 1):

        if mycaa[i] == 'TRUE':
        
            FIRSTNAME = browser.find_element_by_css_selector('input[name="First Name"]')
            LASTNAME = browser.find_element_by_css_selector('input[name="Last Name"]')
            EMAIL = browser.find_element_by_css_selector('input[name="Email"]')
            PHONE = browser.find_element_by_css_selector('input[name="Phone"]')
            MESSAGE = browser.find_element_by_css_selector('textarea[name="LEADCF20"]')
            AFFILIATE = Select(browser.find_element_by_id('affiliate-select'))
            
            #Other dropdown menu items
            NEEDS = Select(browser.find_element_by_css_selector('select[name="LEADCF15"]'))
            INTEREST = Select(browser.find_element_by_css_selector('select[name="LEADCF18"]'))
            BENEFIT = Select(browser.find_element_by_css_selector('select[name="LEADCF125"]'))
            FIRSTNAME.send_keys(fname[i])
            LASTNAME.send_keys(lname[i])
            EMAIL.send_keys(email[i])
            PHONE.send_keys(phone[i])
            time.sleep(5)
            AFFILIATE.select_by_value("1066248000008695253")
            NEEDS.select_by_visible_text('I need help with MyCAA')
            INTEREST.select_by_visible_text('Healthcare and Fitness')
            BENEFIT.select_by_visible_text('Active Military Spouse MyCAA')
            MESSAGE.send_keys(fname[i] + ' qualifies for MyCAA and is interested in the ' + program[i] + ' program.')
   
            SUBMIT = browser.find_element_by_css_selector('input[value="Submit"]')
            SUBMIT.click()

            f = open('saved_token.txt','w')
            f.write(token[i])
            f.close()

            time.sleep(2)
    
            browser.get('https://worldeducation.net/admin/ec-submission.html')

        else:
            
            continue
        
    return None

if last_token_index > saved_token_index:
    print(str(diff) + ' new submission(s) identified.')
    open_form(fname_lst, lname_lst, email_lst, phone_lst, mycaa_lst, program_lst, saved_token_index, last_token_index)
else:
        print("Nothing new.")

os.system("C:\Automated_WE\killkill.bat")
