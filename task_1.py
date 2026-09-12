prices = [120, 350, 80, 500]

def calculate_total(numbers):
    return sum(numbers)

def find_expensive(numbers, limit):
    result = []
    for number in numbers:
        if number > limit:
            result.append(number)
    return result

def apply_discount(numbers, percent):
    result = []
    for price in numbers:
        discounted_price = price * (1 - percent / 100)
        result.append(discounted_price)
    return result

print("Сумма:", calculate_total(prices))
print("Дороже 200:", find_expensive(prices, 200))
print("После скидки 10 процентов:", apply_discount(prices, 10))