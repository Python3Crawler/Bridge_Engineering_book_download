import os
import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def write_file(picPath, src, name):
    if not os.path.isdir(picPath):
        os.mkdir(picPath)
    try:
        response = requests.get(src)
        with open(picPath + name + '.jpg', 'wb') as f:
            f.write(response.content)
        print('{}{}.jpg is saved'.format(picPath, name))
    except requests.exceptions.ConnectionError:
        print('Sorrry,image cannot downloaded, url is error{}.'.format(src))


def get_src(picPath, url, page_start, page_end):
    driver = webdriver.Chrome()
    for i in range(page_start, page_end):
        new_url = url % i
        driver.get(new_url)
        wait = WebDriverWait(driver, 10)
        source = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.tool-bar > ul.tool-page > li.prebtn > span > i')))
        html = etree.HTML(driver.page_source)
        src = '//*[@id="pg_%s"]/img/@src' % i
        name = '//*[@id="pl_%s"]/@id' % i
        img_src = html.xpath(src)
        img_name = html.xpath(name)
        write_file(picPath, img_src[0], img_name[0])


def main():
    picPath = 'D:\\books_img\\'
    url = 'http://app.readoor.cn/pcv/pcv.php?app=1535595605&turn=rich&b_id=79887&a=a&back\
    =http://app.readoor.cn/app/dt/bi/1535595606/79887-6262205e411bc7?s=1&sign=Nzk4ODcsNzAyN\
    jc3NywxNTgyODA4NzcwLDg5YTNjNWI4ODlkZTIyMmZhY2I2MThlNWQ3NmRjNjM1&page_no=%s'
    page_start = 1
    page_end = 676
    get_src(picPath, url, page_start, page_end)


if __name__ == '__main__':
	main()
