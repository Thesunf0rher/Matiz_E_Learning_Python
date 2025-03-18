car = 'BMW'
print(car.lower() != 'bike') #true
print(car.lower() == 'bmw') #true

age = 19
print(age >= 18) #true
print(age <= 18) #false
print(age > 19) #false
print(age < 19) #false

age = 18
print(age == 19 and age > 18) #false
print(age >= 19 or age == 18) #true

nums = list(range(1, 11))
print(5 in nums) #true
print(19 in nums) #false
