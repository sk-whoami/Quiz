# Write a  function that checks weather a number is divisible by three and five 
# print “fizz buzz “ if divisible by both 
# Print fizz if divisible by three only 
# Print buzz if divisible by 5 only 
# If none works print neither 

def fizzbuzz():
  num1 = int(input("Enter : "))
  if num1 % 3 and num1 %5 ==0: 
    print("fizzbuzz")
  elif num1 % 3 == 0 : 
    print("fizz")
  elif num1  % 5 == 0 :
    print("buzz")
  else:
    print("Neither")
fizzbuzz()