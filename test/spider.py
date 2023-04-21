from selenium import webdriver
from selenium.webdriver.common.by import By
import pdfkit
import base64
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

# 将HTML内容进行Base64编码
# html_bytes = html_str.encode('utf-8')
# html_b64 = base64.b64encode(html_bytes).decode('utf-8')

# 生成图片
# driver.maximize_window()
# 执行JavaScript将页面宽度设置为最大值
# driver.execute_script('document.body.style.zoom=1.0; \
#                         document.body.style.width="100%"; \
#                         document.documentElement.style.width="100%"; \
#                         document.body.style.overflowX="hidden";')

# 等待页面加载完成
time.sleep(5)

# driver.save_screenshot('screenshot.png')

# 生成PDF文件
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
# pdf_options = {
#     'page-size': 'A4',
#     'margin-top': '0.75in',
#     'margin-right': '0.75in',
#     'margin-bottom': '0.75in',
#     'margin-left': '0.75in'
# }
# driver.get('data:text/html;base64,{}'.format(html_b64))
# with open('a.pdf', 'wb') as f:
#     f.write(pdfkit.from_string(html_str, False, options=pdf_options))

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

