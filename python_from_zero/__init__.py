name = 'Anzor'
age = 25
family = ['Madin', 'Logic', 'Magic', 'Asdfg']

print(f'type of name: {type(name)}')
print(f'type of age: {type(age)}')
print(f'id of family {id(family)}')

import keyword

kw_list = keyword.kwlist
# print(kw_list)

for kw in kw_list:
    print(kw)
