import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest


# todo 1. Open Youtube URL  2. Search any text  3. Open 1st video  4. Pause video  5. Open 1st video from  right part
# todo push to github


class YoutubeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.youtube.com/")

    def test_test(self):
        # type in selenium at youtube search field and push search button
        searchFieldElement = self.driver.find_element(By.CSS_SELECTOR, "[name='search_query']")
        searchFieldElement.click()
        searchFieldElement.send_keys("selenium")
        searchFieldElement.send_keys(Keys.RETURN)

        # find first video from list and click on it
        firstPlaceholder = self.driver.find_element(By.ID, "title-wrapper")
        firstPlaceholder.click()
        time.sleep(3)

        # pause the video
        pauseVideo = self.driver.find_element(By.CSS_SELECTOR, "[data-title-no-tooltip='Pause']")
        pauseVideo.click()
        time.sleep(2)

        # find first video from right sidebar list and click on it
        rightPartFirstVideo = self.driver.find_element(By.TAG_NAME, "ytd-compact-video-renderer")
        rightPartFirstVideo.click()

        time.sleep(7)

    def tearDown(self) -> None:
        # close the driver
        self.driver.close()
