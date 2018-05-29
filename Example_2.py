marker2 = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

x = line.find("E")
y = line.find("Y", x)

#print x        #by printing x and y we get index at which first occurance of "E" and "Y" is present in the string passed in "Line" variable
#print y + 1    # You can un-comment the print statements to see the results

print line[:x] + replacement + line[y + 1:]
#print line[:28] + replacement + line[30 + 1:]  # By passing value of index we get the same output, un-comment to check the same
