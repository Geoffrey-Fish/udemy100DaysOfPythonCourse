#SOLVED
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
a = 0
pos = list(position)
b = int(pos[0]) -1
if pos[1] == "1": #pos1 ist die Reihe
     row1[b] = "X"
elif pos[1] == "2":
      row2 [b] = "X"
else:
      row3[b] = "X"

print(f"{row1}\n{row2}\n{row3}")
