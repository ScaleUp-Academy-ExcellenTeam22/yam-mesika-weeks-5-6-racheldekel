
def get_recipe_price(prices=dict, optionals=list(), **quantity):
    """
    function that calculate the price for all the integers
    :param prices:
    :param optionals:
    :param quantity:
    :return:
    """
    return sum(quantity[key] / 100 * prices[key]
               for key in prices.keys() if key not in optionals)


if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))