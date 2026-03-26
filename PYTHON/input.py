# Get user ’s name
name = input ( " Enter your name : " )
print (f" Hello , { name }! ")

# The input () function :
# 1. Shows a prompt message
# 2. Waits for user to type
# 3. Returns what they typed as a STRING

# Get string ( no conversion needed )
name = input ( " Enter name : " )

# Get integer
age = int ( input ( " Enter age : " ) )

# Get float
price = float ( input ( " Enter price : " ) )

# Get boolean ( requires manual conversion )
response = input ( " Are you a student ? ( yes / no ) : " )
is_student = response . lower () == " yes "