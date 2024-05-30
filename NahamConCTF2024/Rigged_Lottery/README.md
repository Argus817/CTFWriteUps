# Rigged Lottery? - Cryptography

## Hint
I found out that somebody has been able to guarantee to win a prize everytime in this lottery. I can't figure it out how they were able to do that. Can you?<br>`nc <hostname> <port>`
#### Attachments: [`server.py`](./server.py)

## Solution
We are given a [`server.py`](./server.py) file which includes code running on the remote host. Its contents are as follows... <br>
```python3
#!/bin/python3
from inputimeout import inputimeout, TimeoutOccurred
import random, sys

with open('flag.txt') as f:
	flag = f.read()

def main():
	print("Here is how the lottery works:")
	print("- Players purchase tickets comprising their choices of six different numbers between 1 and 70")
	print("- During the draw, six balls are randomly selected without replacement from a set numbered from 1 to 70")
	print("- A prize is awarded to any player who matches at least two of the six drawn numbers.")
	print("- More matches = higher prize!")
	while True:
		print("\n********************\nHow many tickets would you like to buy? There is a limit of 50 tickets per person")
		try:
			reply = int(inputimeout(prompt='>> ', timeout=60))
		except ValueError:
			reply = 0
		except TimeoutOccurred:
			print("Oof! Not fast enough!\n")
			sys.exit()
		if reply > 50 or reply < 1:
			print("That is an invalid choice!\n")
		else:
			break
	tickets = []
	for x in range(reply):
		ticket = []
		print(f"\n********************\nPlease give the numbers for ticket {x+1}:")
		for _ in range(6):
			while True:
				try:
					number = int(inputimeout(prompt='>> ', timeout=60))
				except TimeoutOccurred:
					print("Oof! Not fast enough!\n")
					sys.exit()
				except ValueError:
					number = 0
				if number > 70 or number < 1:
					print("That is an invalid choice!\n")
				else:
					break
			ticket.append(number)
		tickets.append(ticket)
	winnings = [0, 0, 1, 100, 1000, 100000, 10000000]
	print(f"\n********************\nLet's see if you can win in {10**6} consecutive rounds of the lottery and make a profit at the end of it!")
	profit = 0
	for i in range(10**6):
		draw = set([])
		while len(draw) != 6:
			draw.add(random.randint(1,70))
		won_prize = Falsewinnings
		for ticket in tickets:
			profit -= 1
			matches = len(draw.intersection(set(ticket)))
			if matches > 1:
				won_prize = True
			profit += winnings[matches]
		if won_prize:
			if (i+1)%(10**5) == 0:
				print(f"You made it through {i+1} rounds! Profit so far is ${profit}")
		else:
			print(f"Draw {i+i}: {draw}, profit: ${profit}")
			print(f"\n********************\nAh shucks! Look's like you did not win any prizes this round. Better luck next time")
			sys.exit()
	if profit > 0:
		print(f"\n********************\nWow! You broke the lottery system! Here's the well-deserved flag --> {flag}")

if __name__ == "__main__":
	main()
```
The server seems to be running a lottery system which allows the player to obtain lottery tickets each containing 6 numbers between 1 and 70 inclusive. The player can buy a maximum of 50 tickets. In each round, 6 numbers between 1 and 70 inclusive are randomly generated using the random function. The player wins the round and generates some profit if and only if 2 or more numbers match from a particular ticket with the randomly generated numbers. If the player wins 1000000 rounds, the player is awarded the flag.

Perhaps there exists a certain combination of tickets that may satisfy the above conditions. After discussing with teammates and hints from [@conjectureguy](https://ctftime.org/user/174213), I was able to figure it out. A concept called covering designs is used in this challenge. It gives us a certain combination of a total of 35 tickets as given in [`data`](./data). The combination was downloaded from [Covering Repository](http://www.coveringrepository.com/systems.aspx) with $v=70, k=6, t=2, m=6$. Generation of such combination is a computation intensive task. With this combination, the player is able to win all 1000000 rounds of the game and hence win the flag.

Complete solution is given in [`solve.py`](./solve.py).