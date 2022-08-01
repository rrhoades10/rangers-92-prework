# Write a function that prints "Hello_USERNAME"
def hello_name(user_name):
    print("Hello_" + user_name.upper())

def hello_name(user_name):
    print('hello_' + user_name)


hello_name('James')



hello_name('Ryan')


def hello_name1(user_name):
    """Greets user"""
    print(f"Hello {user_name}!")


hello_name1('Julia')


def hello_name3(user_name):
    print("hello_name" + user_name.title() + "!")


hello_name3('cecilia')


def hello_name(color):
    user_name = input("What is your username?")
    print(f"hello_  {user_name.upper()} your favorite color is {color}" )


hello_name('yellow')

# Print all the odd numbers from 1 to 100
def first_odds():
    """Prints all the odd numbers up to 100"""
    list = []
    x = 0
    while x < 100:
        x += 1
        if x % 2 == 0:
            continue
        else:
            list.append(x)
    for number in list:
        print(number, end=" ")

first_odds()


def first_odds():
    numbers = range(1, 100)
    for number in numbers:
        if number % 2 != 0:
            print(number)


first_odds()


def first_odds():
    odd_number = list(range(1, 100, 2))
    print(odd_number)


def first_odds2():
    print(list(range(1, 100, 2)))   


first_odds2()


# Write a function to return the max number in a list
a_list = range(1, 200)

def max_num_in_list(a_list):
    print(max(a_list))


max_num_in_list(a_list)





def max_num_in_list(a_list):
    print(max(a_list))


max_num_in_list([1, 10, 20, 16, 40, 60])

a_list = [23, 23, 346364, 23, 23434, 6, 788, 66, 4, 3]
def max_number_in_list(a_list):
    i = 0
    stored = 0
    while i < len(a_list):
        x = a_list[i]
        if a_list[i] > stored:
            stored = x
        print(x)
        i += 1
    print("The largest number in the list is " + str(stored))


myList = [54, 23, 78, 11, 102, 55, 54, 53, 54, 54]
max_number_in_list(myList)


def max_num_in_list(a_list):
    """Returns the max number in a list"""
    return max(a_list)


def max_num_in_list(a_list):
    print(max(a_list))


number_list = [1, 3, 4, 9, 19, 12, 2, 3, 4, 5, 16]
max_num_in_list(number_list)

# Write a function to determine if any given year is a leap year
def is_leap_year(a_year):
    if((a_year % 4 == 0) and (a_year % 100 != 0)):
        return True
    elif ((a_year % 400 == 0) and (a_year % 100 == 0)):
        return True
    else:
        return False


print(is_leap_year(1999))

a_year = 2022


def is_leap_year(a_year):
    a_year = 2022
    if (a_year % 400 == 0) or (a_year % 4 == 0 and a_year % 100 != 0):
        print(True)
        print(str(a_year) + " is a leapyear")
    else:
        print(False)
        print(str(a_year) + " is not a leapyear")


is_leap_year(a_year)

# Write a function to check if all numbers in a list are consecutive

def is_consecutive(a_list):
    print(sorted(a_list) == list(range(min(a_list), max(a_list)+1)))
    # new_list = sorted(a_list)
    # print(new_list)
    # min_num = min(a_list)
    # print(min_num)
    # max_num = max(a_list)
    # print(max_num)
    # another_list = list(range(min_num, max_num+1))
    # print(another_list)


is_consecutive([2, 3, 4, 5, 6, 7, 10])




b_list = [2, 3, 4, 5, 6, 7]
is_consecutive(b_list)


def is_consecutive(a_list):
    """checks if numbers in a list are consecutive"""
    while len(a_list[:]) >= 2:        
        if a_list.pop() == a_list[-1] + 1:
            continue
        else:
            return False
    return True

print(is_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16]))


list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_c = [1, 12, 3, 5, 16, 8, 9, 12, 4]


def is_consecutive(a_list):
    for ind, number in enumerate(a_list):
        if ind == 0:
            continue
        else:
            if a_list[ind] == a_list[ind-1] + 1:
                continue
            else:
                print(False)
                return(True)
                break
    print(True)


is_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


def is_consecutive2(a_list):
    for ind, number in enumerate(a_list):
        if ind == 0:
            continue
        else:
            if number == a_list[ind-1] + 1:
                continue
            else:
                print(False)
                return(True)
                break
    print(True)


is_consecutive2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
               12, 13, 14, 15, 16, 17, 18, 19, 20])


is_consecutive(list_c)
is_consecutive(list_a)


def is_consecutive(a_list):
    i = 0
    stored = 0
    while i < len(a_list):
        x = a_list[i]
        if a_list[i] > stored:
            stored = x
        else:
            print("The list is not in order")
            break
        i += 1


myList = [2, 3, 4, 5, 6, 7]
is_consecutive(myList)
