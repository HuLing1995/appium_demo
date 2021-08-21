import yaml
from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            caps = dict()
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = False
            caps['udid'] = yaml.safe_load(open("../page_data/configuration.yaml"))['caps']['udid']
            # 初始化driver
            self._driver = webdriver.Remote(
                "http://localhost:4723/wd/hub",
                caps)

        else:
            self._driver.start_activity(self._package, self._activity)
        self._driver.implicitly_wait(3)
        return self

    def main(self) -> Main:
        return Main(self._driver)
