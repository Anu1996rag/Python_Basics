def reverse(num):
    rev = 0 
    flag = False
    if num < 0:
        flag = True
        num = 0 - num
    while num > 0:
        d = num % 10
        rev = rev * 10 + d
        num = num // 10
    if (flag):
        return -rev
    else:
        return rev
        
user_input = input ("Enter your number")
try:
   val = int(user_input)
   print("Reverse number :",reverse(val))
except ValueError:
  try:
    val = float(user_input)
    #print("Reverse number :",reverse(val))
    print("Number is float")
  except ValueError:
      print("No.. input is not a number. It's a string")
        
