#exercise 1
result = input("write a string: ")
result_lenght = int(len(result))
#exercise 2
if result_lenght < 10 
   print(“String not long enough”)
elif result_lenght > 10
   print(“String too long”)
elif result_lenght == result 
print(“Perfect string”)
#exercise 3
print(f"first character: {result[0]}")
print(f"last character: {result[-1]}")

#exercise 4
for i in range(1, len(result) + 1):
  print(result[:i])  
