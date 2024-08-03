from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# to avoid specifying the full file path, use pathlib
from pathlib import Path

# important for running wait(delay)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# also import keys - to send ctrl, backspace, shift, etc.
from selenium.webdriver.common.keys import Keys

# if you want to see how each step is executed, use sleep
from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Opening the WhatsApp web page
def open_whatsapp_window():
    driver.get("https://web.whatsapp.com/")
    # Authentication moment on WhatsApp
    wait = WebDriverWait(driver, timeout=60)  # if the subsequent element "side_bar" does not load within 60s, it will raise an error
    side_bar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]')))
    # Once it loads, we move to the moment of mapping the side bar (where contacts/messages/etc. are listed)
    side_bar = driver.find_element(by=By.XPATH, value='//*[@id="side"]')
    # Adding a global wait
    driver.implicitly_wait(2)

# Opening chat window
def open_chat_window(contact_name):  # in this case, we named it client1, but you should change it to the name saved in your contacts
    search_bar = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')   # if this xpath doesn't work, use '//div[@title="Search input box"]' # allows clearing the new user input field
    search_bar.send_keys(Keys.CONTROL + 'a')
    search_bar.send_keys(Keys.DELETE)
    
    search_bar = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')    # now performing the actual search for the contact # if this xpath doesn't work, use '//div[@title="Search input box"]'
    search_bar.send_keys(contact_name) # keyboard key, i.e., the keyboard
    
    wait = WebDriverWait(driver, timeout=5)     # wait until the WhatsApp server provides the name 
    searching_span = f'//span[@title="{contact_name}"]' # searching_span is where your contact's name is located
    lateral_chat = wait.until(EC.presence_of_element_located((By.XPATH, searching_span))) # this field "Client1" was written in uppercase because xpath is case-sensitive
    lateral_chat.click() # this allows opening the chat   # once the lateral chat is found, we click on it

def exit_chats():
    search_bar = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')
    search_bar.send_keys(Keys.CONTROL + 'a')
    search_bar.send_keys(Keys.DELETE)
    search_bar.send_keys(Keys.ESCAPE) # escape = ESC

def send_message(message): 
    message_bar = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]') # if this xpath doesn't work, use '//div[@title="Type a message"]'
    message_bar.send_keys(message)
    message_bar.send_keys(Keys.RETURN) # now to send # RETURN is the enter key on the keyboard

def send_documents(document_path): # '' ->  # map the local address of your document  # document address e.g., 'C:/user/myuser/Documents/mydocument.pdf'
    attach_button = driver.find_element(By.XPATH, '//div[@title="Attach" or @title="Attach"]') # looks for the attach button "+"
    attach_button.click()

    document_button = driver.find_element(By.XPATH, '//input[@accept="*" and @type="file"]') # send the document
    document_button.send_keys(document_path)

    send_button = driver.find_element(By.XPATH, '//div[@aria-label="Send"]')
    send_button.click() # click the send button

def send_image(image_path): # '' document address e.g., 'C:/user/myuser/Documents/bird.jpeg'
    attach_button = driver.find_element(By.XPATH, '//div[@title="Attach" or @title="Attach"]') # looks for the attach button "+" # if "attach" doesn't work, try "anexar"
    attach_button.click()

    photos_button = driver.find_element(By.XPATH, '//span[text()="Photos and videos"]/../input')
    photos_button.send_keys(image_path) # send the image

    send_button = driver.find_element(By.XPATH, '//div[@aria-label="Send"]')
    send_button.click() # click the send button

if __name__=='__main__':
    contacts = ['Client1', 'Client2', 'Client3']
    catalog_path = str(Path(__file__).parent.parent / 'catalog.pdf')    # __file__ is the current file, parent -> path to its folder, here within visual studio code
    message = """"
    Hello, {}!
    It was a pleasure meeting you.
    Sending a catalog of products for you to explore.
    Best regards!
    """

    open_whatsapp_window()

    for contact in contacts:
        open_chat_window(contact)
        sleep(1)
        send_message(message.format(contact))
        sleep(1)
        send_documents(catalog_path)
        sleep(1)
        exit_chats()
        sleep(1)
    
    sleep(200)

    # to run -> in cmd, type python3 and the path to the file
