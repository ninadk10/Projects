from replit import clear
import math
from art import logo

print(logo)
print("Welcome to the secret auction program.")

restart_function=True
all_bids = {"name":[],"bid":[]}

x=0

while restart_function ==True:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: £"))

 
  all_bids["name"].append(name)
  all_bids["bid"].append(bid)
  x += 1
  more_bidders= input("Are there other bidders? Type 'yes' or 'no'. ")
  
  if more_bidders.lower() == "yes":
    clear()
  elif more_bidders.lower() == "no":
    highest_bid= max(all_bids["bid"])
    index1 = all_bids["bid"].index(highest_bid)
    highest_bidder= all_bids["name"][index1]
    #print(all_bids)
    print(f"The winner is {highest_bidder} with a bid of: £{highest_bid}")
    restart_function=False