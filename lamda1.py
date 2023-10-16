f= lambda x : x+x+x

a=f(10)
print(a)

full_name = lambda first, last: f'Full name: {(first.title()).replace(" ","")} {last.title()}'
print(full_name('guido hi', 'vanrossum'))