import time
import tkinter.messagebox
from selenium import webdriver


#Selenium config with your own chromedriver path
path = "your web driver path"




#Instead of using ask_for function, you can pass here your E-mail and password

Pass = ""
E_mail = ""

#If you want to add link to your message, you have to add '\n' before, otherwise programm, won't work

mess = "Example message"

def ask_for_emailandpass():
    global Pass, E_mail, driver
    Pass = input("Password: ")
    E_mail = input("Email: ")
    driver = webdriver.Chrome(f"{path}")
    driver.maximize_window()

def post_on_Linkedin(mess,E_mail,Pass):
    driver.get("https://pl.linkedin.com")
    time.sleep(1)

    # Logging and finding publish entry butt etc.
    Log = driver.find_element_by_id("session_key")
    Log.send_keys(f"{E_mail}")

    Pas = driver.find_element_by_id("session_password")
    Pas.send_keys(f"{Pass}")

    Submit_butt = driver.find_element_by_class_name("sign-in-form__submit-button")
    Submit_butt.click()

    time.sleep(3)
    try:
        Start_publish_button = driver.find_element_by_xpath('//*[@id="ember1119"]')
        Start_publish_button.click()
    except:
        Start_publish_button = driver.find_element_by_xpath('//*[@id="ember35"]')
        Start_publish_button.click()

    time.sleep(3)


    Publish_entry = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]')
    Publish_entry.send_keys(f'{mess}')

    time.sleep(3)

    Publish_butt = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button/span')
    Publish_butt.click()

    time.sleep(2)


    driver.close()

def post_on_Twitter(mess, E_mail,Pass):
    driver.get("https://twitter.com")
    time.sleep(1)

    Find_Log_butt = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
    Find_Log_butt.click()

    time.sleep(2)

    Log = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
    Log.send_keys(E_mail)


    Submit = driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span')
    Submit.click()

    time.sleep(2)

    #Twitter phone nummer gate solution
    try:
        number = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        your_phone_number_to_verify = input("Number: ")
        number.send_keys(f"{your_phone_number_to_verify}")
        butt = driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
        butt.click()
        time.sleep(2)
    except:
        pass

    time.sleep(1)

    Pas = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    Pas.send_keys(Pass)

    time.sleep(2)

    Submit = driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
    Submit.click()

    time.sleep(2)

    Start_publish_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
    Start_publish_button.send_keys(mess)

    time.sleep(1)

    Publish_butt = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
    Publish_butt.click()

    time.sleep(2)

    driver.close()

def program():
    global E_mail, Pass

    try:
        ask_for_emailandpass()

        post_on_Linkedin(mess, E_mail, Pass)

        ask_for_emailandpass()

        post_on_Twitter(mess, E_mail, Pass)


    except:
        pass
        driver.close()
        tkinter.messagebox.showerror("Error", "An error occured while working")



program()

