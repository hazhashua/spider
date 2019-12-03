import re
from spider.config import config
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

price_xpath = '//*[@id="J_ItemList"]/div[%d]/div/p[1]/em'
context_xpath = '//*[@id="J_ItemList"]/div[%d]/div/p[2]/a'
sales_xpath = '//*[@id="J_ItemList"]/div[%d]/div/p[3]/span[1]/em'
driver_path = config.get("driver_path")

def deal_data(we: selenium.webdriver.remote.webelement.WebElement):
    stocks = we.text.split("\n")
    stock_names, stock_codes = [], []
    cmp = re.compile("^([^(]+)\((.*)\)$")
    for stock in stocks:
        match_r = cmp.match(stock)
        stock_names.append(match_r.groups()[0])
        stock_codes.append(match_r.groups()[1])
    return stock_codes, stock_names

class Base:
    """抓取基础数据"""
    instance = None
    def __init__(self, *args, **kwargs):
        pass

    def single(self, *args, **kwargs):
        if not Base.instance:
            Base.instance = Base(*args, **kwargs)
        return Base.instance

    def check(self, url):
        """校验是否是网页url"""
        import pdb; pdb.set_trace()
        pattern_str = "http[s]{,1}://[^.]+.[^.]+.*"
        cmp = re.compile(pattern_str)
        match_rs = cmp.match(url)
        if match_rs:
            return True
        else:
            return False

    def crawl(self, url: str):
        """通过selemium抓取stock基础数据"""
        codes, names = [], []
        # driver = webdriver.Chrome(executable_path="C:\spider\chromedriver\chromedriver.exe")
        driver = webdriver.Chrome(driver_path)
        driver.get(url)
        # rs  = driver.get(url)

        sh = driver.find_element_by_xpath(xpath=config.get("stock_info").get("sh"))
        driver.close()
        # //*[@id="quotesearch"]/ul[1], //*[@id="quotesearch"]/ul[1]/li[1]
        # print("..........", sh.text, "..............")
        sh_codes, sh_names = deal_data(sh)
        if len(sh_codes)==len(sh_names)
            codes.extend(sh_codes)
            names.extend(sh_names)

        sz = driver.find_element_by_xpath(xpath=config.get("stock_info").get("sz"))
        # print("..........", sz.text, "...............")
        sz_codes, sz_names = deal_data(sz)
        if len(sz_codes) == len(sz_names):
            codes.extend(sz_codes)
            names.extend(sz_names)

        return codes, names

        """
        context = driver.find_element_by_xpath(xpath=context_xpath )
        value = context.get_property("href")
        # print(context.text)
        name_list.append(context.text)
        value = value.replace("file://", "https://")
        # print(value)
        href_list.append(value)

        sales = driver.find_element_by_xpath(xpath=sales_xpath )
        sales = sales.text.replace('笔', '')
        # print(sales)
        """







if __name__=="__main__":
    bs = Base()
    # print(bs.check("http://www.baidu.com"))
    # bs.crawl("http://www.baidu.com")
    stock_url = config.get("stock_info").get("url")
    print(stock_url)
    bs.crawl(stock_url)
