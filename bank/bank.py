from cs50 import get_string

greeting = get_string("Greeting:")
greeting = greeting.lower()
x = "hello"
if x in greeting:
    print('$0',end = "")
if x not in greeting:
    x = list(x)
    greeting = list(greeting)
    if x[0] == greeting[0]:
        print('$20', end = "")
    else:
        print('$100',end = "")
