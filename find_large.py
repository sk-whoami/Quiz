# def find_largest_num():
#   num1 = int(input("1st Number : "))
#   num2 = int(input("2nd Number :"))
#   num3 = int(input("3rd Number : "))
#   largest = max(num1,num2,num3)
#   print(largest)
    
# find_largest_num()                                                       

# OR
def largest_num(num1,num2,num3):
  if (num1>=num2) and (num1>=num3):
    print(num1)
  elif (num2>=num1) and (num1>=num3):
    print(num2)
  else:
    print(num3)
       
largest_num(4,1,8)
     
  