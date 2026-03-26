# Addition
print (10 + 5) # 15

# Subtraction
print (10 - 5) # 5

# Multiplication
print (10 * 5) # 50

# Division ( always returns float )
print (10 / 5) # 2.0

# Integer Division ( drops decimal )
print (10 // 3) # 3

# Modulus ( remainder )
print (10 % 3) # 1

# Exponent ( power )
print (2 ** 3) # 8


# Multiplication before addition
result = 2 + 3 * 4
print ( result ) # 14 ( not 20!)

# Parentheses change order
result = (2 + 3) * 4
print ( result ) # 20

# Division before addition
result = 10 / 2 + 3
print ( result ) # 8.0

# Parentheses force addition first
result = 10 / (2 + 3)
print ( result ) # 2.0

# Calculate total price
price = 100
tax_rate = 0.08
tax = price * tax_rate
total = price + tax
print ( " Total : " , total ) # 108.0

# Calculate average
score1 = 85
score2 = 92
score3 = 78
average = ( score1 + score2 + score3 ) / 3
print ( " Average : " , average ) # 85.0