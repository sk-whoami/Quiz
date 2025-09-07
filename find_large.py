def find_largest_num():
  num1 = int(input("1st Number : "))
  num2 = int(input("2nd Number :"))
  num3 = int(input("3rd Number : "))
  if num1 > num2:
    print(" 1st number is the the largest")
  else:
    print(" 3rd number is the the largest")
    
  if num2 > num1 :
    print( "2nd number is the largest")
  else:
    print("3rd number is the largest")
  
  if num3 > num2:
    print("3rd number is the largest ")
  else:
    print("1st number is the largest")
    
    
    
find_largest_num()