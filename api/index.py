from flask import Flask, jsonify, request
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# 设置浏览器参数
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# 创建Chrome浏览器驱动，用来解析网页
driver = webdriver.Chrome(options=chrome_options)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/about')
def about():
    return 'About'


# 获取url页面信息，构造prompt内容
@app.route('/page', methods=['POST'])
def page():
    data = request.json
    url = data['url']

    # 打开网页
    driver.get(url)
    # 等待页面加载完成
    time.sleep(3)

    # 点击【商品问答】按钮：
    btn = driver.find_element(by=By.CSS_SELECTOR, value='#detail > div.tab-main.large > ul > li:nth-child(6)')
    btn.click()

    # 等待问答信息加载完成：
    time.sleep(2)

    # 获取【问答】信息：
    aa_content = ''
    aa_list = driver.find_element(by=By.CSS_SELECTOR, value='#askAnswer .askAnswer-list')
    aa_items = aa_list.find_elements(by=By.CSS_SELECTOR, value='.askAnswer-item')
    for aa in aa_items:
        ask = aa.find_element(by=By.CSS_SELECTOR, value='.ask .item-con p').text
        answer = aa.find_element(by=By.CSS_SELECTOR, value='.answer .item-con .answer-list li p').text
        aa_content = aa_content + '问：' + ask + '答：' + answer + '\n'

    prompt = f"{aa_content}以上是商品买家对该商品的问答内容，根据这些问答内容，总结这个商品的优点和缺点，告诉我这个商品值不值得买。\n"
    return jsonify({'result': prompt})


# 启动服务
# if __name__ == '__main__':
#     app.run(debug=True)

