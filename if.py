b = input ('Input the base of the triangle: ')
b = int(b)
h = input('Input the heiht of the base: ')
h = int(h)
A = (h * b)/2
print(f'The area of the triangel is {A}')

if A > 100:
    print('Large Area')
elif A == 100:
    print('Medium Area')
else:
    print('Small Area')


print('Thanks You')
