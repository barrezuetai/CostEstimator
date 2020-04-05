"""
This module consists of the functions needed
in order to find a hospital's pcr
"""
from django.contrib.staticfiles.storage import staticfiles_storage


def get_pcr(hospital_finances: {}) -> int:
    """ Calculates and returns the pcr given proper parameters """
    pcr = int(hospital_finances['net_revenue']) / int(hospital_finances['gross_revenue'])  # noqa: E501
    return float(pcr)


def get_prices() -> {}:
    """ Gets data from the csv file and prepares it into a dictionary"""
    price_template = open(staticfiles_storage.path('estimator/data.csv'))
    rows = []
    price_split = {}
    for line in price_template:
        line = line.replace("\n", "")
        rows.append(line)
    for row in rows:
        temp = row.split("* ")
        price_split[temp[0]] = temp[1]
    return price_split


def generate_prices(pcr: int) -> {}:
    """ Generates prices for hospital procedures given a pcr"""
    procedure_prices = get_prices()
    for procedure, price in procedure_prices.items():
        procedure_prices[procedure] = pcr * int(price)
    return procedure_prices
