from airpeace_automation import airpeaceAutomation
from arik_automation import arikFlightAutomation
from get_minimum_flight import get_minimum_flight_price_detail


loc = "ABV"
des = "LOS"
desDate = "23/03/2025"

result2 = arikFlightAutomation(loc, des, desDate)
print(result2)

result1 = airpeaceAutomation(loc, des, desDate)
print(result1)




