#SOLVED
print("Welcome to the Love Calculator!")
name1 = input("Your Name? ")
name2 = input("The other Name? ")
name3 = name1 + name2
name4 = name3.lower()
tru = ["t","r","u","e"]
lov = ["l","o","v","e"]
tc = 0 #true counter
lc = 0 #love counter
for x in range(0,4):
    tc += name4.count(tru[x])
    lc += name4.count(lov[x])
tclc = str(tc) + str(lc)#glue that shit together
tl = int(tclc)#convert to integer
if tl < 10 or tl > 90 :
    men = "Your score is {}, you go together like coke and mentos."
    print(men.format(tl))
elif tl >= 40 and tl <= 50 :
    alr = "Your score is {}, you are alright together."
    print(alr.format(tl))
else :
    ist = "Your score is {}." 
    print(ist.format(tl))

