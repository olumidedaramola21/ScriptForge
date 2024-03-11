# A little refresher on dictionary
tel = {'jack': 4098, 'sape': 4139} 
tel['guido'] = 4127
print(tel)

del tel['sape']
tel['irv'] = 4127
print(sorted(tel.keys()))
print('guido' in tel)
print('guido' not in tel)

# The dict() constructor builds directionaries from sequences of key-value pairs
sq = dict([('sape', 4139), ('guido', 4127), ('olumide', 1234)])
print(sq)
dict(sape=4139, guido=4127, olumide=1234)

# Using dict comprehensions to create dictionaries from arbitary key and value expressions.
{x: x**2 for x in (2, 3, 4)}