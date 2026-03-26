first_name = " John "
last_name = " Doe "
full_name = first_name + " " + last_name
print ( full_name ) # John Doe

# Build sentences
greeting = " Hello "
name = " Alice "
message = greeting + " , " + name + " ! "
print ( message ) # Hello , Alice !

age = 25
print ( " Age : " + age )
# ERROR ! Can ’t concatenate str and int

# Convert to string
age = 25
print ( " Age : " + str ( age ) ) # Works !

# Convert to integer
score = " 85 "
numeric_score = int ( score )
print ( numeric_score + 10) # 95

# Convert to float
price = " 99.99 "
numeric_price = float ( price )
print ( numeric_price * 2) # 199.98

# Variables
name = " Bob "
age = 30
print (f" My name is { name } and I ’m { age } years old ")

# Expressions inside braces
print (f" Next year I ’ ll be { age + 1} ")
print (f" Half my age is { age / 2} ")

# Multiple calculations
price = 50
quantity = 3
print (f" Total : ${ price * quantity } ")

# Format decimal places
pi = 3.14159
print (f" Pi is approximately { pi :.2 f } ") # 3.14