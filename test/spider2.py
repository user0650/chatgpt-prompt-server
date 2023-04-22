"""
使用pyppeteer实现的爬虫
相比selenium需要安装chrome、chromedriver，pyppeteer自动完成安装工作
"""

import asyncio
from pyppeteer import launch


async def main():
    url = 'https://item.jd.com/6039832.html'
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.screenshot({'path': 'example.png'})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
