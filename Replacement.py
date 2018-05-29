marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

x = line.find("A")
y = line.find("K", x)

print x
print y + 1

print line[:x] + replacement + line[y + 1:]
