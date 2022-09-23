from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def plan():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.airtel.in/myplan-infinity/")

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "plansSection"))
        )
        
        if element:
            plan = driver.page_source
            soup = BeautifulSoup(plan, 'lxml')
            single_cart = soup.find_all('div', class_ = 'single_cart')
            plan_dict = {}
            plan_benifits_all = []
            for i in range(len(single_cart)):
                cart_index = single_cart[i]

                benifit = cart_index.find_all('div', class_='border-bottom')
                
                plan_benifits = []
                for ben_in in range(len(benifit)):
                    benifit_div = benifit[ben_in]
                    data = benifit_div.find('span').text.strip()
                        
                    plan = cart_index.find(class_='cart_head')
                    price = plan.find('span', class_='price')
                    plan_price = price.text.strip()

                    plan_benifits.append(data)
                plan_benifits.append(plan_price)
                plan_dict[f'{i+1} plan'] = plan_benifits
                plan_benifits_all.append(plan_benifits)

            driver.close()
            return plan_dict
    finally:
        driver.quit()
