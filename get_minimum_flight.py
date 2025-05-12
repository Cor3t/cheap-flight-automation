def get_minimum_flight_price_detail(details : list[dict]):

    if (len(details) == 0):
        return

    prices = []

    for detail in details:
        if not detail:
            continue
        prices.append(detail["price"])

    minimum_price = min(prices)
    
    for detail in details:
        if minimum_price == detail["price"]:
            return detail