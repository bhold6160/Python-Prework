shopping_list = ["banana", "orange", "apple"]

prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
}

stock = {
  "banana" : 6,
  "apple" : 0,
  "orange" : 32,
  "pear" : 15
}

for key in prices:
	print key
	print "price: %s" % prices[key]
	print "stock: %s" % stock[key]

for key in prices:
  new_price = prices[key] * stock[key]
  print new_price
  total += new_price

print total

def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
	  	total = total + prices[item]
    stock[item] -= 1
  print total
  return total
