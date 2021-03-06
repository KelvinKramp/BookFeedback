import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime as dt
import os
import datetime
from selenium.webdriver.chrome.service import Service

# define sleep parameter
sleep_par_short = 0.1
sleep_par_long = 4

test_page = "https://urbankizbookfeedback.herokuapp.com/"
test_name = "test_name"
test_email = "test_email@email.com"
test_text = "THIS IS A TEST RUN"
keyword1 = "Readability/comprehensibilty"
keyword2 = "Feedback"


name = "/html/body/div[2]/div/div/div/div/div[2]/div[5]/input"
email = "/html/body/div[2]/div/div/div/div/div[2]/div[7]/input"
submit_button = "/html/body/div[2]/div/div/div/div/div[2]/div[8]/button"
text_area = "/html/body/div/div/div[1]/div/div[10]/div/div/textarea"
submit_button_2 = "/html/body/div/div/div[1]/div/div[34]/button"
submit_button_3 = "/html/body/div[2]/div/div/div/div/div[2]/button"
close_button = "/html/body/div[3]/div/div/div/div/div[2]/button"
report_bug = "/html/body/div/div/nav/div/div/ul/li[2]/a"
report_bug_text = "/html/body/div[2]/div/div[1]/div/div/div[2]/textarea"
report_bug_send = "/html/body/div[2]/div/div[1]/div/div/div[3]/button"
support = "/html/body/div/div/nav/div/div/ul/li[1]/a"
buy_hardcover = "/html/body/div/div/nav/div/div/ul/li[1]/div/a[2]"
buy_hardcover_send = "/html/body/div[2]/div/div[1]/div/div/div[3]/button"


class TestFeedbackApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('SETTING UP TEST UNIT')
        global driver, wait
        # https://stackoverflow.com/questions/63783983/element-not-interactable-in-selenium-chrome-headless-mode
        if "Users" in os.getcwd():
            options = Options()
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            # options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
        else:
            chrome_options = Options()
            chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            ser = Service(os.environ.get("CHROMEDRIVER_PATH"))
            driver = webdriver.Chrome(service=ser,
                                      options=chrome_options)
        wait = WebDriverWait(driver, 60)
        print("CONNECTION TO BROWSER SUCCESFULL")


    def test_a_registering(self):
        time.sleep(2)
        driver.get(test_page)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, name)))
        driver.find_element(By.XPATH, name).clear()
        element = wait.until(EC.element_to_be_clickable((By.XPATH, name)))
        driver.find_element(By.XPATH, name).send_keys(test_name)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, email)))
        driver.find_element(By.XPATH, email).clear()
        element = wait.until(EC.element_to_be_clickable((By.XPATH, email)))
        driver.find_element(By.XPATH, email).send_keys(test_email)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button)))
        driver.find_element(By.XPATH, submit_button).click()
        time.sleep(sleep_par_long)
        page_source = driver.page_source
        self.assertTrue(keyword1 in page_source)
        print("REGISTER PAGE OK")

    def test_b_report_bug(self):
        time.sleep(2)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, report_bug)))
        driver.find_element(By.XPATH, report_bug).click()
        element = wait.until(EC.element_to_be_clickable((By.XPATH, report_bug_text)))
        driver.find_element(By.XPATH, report_bug_text).send_keys(test_text)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, report_bug_send)))
        driver.find_element(By.XPATH, report_bug_send).click()
        print("REPORT BUG WINDOW OK")

    def test_c_buy_hardcover(self):
        time.sleep(2)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, support)))
        driver.find_element(By.XPATH, support).click()
        element = wait.until(EC.element_to_be_clickable((By.XPATH, buy_hardcover)))
        driver.find_element(By.XPATH, buy_hardcover).click()
        element = wait.until(EC.element_to_be_clickable((By.XPATH, buy_hardcover_send)))
        driver.find_element(By.XPATH, buy_hardcover_send).click()
        print("BUY HARDCOVER WINDOW OK")

    def test_d_submit_form(self):
        time.sleep(2)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, text_area)))
        driver.find_element(By.XPATH, text_area).send_keys(test_text)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_2)))
        driver.find_element(By.XPATH, submit_button_2).click()
        element = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_3)))
        driver.find_element(By.XPATH, submit_button_3).click()
        element = wait.until(EC.element_to_be_clickable((By.XPATH, close_button)))
        driver.find_element(By.XPATH, close_button).click()
        time.sleep(sleep_par_long)
        page_source = driver.find_element(By.XPATH, "/html/body").text
        self.assertTrue(keyword2 in page_source)
        print("SUBMITTING PROCCESS OK")

    def test_e_check_database(self):
        time.sleep(2)
        from app import db
        from sqlalchemy import text
        result1 = db.engine.execute(text("select * from feedback_book;")).fetchall()[-1]
        result2 = db.engine.execute(text("select * from report_bug;")).fetchall()[-1]
        result3 = db.engine.execute(text("select * from buy_hardcover;")).fetchall()[-1]
        results = [result1, result2, result3]
        new_list = [True for i in results if (test_name and test_email and (str(dt.now(datetime.timezone.utc).day)+"-"+str(dt.now(datetime.timezone.utc).month)+"-"+str(dt.now(datetime.timezone.utc).year))) in str(i)]
        self.assertEqual(sum(new_list), 3)
        print("DATABASE OK")

    @classmethod
    def tearDownClass(cls):
        # driver.close()
        print('TEARING DOWN CLASS')


if __name__ == '__main__':
    unittest.main()