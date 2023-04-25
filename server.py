from flask import Flask, jsonify, request
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
import time

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/about')
def about():
    return 'About'


# 设置浏览器参数
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# 创建Chrome浏览器驱动，用来解析网页
driver = webdriver.Chrome(options=chrome_options)


# 获取url页面信息，构造prompt内容
@app.route('/page', methods=['POST', 'GET'])
def page():
    url = 'https://item.jd.com/6039832.html'
    aa_content = ''

    try:
        data = request.json
        url = data['url']
    except Exception as e:
        pass

    try:
        # 打开网页
        driver.get(url)

        # 等待页面加载完成
        time.sleep(3)

        # 点击【商品问答】按钮：
        btn = driver.find_element(by=By.CSS_SELECTOR, value='#detail > div.tab-main.large > ul > li:nth-child(6)')
        btn.click()
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # time.sleep(3)

        # 获取【问答】信息：
        aa_list = driver.find_element(by=By.CSS_SELECTOR, value='#askAnswer .askAnswer-list')
        aa_items = aa_list.find_elements(by=By.CSS_SELECTOR, value='.askAnswer-item')
        for aa in aa_items:
            ask = aa.find_element(by=By.CSS_SELECTOR, value='.ask .item-con p').text
            answer = aa.find_element(by=By.CSS_SELECTOR, value='.answer .item-con .answer-list li p').text
            aa_content = aa_content + '问：' + ask + '答：' + answer + '\n'
    finally:
        pass
        # if driver:
        #     driver.close()
        #     driver.quit()

    prompt = f"{aa_content}以上是商品买家对该商品的问答内容，根据这些问答内容，总结这个商品的优点和缺点，告诉我这个商品值不值得买。\n"
    return jsonify({'result': prompt})


# 启动服务
if __name__ == '__main__':
    app.run(debug=True)
