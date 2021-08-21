import yaml
from appium import webdriver


def start():
    caps = dict()
    caps["platformName"] = "android"
    caps["deviceName"] = "hogwarts"
    caps["appPackage"] = "com.xueqiu.android"
    caps["appActivity"] = ".view.WelcomeActivityAlias"
    caps["noReset"] = False
    caps['udid'] = yaml.safe_load(open("../data/page_data/configuration.yaml"))['caps']['udid']
    # 初始化driver
    driver = webdriver.Remote(
        "http://192.168.254.110:5001/wd/hub",
        caps)


if __name__ == '__main__':
    start()