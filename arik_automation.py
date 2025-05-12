from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
import time
from get_minimum_flight import get_minimum_flight_price_detail
from utils import check_if_value_in_select, is_future

URL = "https://www.arikair.com/"


def arikFlightAutomation(location, destination, depDate):


    if not is_future(depDate):
        return

    chrome_options = Options()
    chrome_options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(URL)

    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='alertModal']")))

    driver.find_element(by=By.XPATH, value="//button[@class='btn btn-danger']").click()

    from_selection = Select(driver.find_element(by=By.XPATH, value="//select[@id='depPort']"))


    if not check_if_value_in_select(from_selection.options, location):
        return

    from_selection.select_by_value(location)

    time.sleep(5)
    dest_selection = Select(driver.find_element(by=By.XPATH, value="//select[@id='arrPort']"))
    
    if not check_if_value_in_select(dest_selection.options, destination):
        return
    
    dest_selection.select_by_value(destination)

    flight_date = driver.find_element(by=By.XPATH, value="//input[@id='departureDate']")
    flight_date.clear()
    flight_date.send_keys(depDate)

    driver.find_element(by=By.XPATH, value="//button[@id='search']").click()

    time.sleep(5)
    result_containers = driver.find_elements(by=By.XPATH, value="//div[@class='js-journey']")


    flight_details = []

    for result in result_containers:
        price = result.find_element(by=By.XPATH, value=".//div[@class='desktop-fare-block']").find_element(by=By.XPATH, value=".//div[@class='price-block cabin-name-ECONOMY']").text

        dep_time, arr_time = result.find_element(by=By.XPATH, value=".//div[@class='desktop-route-block col-12 col-lg-7 col-xl-7']").find_elements(by=By.XPATH, value=".//div[@class='time-block']")

        final_res = {
            "dep_time": dep_time.text,
            "arr_time": arr_time.text,
            "price": float(price.replace("₦ ", "").replace(",", ""))
        }

        flight_details.append(final_res)

    driver.quit()


    return {"flight": "arik", "details": get_minimum_flight_price_detail(flight_details)} 



# print(arikFlightAutomation('ABV', 'LOS', "23/03/2026"))