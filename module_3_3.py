

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [False, 0, 'список']
values_dict = {'a': 1, 'b': 'строка', 'c': True}
values_list_2 = [88.8, 'список2']


print_params()
print_params(a = '33')
print_params(b = 25, c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)