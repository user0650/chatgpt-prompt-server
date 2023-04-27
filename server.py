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
    url = 'https://item.jd.com/100008197356.html'
    content = ''

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

        # 标题
        title = driver.title

        # 价格
        price = driver.find_element(by=By.CSS_SELECTOR, value='body > div:nth-child(10) > div > div.itemInfo-wrap > div.summary.summary-first > div > div.summary-price.J-summary-price > div.dd > span.p-price').text

        # 介绍
        detail = driver.find_element(by=By.CSS_SELECTOR, value='#detail > div.tab-con > div:nth-child(1) > div.p-parameter').text

        # 规格与包装
        specification = driver.find_element(by=By.CSS_SELECTOR, value='#detail > div.tab-con > div:nth-child(2) > div.Ptable').text

        # # 评价：点击【商品评价】按钮，等待内容加载完成，提取文字信息
        # comment_btn = driver.find_element(by=By.CSS_SELECTOR, value='#detail > div.tab-main.large > ul > li:nth-child(5)')
        # comment_btn.click()
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # time.sleep(3)
        # comment_list = driver.find_elements(by=By.CSS_SELECTOR, value='#comment-0 > div > div.comment-column.J-comment-column > p')
        # comment_context = ''
        # for comment in comment_list:
        #     comment_context = comment_context + comment.text + '\n'

        # 点击【商品问答】按钮：
        btn = driver.find_element(by=By.CSS_SELECTOR, value='#detail > div.tab-main.large > ul > li:nth-child(6)')
        btn.click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)

        # 获取【问答】信息：
        aa_list = driver.find_elements(by=By.CSS_SELECTOR, value='#askAnswer > div.mc > div.askAnswer-list > div.askAnswer-item')
        aa_content = ''
        for aa in aa_list:
            ask = aa.find_element(by=By.CSS_SELECTOR, value='.ask .item-con p').text
            answer = aa.find_element(by=By.CSS_SELECTOR, value='.answer .item-con .answer-list li p').text
            aa_content = aa_content + '问：' + ask + '答：' + answer + '\n'
    finally:
        pass
        # if driver:
        #     driver.close()
        #     driver.quit()

    # content = content + f'商品标题：\n{title}\n商品价格：${price}\n商品介绍：\n{detail}\n规格与包装：\n{specification}\n商品评价：\n{comment_context}\n买家问答：\n{aa_content}'
    content = content + f'商品标题：\n{title}\n商品价格：${price}\n商品介绍：\n{detail}\n规格与包装：\n{specification}\n买家问答：\n{aa_content}'
    prompt = f"{content}\n以上是商品信息，总结这个商品的优缺点，是否值得购买。"
    return jsonify({'result': prompt})


# 启动服务
if __name__ == '__main__':
    app.run(debug=True)
