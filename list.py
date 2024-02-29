from icecream import ic

fruits = ['apple','banana','watermelon', 1 ,2,3,True]

numbers =[1,4,56,77,32]

newlist = fruits + numbers

print(newlist)
if 'apple' in fruits:
    print('apple is included in fruits')
else:
    print('Does not include')

realfruits =newlist[5-2]
ic(realfruits)
