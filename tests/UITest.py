import time
import unittest
from selenium import webdriver
import warnings
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from locators.CareersPageLocators import CareersObjects
from locators.OpenPositionsPageLocators import JobsObjects
from pages.Homepage import HomePage

warnings.filterwarnings("ignore", category=ResourceWarning)


class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("./chromedriver.exe"))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_home_page(self):
        # Step 1: Visit Insider home page and check if it is opened or not
        home_page = HomePage(self.driver).visit()
        assert '#1 Leader in Individualized, Cross-Channel CX — Insider' in self.driver.title

        try:
            cookie_accept_button = self.driver.find_element(By.XPATH, '//*[@id="wt-cli-accept-all-btn"]')
            cookie_accept_button.click()
        except Exception as e:
            print("Cookie button not found:", e)

        # Step 2: Select "More" menu and go to "Careers" page & Check if Career page is opened or not
        careers_page = home_page.go_to_careers()
        assert 'Insider Careers' in self.driver.title

        # Step 3: Click "See All Teams", select Quality Assurance, click "See all QA jobs",
        # filter jobs by Location - Istanbul, Turkey and department - Quality Assurance,
        # and check presence of jobs list
        jobs_page = careers_page.go_to_qa_jobs()
        time.sleep(2)
        jobs_page.filter_jobs()
        time.sleep(2)
        jobs = jobs_page.get_jobs()
        assert 'Insider Open Positions | Insider' in self.driver.title

        # Step 4: Check if all jobs' Position contains "Quality Assurance", Department contains
        # "Quality Assurance", Location contains "Istanbul, Turkey", and "View Role" button
        for i, job in enumerate(jobs):
            self.driver.execute_script(CareersObjects.scroll_into_view_script, job)
            time.sleep(1)
            self.driver.execute_script(CareersObjects.scroll_up_script)
            time.sleep(1)

            position = job.find_element(By.XPATH, '//*[@id="jobs-list"]/div[' + str(i + 1) + ']/div/p').text
            print("position: ", position)
            department = job.find_element(By.XPATH, '//*[@id="jobs-list"]/div[' + str(i + 1) + ']/div/span').text
            print("department: ", department)
            location = job.find_element(By.XPATH, '//*[@id="jobs-list"]/div[' + str(i + 1) + ']/div/div').text
            print("location:", location)

            position_element = job.find_element(By.XPATH, '//*[@id="jobs-list"]/div[' + str(i + 1) + ']/div/p')
            ActionChains(self.driver).move_to_element(position_element).perform()
            time.sleep(1)
            view_role_button = job.find_element(By.XPATH, '//*[@id="jobs-list"]/div[' + str(i + 1) + ']/div/a')
            print("view_role_button: ", view_role_button)

            assert 'Quality Assurance' in position
            assert 'Quality Assurance' in department
            assert 'Istanbul, Turkey' in location
            self.assertTrue(view_role_button)
            break

        view_role_button.click()
        time.sleep(2)
        # Yeni sekmeye geçiş yap
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])  # En son açılan sekmeye geç
        
        apply_job_button = self.driver.find_element(By.XPATH, JobsObjects.apply_job_button)
        assert apply_job_button.is_displayed(), "'Apply for this job' button is not visible"
        
        time.sleep(1)
        # Ana sekmeye geri dön
        self.driver.close()  # Mevcut sekmeyi kapat
        time.sleep(1)
        self.driver.switch_to.window(windows[0])  # İlk sekmeye geri dön
        time.sleep(1)
    
    def tearDown(self):
        self.driver.quit()
    