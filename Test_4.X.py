def fun_default(a=2):
    print(f"default_{a}")

def fun_positional(a):
    print(f"positional_{a}")

def fun_keyword(*,a=2):
    print(f"keyword_{a}")

fun_default()
fun_default(3)
fun_default(a=5)

#fun_positional()
fun_positional(3)
fun_positional(a=5)

fun_keyword()
#fun_keyword(3)
fun_keyword(a=5)


# * i **
def count_them_all(*args,**kwargs):
    positional_args_count = len(args)
    keyword_args_count = len(kwargs)
    print(f"I have received {positional_args_count} positional arguments and {keyword_args_count} named arguments.")

count_them_all(1, 2, 3, "A", a=1, b=2)


# Dokumentacja
def customized_hello(first_name, last_name, gender_prefix='Mr'):
    """
        Prints hello, based on arguments passed
        Arguments:
        first_name,
        last_name
        Optional arguments:
        gender_prefix:  Mr/Ms based on sex of person
    """
    print("Hello %s %s %s" % (gender_prefix, first_name, last_name))


# Lambda - just an example
shopping_items = [
    ("ziemniak", 2.5, 0.51),
    ("cebula", 3, 1.60),
    ("ser", 0.8, 15.50)
]

sorted_items = sorted(shopping_items, key=lambda given_tuple: given_tuple[1])
print(sorted_items)

# Daje ten sam wynik co:
# def get_index_1_tuple_element(given_tuple):
#     return given_tuple[1]

# sorted_items = sorted(shopping_items, key=get_index_1_tuple_element)
# print(sorted_items)


if __name__ == "__main__":
    pass
    # here you have a place to write code that will be
    # executed after python <path_to_this_script.py>