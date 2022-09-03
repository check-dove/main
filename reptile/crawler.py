from selenium import webdriver
from file_handle import data_storage

web = 'https://uland.taobao.com/sem/tbsearch'
browser = webdriver.Chrome()


class test_selenium(object):
    def init_browser(self):
        pass

    def page_open(self):
        browser.get(web)

    def page_handle(self):
        info = browser.find_elements_by_css_selector("div#J_u_root> div#mx_3> div#mx_5> ul>li")
        mc = data_storage()
        for i in info:
            data = self.need_info(i)
            mc.file_output(str(data))

    def need_info(self, need_info):
        goods_name = need_info.find_element_by_css_selector("a > div.pc-items-item-title.pc-items-item-title-row2 > span").text
        goods_price = need_info.find_element_by_css_selector("a> div.price-con > span.coupon-price-afterCoupon").text
        store_names = need_info.find_element_by_css_selector('a > div.seller-info > div').text
        sell_info = need_info.find_element_by_css_selector('a > div.item-footer > div.sell-info').text
        store_name = str(store_names)[1:]
        return (goods_name, goods_price, store_name, sell_info)

    def run(self):
        self.page_open()
        self.page_handle()
        browser.close()


if __name__ == '__main__':
    mk = test_selenium()
    mk.run()
