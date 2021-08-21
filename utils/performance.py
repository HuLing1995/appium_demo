from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


def test_xueqiu():
    caps = {}
    caps["platformName"] = "Android"
    caps["deviceName"] = "127.0.0.1:7555"
    caps["appPackage"] = "com.xueqiu.android"
    caps["appActivity"] = ".view.WelcomeActivityAlias"
    caps['noReset'] = "true"
    # caps['chromedriverExecutable']="D:\chromedriver\chromedriver_win32/chromedriver.exe"
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, "//*[@text='交易']").click()
    webview = driver.contexts[-1]
    driver.switch_to.context(webview)
    # 查看刚进入页面的操作码：0
    print(driver.execute_script("return window.performance.navigation.type"))
    # 进入到百度页面
    driver.execute_script("window.location.href='https://www.baidu.com/'")
    # 实现页面重载操作
    driver.execute_script("window.location.reload()")
    # 查看操作码：1
    print(driver.execute_script("return window.performance.navigation.type"))
    # 查看刚进入页面的操作码：0
    print(driver.execute_script("return window.location.href"))
    # 动作模拟
    # window.history.back()
    # window.history.forward()
    # window.location.reload()
    # window.location.href = "https://www.baidu.com/"
    # 下面分别实现导航，重新加载，回退的操作码
    # const unsigned short TYPE_NAVIGATE = 0;
    # const unsigned short TYPE_RELOAD = 1;
    # const unsigned short TYPE_BACK_FORWARD = 2;
    #使用 appium 获取性能数据
    # performance = driver.execute_script("return window.performance.timing")
    # print(performance['domComplete'] - performance['responseStart'])


if __name__ == '__main__':
    test_xueqiu()
