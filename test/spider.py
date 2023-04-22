"""
使用selenium实现的爬虫
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 设置浏览器参数
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# 创建Chrome浏览器驱动
driver = webdriver.Chrome(options=chrome_options)

url = 'https://item.jd.com/6039832.html'
# 打开网页
driver.get(url)

# 获取页面内容
html_str = driver.page_source

# 等待页面加载完成
time.sleep(3)

# 点击【商品问答】按钮：
btn = driver.find_element(by=By.CSS_SELECTOR, value='#detail > div.tab-main.large > ul > li:nth-child(6)')
btn.click()

# 等待2秒
time.sleep(2)

# 获取【问答】信息：
aaContent = ''
aaList = driver.find_element(by=By.CSS_SELECTOR, value='#askAnswer .askAnswer-list')
aaItems = aaList.find_elements(by=By.CSS_SELECTOR, value='.askAnswer-item')
for aa in aaItems:
    ask = aa.find_element(by=By.CSS_SELECTOR, value='.ask .item-con p').text
    answer = aa.find_element(by=By.CSS_SELECTOR, value='.answer .item-con .answer-list li p').text
    aaContent = aaContent + '问：' + ask + '答：' + answer + '\n'

print(aaContent)

# 关闭浏览器
driver.quit()

