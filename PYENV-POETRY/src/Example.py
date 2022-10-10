# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return

#         return func(a, b)
#     return inner


# @smart_divide
# def divide(a, b):
#     print(a/b)

# divide(2,5)

def make_pretty(func):
    def print_something():
        func()
        return 
    return print_something
    
@make_pretty
def main_function():
    print ("second")
    print ("seconeqw")

main_function()