file_name = input('please enter the file name')
fhand = open(filoe_name)
fcont = fhand.read()
print(fcont,"\n\n")
fcont = fcont.split()
print(fcont, "\n\n")
t = list()
# sort a list from longest to sortest

for word in fcont:
    l=len(word)
    t.append(str(l)+word)
    
print(t)

t.sort(reverse = True)

finalt = list()
for word in t:
    finalt.append(word[1:])
print(finalt)
    
    
