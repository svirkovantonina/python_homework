import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search(self):
        self.driver.get("https://www.google.com/")
        self.driver.implicitly_wait(2000)
        self.driver.set_script_timeout(5)
        assert 'Google' in self.driver.title
        search = self.find_element("[name=q]")
        search.send_keys("selenide")
        search.submit()
        assert "No results found" not in self.driver.page_source
        element = self.find_element("div.r>a")
        str = element.get_attribute("href")
        assert 'selenide.org' in str
        print(str + " 1-st search result is correct")

        menu = self.find_element("[id=ow15]>a")
        menu.click()
        images = self.find_element("[id=lb]>div>a")
        images.click()
        first_picture = self.find_element("[id=rg_s]>div>a:nth-child(2)")
        url_f_picture = first_picture.get_property('text')
        assert 'selenide.org' in url_f_picture
        print("First picture is related to Selenide site")

        self.driver.back()
        element_check = self.find_element("div.r>a")
        str2 = element_check.get_attribute('href')
        print(str2)
        assert str == str2
        print("Received result is equal to the previous one")

    def tearDown(self):
        self.driver.close()

    def find_element(self, selector):
        element = self.driver.find_element_by_css_selector(selector)
        if element:
            return element
        else:
            raise NoSuchElementException("element was not found by selector:" + selector)


if __name__ == "__main__":
    unittest.main()


