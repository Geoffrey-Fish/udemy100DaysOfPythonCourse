rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def rps():
    player_choice = input("Rock, Paper or Scissors?")
    computer_choice = random.randint(3)
    1 = "Scissors"
    2 = "Paper"
    3 = "Rock"
    beats = {"Rock": "Scissors"}, {"Paper" : "Rock"}, {"Scissors" : "Paper}

if __name__ == "__main__":
    x = 0
    while x < 3:
        rps()
        x +=1
