from airpeace_automation import airpeaceAutomation
from arik_automation import arikFlightAutomation
from get_minimum_flight import get_minimum_flight_price_detail


loc = "ABV"
des = "LOS"
desDate = "10/04/2025"

result1 = airpeaceAutomation(loc, des, desDate)
print(result1)

result2 = arikFlightAutomation(loc, des, desDate)
print(result2)



def get_price(arg):

    price = arg.get("details")

    if not price or not arg:
        return 9999999999
    
    return price.get("price")


cheapest = min(
    [result1, result2],
    key = lambda value : get_price(value)
)

print(cheapest)

a = get_price()






