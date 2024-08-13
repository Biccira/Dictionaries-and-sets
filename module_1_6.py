my_dict = {'Jons':1997, 'Kevin':1987, 'Jeims':2001}
print(my_dict)
print(my_dict['Kevin'])
my_dict['Ben'] = 2010
print(my_dict)
my_dict.update({'Genrih':2018, 'Den':2003})
print(my_dict)
del my_dict['Genrih']
print(my_dict)
a = my_dict.pop('Jons')
print(my_dict)
print(a)
print(my_dict)


my_set = {1,1,2,2,3,3}
print(my_set)
my_set.update({4, 5})
print(my_set)
my_set.remove(1)
print(my_set)
