def get_minimum_flight_price_detail(details : list[dict]):
    prices = []

    for detail in details:
        prices.append(detail["price"])

    minimum_price = min(prices)
    
    for detail in details:
        if minimum_price == detail["price"]:
            return detail