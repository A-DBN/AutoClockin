from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
LOGIN_BUTTON_XPATH = '//*[@id="passwordFields"]/div[3]/button'
NEW_PAGE_BUTTON_XPATH = '//*[@id="TIME_TRACKING"]/div/div[2]/button[1]'

def login_with_credentials(user_id):
    # Initialize WebDriver options
    chrome_options = Options()
    chrome_options.binary_location = '/usr/bin/chromium-browser'  # Path to Chromium
    chrome_options.add_argument("--headless")  # Optional: Run in headless mode

    # Setup WebDriver
    service = Service(executable_path='/usr/bin/chromedriver')  # Path to ChromeDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Open the login page
        driver.get(LOGIN_URL)
        
        # Wait for the login input fields to be loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, USERNAME_FIELD_ID))
        )
        
        # Get credentials for the given user ID
        username, password = credentials[user_id]
        
        # Perform login
        driver.find_element(By.ID, USERNAME_FIELD_ID).send_keys(username)
        driver.find_element(By.ID, PASSWORD_FIELD_ID).send_keys(password)
        driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()
        
        # Wait for the new page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, NEW_PAGE_BUTTON_XPATH))
        )
        
        # Click on the new button on the loaded page
        driver.find_element(By.XPATH, NEW_PAGE_BUTTON_XPATH).click()

    finally:
        driver.quit()