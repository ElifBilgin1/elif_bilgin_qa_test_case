import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.OpenPositionsPageLocators import JobsObjects


class JobsPage:
    def __init__(self, driver):
        self.driver = driver

    def filter_jobs(self):

        time.sleep(1)
        deneme_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "deneme"))
        )
        print("\ndeneme_element: ", deneme_element.text.strip())

        while deneme_element.text.strip() == "":
            print("\nElement is empty")
            
            try:
                WebDriverWait(self.driver, 20).until(
                    lambda driver: driver.find_element(By.ID, "deneme").text.strip() != ""
                )
                print("\ndeneme_element: ", deneme_element.text)
                break
            except:
                print("\nElement not found")

        location_filter = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, JobsObjects.location_filter_elem))
        )
        print("\nlocation_filter found")
        time.sleep(1)
        location_filter.click()
        print("\nlocation_filter clicked")
        time.sleep(1)

        location = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, JobsObjects.location_elem))
        )
        print("\nlocation found")
        time.sleep(1) 
        location.click()
        print("\nlocation clicked")

        time.sleep(1)
        department_filter = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, JobsObjects.department_filter_elem))
        )
        print("\ndepartment_filter found")
        time.sleep(1)
        department_filter.click()
        print("\ndepartment_filter clicked")
        time.sleep(1)

        time.sleep(1)
        department = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, JobsObjects.department_elem))
        )
        print("\ndepartment found")
        time.sleep(1)
        department.click()
        print("\ndepartment clicked")
        time.sleep(1)
        
        return self
        

    def get_jobs(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, JobsObjects.all_jobs_elem))
        )

