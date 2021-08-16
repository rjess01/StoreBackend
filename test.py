

from data import data





def test_forloop():
    for i in range(10):
        print(i)


def print_title():
    """
    Method to learn for loops in pyhton
    1 - import data
    2 - for loop for data list
    3 - print the object
    """

    for item in data:
        print(item["title"])


def print_sum():
    """
    Method to print the sum of catalog prices
    """
    sum = 0
    for item in data:
        sum += item["price"]
    
    print(f"The sum is: {sum}")


def print_test2(limit):
    """
    Method to print the title whos price is greater than 10
    """
    for item in data:
        if item["price"] > limit:
            print(f"{item['title']} - ${item['price']}")

def print_total_value():
    """
    Method to print the total stock
    """
    sum = 0
    for item in data:
        sum += (item["price"] * item["stock"])

    print(f"Total Stock Value = {sum}")

def print_categories_list():
    """
    Method to get and print the list of unique categories
    a - creat a result list
    1 - travle the list
    2 -  get the category
    3 - if the category is not in a result list, push it
    """
    categories = []
    for item in data:
        cat = item["category"]

        if cat not in categories:
            categories.append(cat)
    
    print(categories) # print the list


def run_test():
    print("Running tests")

    #test_forloop()
    #print_title()
    #print_sum() #should print the sum of all prices in catelog
    #print_test2(10)
    #print_test2(20)

    #print_total_value() # print total stock value sum (price + stock)

    #print_categories_list() # print list with the #unique# categories


run_test()