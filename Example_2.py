#Example 2

marker = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

x = line.find("E")
y = line.find("Y", x)

# z variable will store resultant value
z = line[:x] + replacement + line[y + 1:]          # I'm directly passing value of x and y to reduce the LINE OF CODE.
#z1 = line[:28] + replacement + line[30 + 1:]       # By passing value of index we get the same output, un-comment to check the same.

#print x        #by printing x and y we get index of "E" and "Y" within the string passed in "Line" variable
#print y + 1    # You can un-comment the print statements to see the results

print z
#print z1       #Un-comment "z1" variable before un-commenting this !!

# CODED BY - GAURAV PADAWE
