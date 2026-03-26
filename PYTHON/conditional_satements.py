age = 20

if age >= 18:
    print ( " You are an adult " )

# How it works :
# 1. Check if condition is True
# 2. If True , run indented code
# 3. If False , skip the indented code

age = 15
if age >= 18:
    print ( " You are an adult " )
else :
    print ( " You are not an adult " )

# How it works :
# 1. Check if condition
# 2. If True , run first block
# 3. If False , run else block
# Only ONE block runs !

age = 16

if age >= 18:
    print ( " You are an adult " )
elif age >= 13:
    print ( " You are a teenager " )
else :
    print ( " You are a child " )

# How it works :
# 1. Check first if condition
# 2. If False , check elif condition
# 3. If all False , run else block
# Only the FIRST True condition runs !