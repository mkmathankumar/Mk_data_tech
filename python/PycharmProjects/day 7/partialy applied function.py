#normal function then
def calculate_price(base_price,tax_rate):
    return base_price * (1 +tax_rate)

print(calculate_price(1000,0.18))
print(calculate_price(2700,0.18))


#partially applied function

from functools import partial

def calculate_prices(base_prices,tax_rates):
    return base_prices * (1 + tax_rates)

price_with_gst=partial(calculate_prices,tax_rates=0.18)

print(price_with_gst(1360))
print(price_with_gst(1890))