from pprint import pprint

def dict_maker(**kwargs):
    my_dict.update(kwargs)

my_dict = {'first': 'so easy'}
dict_maker(second=2, third='three', fourth=[1, 2, 3])
pprint(my_dict, width=20, sort_dicts=False)