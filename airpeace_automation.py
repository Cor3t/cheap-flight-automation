from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
import time
from get_minimum_flight import get_minimum_flight_price_detail

URL = "https://flyairpeace.com/"

def airpeace():
    chrome_options = Options()
    chrome_options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(URL)

    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='bdt-switcher bdt-switcher-item-content two_elementor_element']")))
    driver.find_element(by=By.XPATH, value="//input[@value='ONE_WAY']").click()

    select_departure = Select(driver.find_element(by=By.XPATH, value="//select[@name='depPort']"))



    select_departure.select_by_value('ABV')

    time.sleep(5)

    select_arrival = Select(driver.find_element(by=By.XPATH, value="//select[@name='arrPort']"))

    select_arrival.select_by_value("LOS")


    departureDate = driver.find_element(by=By.XPATH, value="//input[@name='departureDate']")
    departureDate.send_keys("10/03/2025")


    search_button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Search flights')]")
    search_button.click()

    time.sleep(5)
    flight_info_container = driver.find_elements(by=By.XPATH, value="//div[@class='js-journey']")


    flight_details = []

    for flight in flight_info_container:
        price = flight.find_element(by=By.XPATH, value=".//div[@class='price-block currency-left-side']")
        dep_time, arr_time = flight.find_elements(by=By.XPATH, value=".//div[@class='time-block']")[2:]

        result = {
            "dep_time": dep_time.text,
            "arr_time": arr_time.text,
            "price": float(price.text.replace("₦ ", "").replace(",", ""))
        }

        flight_details.append(result)

    driver.quit()
    

    return get_minimum_flight_price_detail(flight_details)

