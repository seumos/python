# Writing a 8-Ball's forture 
import random

def magic_8_ball():
  responses = [
    "Yes - definitely.",
    "It is decidedly so",
    "Without a doubt",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
  ]
  
  return random.choice(responses)

print(magic_8_ball())
