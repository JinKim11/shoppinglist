my_list = []


def prompt():
	print my_list
	choice = raw_input ("What would you like to do? Type 1 to add item, type 2 to remove, type 3 to quit.")
	if choice == "1":
		add_item()
	elif choice == "2":
		remove_item()



def add_item ():
	item = raw_input ("What do you want to add to your shopping list?").lower()
	if check_item(item) ==  False:
		my_list.append(item)
		my_list.sort()
	prompt()

def remove_item():
	rem_item = raw_input ("What item would you like to remove?").lower()
	if check_item(rem_item) == True:
		my_list.remove(rem_item) 
	prompt()


def check_item(item):
	return item in my_list

def main():
	prompt() 
	


if __name__ == '__main__':
	main()