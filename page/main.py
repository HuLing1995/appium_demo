from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        # self.find(By.ID, 'tv_search').click()
        self.steps("../page_data/main.yaml")

    def goto_windows(self):
        self.find(By.ID, "post_status").click()
        self.find(By.ID, 'tv_search').click()
