#SOLVED ,oh what a ride...
'''Calculate the sum with efficient code'''
''' pizza costs 15,20 or 25 $, peperoni 2 for small and 3 for m and l, cheese 1 for any'''

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
s = size
p = add_pepperoni
c = extra_cheese
d = 15

def pizza(s,p,c):
    if s == "S":
        if p == "N" and c == "N":
            return d
        elif p == "Y" and c == "N":
            return d + 2
        elif p == "N" and c == "Y":
            return d + 1
        else :
            return d + 3
    elif s == "M":
        if p == "N" and c == "N":
            return d + 5
        elif p == "Y" and c == "N":
            return d + 8
        elif p == "N" and c == "Y":
            return d + 7
        else :
            return d + 9
    else :
        if p == "N" and c == "N":
            return d + 10
        elif p == "Y" and c == "N":
            return d + 13
        elif p == "N" and c == "Y":
            return d + 12
        else :
            return d + 14

total = pizza(s,p,c) 
print("Your final bill is: $"+ str(total) +".")
