# start
#1
prices = {'apple': 12, 'banana': 7, 'cherry': 25}
print(prices)
key = input("Which fruit? ")
try :
    print(prices[key])
except KeyError as key:
    print (key , 'is not in the list')
print ('goodbye')

#2
t = (1, 2, 3)
try:
    t[0] = 99
    print(t)
except TypeError:
    print ('cannot change a tuple: tuple object does not support item assignment')
print (t)
print ('goodbye')

#3
fruits = ["apple", "banana"]
try:
    fruits.remove('orange')
except ValueError:
    print ('orange is not in the list')
print (fruits)



