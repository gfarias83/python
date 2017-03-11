
stock = {}

def menu():
	print("Press 1 : To add stock. ")
	print("Press 2 : To check stock. ")
	print("Press 3 : To enter sale. ")
	print("Press 4 : To exit. ")
	return int(input("What would you like to do: "))

run = menu()

while True:
	if run == 1:
		addStock = raw_input('Item to be added: ')
		amount = int(input('Quantity to be added: '))
		stock[addStock] = amount
		run = menu()

	elif run == 2:
		for key, value in stock.items():
			print("{}: {}".format(key, value))
		run = menu()

	elif run == 3:
		item = raw_input('Item sold: ')		
		qSold = int(input('Quantity sold: '))
		if item in stock:
			stock[item] -= qSold
			run = menu()

	elif run == 4:
		break

print("You exited the program.")