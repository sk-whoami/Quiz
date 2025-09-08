# Write a  function that checks weather a number is divisible by three and five 
# print “fizz buzz “ if divisible by both 
# Print fizz if divisible by three only 
# Print buzz if divisible by 5 only 
# If none works print neither 

def fizzbuzz():
  num1 = int(input("Enter : "))
  if num % 2 == 0 and / 3 and 5 :
    print("fizz buzz")
  else:
    print("Neither")
  if num1 % 3 == 0 :
    print("fizz")
  elif num1  % 5 == 0 :
    print("buzz")
  else:
    print("Neither")
fizzbuzz()