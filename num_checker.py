# Even Numbers: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
# Odd Numbers: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19

def checkNumber():
  num = int(input("Enter your number : "))
  even_num = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20 ]
  odd_num = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ]
  if num in even_num == even_num:
    print("even")
  elif num in odd_num == odd_num:
    print("odd number")
  else:
    print("invalid")
    
checkNumber()