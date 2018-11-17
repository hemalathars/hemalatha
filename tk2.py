

		
	
a=['1','2','3','4','5','6','7','8','9']
def printboard():
	print(a[0]+'|'+a[1]+'|'+a[2])
	print("-----")
	print(a[3]+'|'+a[4]+'|'+a[5])
	print("-----")
	print(a[6]+'|'+a[7]+'|'+a[8])
playeroneturn = True
while True:
				printboard()
				p=input("choose an available space:")

				if(p in a):
								if (a[int(p)-1]=='X' or a[int(p)-1]=='O'):
													print("place taken,choose another place...")
													continue
								else:
													if playeroneturn:
																	print("player 1>>")
																	a[int(p)-1] = 'X'
																	playeroneturn = not playeroneturn
													else:
																	print("player 2 >>")
																	a[int(p)-1] = '0'
																	playeroneturn = not playeroneturn
													for i in(0,3,6):
																	if(a[i]==a[i+1] and a[i]==a[i+2]):
																					print("game over");
																					exit()
													for i in range(3):
																	if(a[i]==a[i+3] and a[i]==a[i+6]):
																					print("game over")
																					exit()
				else:
								print("you have entered an invalid position")
								1|2|3
-----
4|5|6
-----
7|8|9
choose an available space:2
player 1>>
1|X|3
-----
4|5|6
-----
7|8|9
choose an available space:9
player 2 >>
1|X|3
-----
4|5|6
-----
7|8|0
choose an available space:5
player 1>>
1|X|3
-----
4|X|6
-----
7|8|0
choose an available space:4
player 2 >>
1|X|3
-----
0|X|6
-----
7|8|0
choose an available space:6
player 1>>
1|X|3
-----
0|X|X
-----
7|8|0
choose an available space:1
player 2 >>
0|X|3
-----
0|X|X
-----
7|8|0
choose an available space:7
player 1>>
0|X|3
-----
0|X|X
-----
X|8|0
choose an available space:3
player 2 >>
0|X|0
-----
0|X|X
-----
X|8|0
choose an available space:8
player 1>>
game over
