from datetime import datetime

def check_if_value_in_select(items, value):
    new_options = []

    for option in items:
        new_options.append(option.get_attribute("value"))

    return value in new_options

def is_future(date_str):

    date_format = "%d/%m/%Y"
    # Convert the string to a datetime object
    input_date = datetime.strptime(date_str, date_format)
    # Get today's date 
    today = datetime.today()
    # Compare and return result
    return input_date.date() > today.date()
