#Example 1

marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

x = line.find("A")
y = line.find("K", x)
# "replaced" variable will store resultant value
replaced = line[:x] + replacement + line[y + 1:]          # I'm directly passing value of x and y to reduce the LINE OF CODE.
#z1 = line[:30] + replacement + line[32 + 1:]      # By passing value of index we get the same output, un-comment to check the same.

#print x        #by printing x and y we get index of "A" and "K" within the string passed in "Line" variable
#print y + 1    # You can un-comment the print statements to see the results

print replaced
#print z1        #Un-comment "z1" variable before un-commenting this !!

# CODED BY - GAURAV PADAWE
