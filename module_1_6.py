
my_dict = {'Andrey': 35,
           'Anastasia': 57,
           'Rodion': 22,
           'Larisa': 33}
print(my_dict)

my_dict['Artem'] = 5
print(my_dict.get('Larisa'))
print(my_dict.get('Artem'))

my_dict.update({'Anna': 21, 'Victor': 31})
print(my_dict)

a = my_dict.pop('Anna')
print(a)
print(my_dict)

my_set = {2,2,3,3,4,4,'good day','ok','ok', 'ok',125.43, True}
print(my_set)
my_set.update([123,124])
print(my_set)

my_set.remove('ok')
print(my_set)
















