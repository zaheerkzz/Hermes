# selenium imports
from selenium import webdriver
import jsons
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions

# BS4 import
from bs4 import BeautifulSoup as Soup
import time

# selenium setings
class Arguments:
    DRIVER_PATH = 'driver/chromedriver'

    options = ChromeOptions()
    # headless is set TRUE, it will stop browser from opening
    # selenium settings
    options.headless = False 
    options.add_argument('--no-sandbox')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36')
    options.add_argument("--window-size=1920,1200")
    options.add_argument('--lang=en_US')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--enable-features=NetworkService,NetworkServiceInProcess')
    options.add_argument('--force-color-profile=srgb')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")

class HermesModel:
    def __init__(self, title: str, price: str, url: str, image_url: str):
        self.price = price
        self.title = title
        self.url = url
        self.image_url = image_url

class Hermes:
    domain = 'https://www.hermes.com'

    # change your category URL here...
    categoryURL = f"https://www.hermes.com/hk/en/category/women/shoes/"

    def __init__(self):
        arguments = Arguments()
        self.driver = webdriver.Chrome(options=arguments.options, executable_path=arguments.DRIVER_PATH)

    def click_button(self):
        try:
            self.driver.find_element("xpath", "//button[.='Load more items']").click()
            time.sleep(10)
            self.click_button()
        except:
            print('no more load more button')
            self.parseHtml()


    def loadPage(self):
        try:
            print(self.categoryURL)
            self.driver.get(self.categoryURL)
            time.sleep(10)

            # click load more button
            self.click_button()
        except Exception as ex:
            print(f"Hermes ex: {ex}")

    def parseHtml(self):
        detailList = []
        time.sleep(5)
        pageSoup = Soup(self.driver.page_source, "html.parser")
        self.driver.quit()
        
        products = pageSoup.find('div', class_='grid-result').find('h-grid-results')
        for product in products.findAll('div', class_='product-grid-list-item'):
            url = self.domain + product.a['href'].strip()
            title = product.h4.text.strip()
            price = product.find('h-price').text.strip()
            try:
                image_url = 'https:' + product.a.picture.source['data-srcset'].strip()
            except:
                image_url = 'https:' + product.a.picture.source['srcset'].strip()

            hermesModel = HermesModel(
                title=title,
                price=price,
                url=url,
                image_url=image_url
            )

            detailList.append(jsons.dump(hermesModel))
        data_ = jsons.dumps(detailList)

        # print JSON data into terminal
        print(data_)



if __name__ == "__main__":
    m = Hermes()
    m.loadPage()
