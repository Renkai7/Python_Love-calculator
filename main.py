# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
nameToLowerCase = name1.lower() + name2.lower()

letterT = nameToLowerCase.count("t")
letterR = nameToLowerCase.count("r")
letterU = nameToLowerCase.count("u")
letterE = nameToLowerCase.count("e")

letterL = nameToLowerCase.count("l")
letterO = nameToLowerCase.count("o")
letterV = nameToLowerCase.count("v")

countForTrue = letterT + letterR + letterU + letterE
countForLove = letterL + letterO + letterV + letterE

loveScore = str(countForTrue) + str(countForLove)

if int(loveScore) < 10 or int(loveScore) > 90:
  print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif int(loveScore) > 40 and int(loveScore) < 50:
  print(f"Your score is {loveScore}, you are alright together.")
else:
  print(f"Your score is {loveScore}.")
