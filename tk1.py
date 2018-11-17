a=['1','2','3','4','5','6','7','8','9']

def printboard():
	print(a[0]+'|'+a[1]+'|'+a[2])
	print("----")
	print(a[3]+'|'+a[4]+'|'+a[5])
	print("----")
	print(a[6]+'|'+a[7]+'|'+a[8])

playeroneturn = True

for i in range(9):
	printboard()
	#player 1 plays
	if playeroneturn:
		printboard()
		p=input("player 1,choose your place:")
		if p in a:
			a[int(p)-1]='X'
			playeroneturn= not playeroneturn
		else:
			p=input("player 2,choose your place:")
			if p in a:
				a[int(p)-1] = 'O'
				playeroneturn = not playeroneturn
				#check for winning combination

#check for a tie condition
print("it's a tie!")



1|2|3
----
4|5|6
----
7|8|9
1|2|3
----
4|5|6
----
7|8|9
player 1,choose your place:1
X|2|3
----
4|5|6
----
7|8|9
X|2|3
----
4|5|6
----
7|8|9
X|2|3
----
4|5|6
----
7|8|9
X|2|3
----
4|5|6
----
7|8|9
X|2|3
----
4|5|6
----
7|8|9
X|2|3
----
4|5|6
----
7|8|9
X|2|3
----
4|5|6
----
7|8|9
X|2|3
----
4|5|6
----
7|8|9
it's a tie!
