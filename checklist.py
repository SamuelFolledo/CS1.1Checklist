import os #for clearing screen

checklist = list()


def create(item): #create
    checklist.append(item)

def read(index): #read
    print("{}".format(checklist[index]))

def update(index, item): #update
    checklist[index] = item

def destroy(index): #destroy
    checklist.pop(index)    

def list_all_items(): #lists all items
    index = 0
    for list_item in checklist:
        # print(str(index) + list_item)
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index): #marks list completed
    checklist[index] = "✅ " + checklist[index]
    print(checklist[index])

def unmark_completed(index): #marks list completed
    #1st way is using .replace #RECOMMENDED IN THIS EXAMPLE
    # checklist[index] = checklist[index].replace("✅ ", "")

    #2nd way is removing using stringObject[ start : stop : interval]
    #first check if our checklist has "✅ "
    checkmark_index = checklist[index].find("✅ ", 0, 2) #search for the index where our checkmark exist
    start = 0
    stop = 1
    if checkmark_index == -1:
        print("{} is already unselected".format(checklist[index]))
    else: #if checkmark_index is not -1, it means we have the checkmark somewhere in our string
        if len(checklist[index]) > stop: #ensure that char_index we are removing is less than the checklist[index] string #but here we are sure that "✅ " are index 0 through 1 in our checklist
            checklist[index] = str(checklist[index])[0 : start :] + str(checklist[index])[stop + 1 : :] #removes the first 2 characters which are the "✅ "
        print("{} is successfully unselected!".format(checklist[index]))

def select(function_code):
    if (function_code == "A") or (function_code == "a"): #Create item
        input_item = user_input("Enter item to add: ")
        create(input_item)
    
    elif (function_code == "R") or (function_code == "r"): #Read item
        item_index = user_int_input("Enter index number to read: ")
        read(item_index) # remember that item_index must exist or our program will crash

    elif (function_code == "P") or (function_code == "p"): #Print all items
        list_all_items()

    elif (function_code == "S") or (function_code == "s"): #select item by index
        item_index = user_int_input("Enter index number to select: ")
        mark_completed(item_index)

    elif (function_code == "X") or (function_code == "x"): #uncheck item by index
        item_index = user_int_input("Enter index number to uncheck: ")
        unmark_completed(item_index)

    elif (function_code == "D") or (function_code == "d"): #delete item by index
        item_index = user_int_input("Enter index number to delete: ")
        destroy(item_index)

    elif (function_code == "U") or (function_code == "u"): #update item by index
        item_index = user_int_input("Enter index number to update: ") #select which index to replace
        input_item = user_input("Enter item to replace {} with: ".format(checklist[item_index])) #select what to replace it with
        update(item_index, input_item) #with our item_index and input_item, we can now update our checklist

    elif (function_code == "Q") or (function_code == "q"): #to quit
        print("Quitting...")
        return False
        
    else: #catch all
        print("Unknown option. Please input \"A\", \"R\", \"P\", \"S\", \"D\", \"U\", \"X\", or \"Q\" only")

    return True

def user_int_input(prompt): #for INT user input
    user_input = int(input(prompt))
    return user_input

def user_input(prompt): #this method will display a message in the terminal and wait for user input
    user_input = input(prompt) #user_input will equal to what the user inputted
    return user_input


def test():
    create("purple sox")
    create("red cloak")



test()
# user_value = user_input("Please enter a value: ")
# select(user_value)
running = True
while running:
    selection = user_input("Press A to Add to list, R to Read from list, P to display list, S to select from list, D to delete from list, X to uncheck from list, U to update from list, and Q to quit\n")
    running = select(selection)

# print(chr(27) + "[2J") #clears terminal
os.system('cls' if os.name == 'nt' else 'clear')