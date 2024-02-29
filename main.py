from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


credentials = {
    1: ('username1', 'password1'),
    2: ('username2', 'password2'),
    3: ('username3', 'password3'),
    4: ('username4', 'password4'),
}

# Login URL and element locators
LOGIN_URL = 'https://epitech.bamboohr.com/login.php'
USERNAME_FIELD_ID = 'lemail'
PASSWORD_FIELD_ID = 'password'
LOGIN_BUTTON_TEXT = 'Log In'
NEW_PAGE_BUTTON_TEXT_IN = 'Clock In'
NEW_PAGE_BUTTON_TEXT_OUT = 'Clock Out'

def login_with_credentials(user_id):
    # Initialize WebDriver options
    firefox_options = Options()
    firefox_options.binary_location = '/usr/bin/firefox-esr'
    firefox_options.add_argument("--headless")  # Optional: Run in headless mode

    # Setup WebDriver
    service = Service(executable_path='/usr/local/bin/geckodriver')  # Path to geckodriver
    driver = webdriver.Firefox(service=service, options=firefox_options)
    
    try:
        # Open the login page
        driver.get(LOGIN_URL)
        
        # Wait for the login input fields to be loaded
#        WebDriverWait(driver, 60).until(
#            EC.visibility_of_element_located((By.ID, USERNAME_FIELD_ID))
#        )
        
        # Get credentials for the given user ID
        username, password = credentials[user_id]
        
        # Perform login
        username = driver.find_element(By.ID, USERNAME_FIELD_ID).send_keys(username)
        print(username)
        driver.find_element(By.ID, PASSWORD_FIELD_ID).send_keys(password)
        button = driver.find_element(By.LINK_TEXT, LOGIN_BUTTON_TEXT)
        print("Found out buttons")
        print(button)
        button.click()
        time.sleep(10)
        # Wait for the new page to load
#        WebDriverWait(driver, 60).until(
#            EC.visibility_of_element_located((By.XPATH, NEW_PAGE_BUTTON_XPATH))
#        )
       
        # Click on the new button on the loaded page
        print(driver.current_url)
        driver.find_element(By.XPATH, NEW_PAGE_BUTTON_XPATH).click()
        print("CLick final")
    finally:
        driver.quit()

# Replace '/path/to/geckodriver' with the actual path to your geckodriver executable.
# If geckodriver is in your system PATH, you can omit the `executable_path` argument.

login_with_credentials(1)  # Replace with the user ID you want to test
