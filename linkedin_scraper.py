import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re
# import pytesseract
import pickle
import logging
class LinkedInScraper:

    def __init__(self):
        self.LINKEDIN_LOGIN_URL = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
        self.OUTPUT_FILE = 'profile_data.xlsx'
        self.VISITED_PROFILES_FILE = 'visited_profiles.txt'
        self.COOKIE_FILE = 'cookies.pkl'
        # self.API_KEY = 'sk-7f'
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Setup logger
        logging.basicConfig(filename='scraping_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')
        # Manually login
            # email =  "conomi5872@hraifi.com" #Botsaiteja21@gmail.com" #conomi5872@hraifi.com
            # password = "Spe@rsoft2024"
        self.User_name = 'fizozycu@polkaroad.net' #lodyru@polkaroad.net'

        self.User_password = 'Spe@rsoft2024'

        # Set up Chrome options for headless browsing
        chrome_options = Options()
        # chrome_options.add_argument("--headless")

        # Initialize the WebDriver
        self.driver = webdriver.Chrome(options=chrome_options)
        # screenshot_folder = 'screenshots1q'
    # Helper function to load cookies
    def load_cookies(self, driver1, cookie_file):
        try:
            with open(cookie_file, 'rb') as f:
                cookies = pickle.load(f)
                for cookie in cookies:
                    driver1.add_cookie(cookie)
                return True
        except Exception as e:
            logging.error(f"Could not load cookies: {e}")
            return False

    # Helper function to save cookies
    def save_cookies(self, driver, cookie_file):
        with open(cookie_file, 'wb') as f:
            pickle.dump(self.driver.get_cookies(), f)
    # def login(self):
    #     url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
    #     self.driver.get(url)
    #     time.sleep(2)
    #     email_field = self.driver.find_element(By.ID, 'username')
    #     email_field.send_keys(self.User_name)
    #     time.sleep(2)
    #     password_field = self.driver.find_element(By.ID, 'password')
    #     password_field.send_keys(self.User_password)
    #     time.sleep(3)
    #     # login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    #     # login_button.click()
    #     password_field.send_keys(Keys.RETURN)
    def login_linkedin(self):
    
    # options.add_argument('--headless')  # Run headless if needed
    # service = Service(CHROMEDRIVER_PATH)
    # driver = webdriver.Chrome(service=service, options=options)
        # chrome_options = Options()
        # self.driver = webdriver.Chrome(options=chrome_options)
        # Navigate to LinkedIn login
        self.driver.get(self.LINKEDIN_LOGIN_URL)
        
        # If cookie exists, use it
        if os.path.exists(self.COOKIE_FILE):
            self.load_cookies(self.driver, self.COOKIE_FILE)
            time.sleep(9)
            self.driver.refresh()
        else:
            
            
            self.driver.find_element(By.ID, 'username').send_keys(self.User_name)
            time.sleep(6)
            self.driver.find_element(By.ID, 'password').send_keys(self.User_password + Keys.RETURN)
            time.sleep(30)
            
            # Handle 2FA (if needed)
            # otp = input("Enter the OTP: ")
            # otp_input = driver.find_element(By.ID, 'two-step-verification-code')
            # otp_input.send_keys(otp + Keys.RETURN)
            
            # Save session cookies after successful login
            self.save_cookies(self.driver, self.COOKIE_FILE)
        
        return self.driver

    def extract_name(self,url):
        pattern = r'https://www\.linkedin\.com/in/([^/]+)'
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        
    def take_screenshot_scroll(self,page_name,user):
        """ Takes a screenshot of the page and scrolls down to capture more content """
        SCROLL_PAUSE_TIME = 2
        total_height = self.driver.execute_script("return document.body.scrollHeight")  # Get total scrollable height
        viewport_height = self.driver.execute_script("return window.innerHeight")  # Get the height of the visible portion
        screenshot_folder = os.path.join(os.getcwd(), 'screenshots_' + user)
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
        # print(os.getcwd())
        num_screenshots = 0
        scroll_position = 0
        
        while scroll_position < total_height:
            # Save screenshot
            screenshot_path = os.path.join(screenshot_folder, f'{page_name}_{num_screenshots}.png')
            self.driver.save_screenshot(screenshot_path)
            print(f"Saved screenshot {screenshot_path}")
            
            # Scroll down by the viewport height
            self.driver.execute_script(f"window.scrollBy(0, {viewport_height});")
            time.sleep(SCROLL_PAUSE_TIME)
            
            # Update scroll position
            scroll_position += viewport_height
            num_screenshots += 1
            
            # Recalculate total height to account for lazy-loaded content
            total_height = self.driver.execute_script("return document.body.scrollHeight")

        return screenshot_folder

    # def take_screenshot_scroll(self, page_name, user):
    #     """ Takes a screenshot of the page and scrolls down to capture more content """
    #     SCROLL_PAUSE_TIME = 2
    #     total_height = self.driver.execute_script("return document.body.scrollHeight")  # Get total scrollable height
    #     viewport_height = self.driver.execute_script("return window.innerHeight")  # Get the height of the visible portion
    #     screenshot_folder = os.path.join(os.getcwd(), 'screenshots')  # Use a single folder for all users

    #     # Create the folder if it doesn't exist
    #     if not os.path.exists(screenshot_folder):
    #         os.makedirs(screenshot_folder)
    #     else:
    #         # Clear the folder before taking new screenshots
    #         for file in os.listdir(screenshot_folder):
    #             file_path = os.path.join(screenshot_folder, file)
    #             try:
    #                 if os.path.isfile(file_path):
    #                     os.unlink(file_path)  # Delete the file
    #                 # If you want to delete subdirectories, uncomment the following lines
    #                 # elif os.path.isdir(file_path): 
    #                 #     shutil.rmtree(file_path)
    #             except Exception as e:
    #                 print(f'Failed to delete {file_path}. Reason: {e}')

    #     num_screenshots = 0
    #     scroll_position = 0

    #     while scroll_position < total_height:
    #         # Save screenshot
    #         screenshot_path = os.path.join(screenshot_folder, f'{page_name}.png')  # Use a single filename
    #         self.driver.save_screenshot(screenshot_path)
    #         print(f"Saved screenshot {screenshot_path}")

    #         # Scroll down by the viewport height
    #         self.driver.execute_script(f"window.scrollBy(0, {viewport_height});")
    #         time.sleep(SCROLL_PAUSE_TIME)

    #         # Update scroll position
    #         scroll_position += viewport_height
    #         num_screenshots += 1

    #         # Recalculate total height to account for lazy-loaded content
    #         total_height = self.driver.execute_script("return document.body.scrollHeight")

    #     return screenshot_folder
        
