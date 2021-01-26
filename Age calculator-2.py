# Age-Calculator-2
This code will be helpful for age calculator।
#python 3.7.1
print("Hello World ! I am Ankit Khatkar.")
print("About Topic :- Today we'll find your that how old are you.")
print("Are you Ready !!")
A=input("Yes or No ;")
print(A)
if A==str("yes"):
  print("Let's Start !!")
  Age=int(input("What is your Date of Birth ="))
  name=str(input("What is your name = "))
  Total=2021-Age
  print(str(name)+",You are " +str (Total) + " year old.")
  
  print(str(name)+",You are "+str(Total*12)+" mothes old.")
  
  print(str(name)+",You are "+str(Total*12*30)+" days old.")
  
  print(str(name)+",You are "+str(Total*12*30*24)+" hours old.")
  
  print(str(name)+",You are "+str(Total*12*30*24*60)+" minutes old.")
  
  print(str(name)+",You are "+str(Total*12*30*24*60*60)+" seconds old.") 
  print("Please,Give me a 🔯🌟 Star ⭐🌟")
elif A==str("No"):
  print("We'll meet Again !!")
