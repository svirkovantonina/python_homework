import unittest
from selenium import webdriver

class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search(self):
        self.driver.get("https://www.google.com/")
        self.driver.implicitly_wait(2000)
        assert 'Google' in self.driver.title
        search = self.driver.find_element_by_name("q")
        search.send_keys("selenide")
        search.submit()
        assert "No results found" not in self.driver.page_source
        element = self.driver.find_element_by_xpath('(//h3)[1]/..')
        str = element.get_attribute('href')
        assert 'selenide.org' in str
        print(str + " 1-st search result is correct")

        menu = self.driver.find_element_by_xpath('//*[@id="ow15"]/a')
        menu.click()
        images = self.driver.find_element_by_xpath("//*[text()='Картинки']")
        images.click()
        first_picture = self.driver.find_element_by_xpath("//*[@id='rg_s']/div[1]/a[2]")
        url_f_picture = first_picture.get_property('text')
        assert 'selenide.org' in url_f_picture
        print("First picture is related to Selenide site")

        self.driver.back()
        element_check = self.driver.find_element_by_xpath('(//h3)[1]/..')
        str2 = element_check.get_attribute('href')
        assert str == str2
        print("Received result is equal to the previous one")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


