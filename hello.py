# variables to use in f string so they can change later  
name ="Josh"
hobby ="3d modeling"
birthYear = 2008
currentYear = 2026
#this subtracts your birth year from the current year to create the new age variable
age = currentYear - birthYear 


# this adds contexts and adds the two variables together
print("Hello I am"+" "+name+" "+"and I am interested in"+" "+hobby)

#this puts the name and age into readable text
print (f"{name} is {age} years old")
