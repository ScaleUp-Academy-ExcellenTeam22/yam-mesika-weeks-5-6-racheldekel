#function that calculate the price for all the integers
def get_recipe_price(prices=dict, optionals=list(), **quantity):
    sum_price = 0
    for key in prices.keys():
            if key not in optionals:
                sum_price += (quantity[key] / 100 * prices[key])
    return sum_price


if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))