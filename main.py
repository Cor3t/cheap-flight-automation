from airpeace_automation import airpeace
from flyunited_automation import flyunited
from get_minimum_flight import get_minimum_flight_price_detail


result1 = airpeace()
result2 = flyunited()

results = [result1, result2]

cheapest = get_minimum_flight_price_detail(results)

print(cheapest)