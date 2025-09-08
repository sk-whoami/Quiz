
#function to check if number is even or odd
def checkNumber():
  num = int(input("Enter your number : "))
  if num % 2 == 0:
    print(f'{num} is even and number')
  else:
    print(f'{num} is an odd number ')
    
checkNumber()