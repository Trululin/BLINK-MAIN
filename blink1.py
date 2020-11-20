from os import system
import time
from json import load, dump

#Tugas, add tambah info, edit, update discography, member, and history

def info() : 
	system("cls")
	print("""

		THIS APP WAS MADE BY LIN FOR SCHOOL PROJECT
		ON 10/10/2020 

		DEDICATED TO BLINK BECAUSE BLINKS ARE TOO LAZY TO VOTE AND A SELF REMINDER

	""")

	input("\n\tPRESS ENTER TO CONTINUE")
	view_menu()

def idolchamp() : 
	system("cls")
	print("""

		WHAT IS IDOLCHAMP ? 
	[1] - IDOLCHAMP IS AN APP USED TO VOTE FOR MUSICSHOWS
	[2] - IT WILL HELP TO GIVE BLACKPINK MORE POINTS IN MUSICSHOWS

		HOW TO VOTE : 
	[1] - SIGN IN TO YOUR ACCOUNT
	[2] - CLICK ON THE VOTE LOGO ON THE BOTTOM OF YOUR SCREEN
	[3] - SEARCH FOR SHOWCHAMPION
	[4] - CLICK VOTE FOR LOVESICK GIRLS
	[6] - YOU ONLY CAN VOTE THREE TIMES ON EACH DEVICE

	""")

	input("\n\tPRESS ENTER TO CONTINUE")
	voting()

def whosfan() : 
	system("cls")
	print("""
		
		WHAT IS WHOSFAN ? 
	[1] - WHOSFAN IS AN APP USED TO VOTE FOR MUSICSHOWS
	[2] - IT WILL HELP TO GIVE BLACKPINK MORE POINTS IN MUSICSHOWS

		HOW TO VOTE : 
	[1] - SIGN IN TO YOUR ACCOUNT
	[2] - CLICK ON THE STAR LOGO ON BOTTOM OF YOUR SCREEN
	[3] - SEARCH FOR MCOUNTDOWN PREVOTING
	[4] - EXCHANGE TICKET TO VOTE
	[5] - CLICK VOTE ON LOVESICK GIRLS
	[6] - YOU ONLY CAN VOTE ONCE WITH EVERY ACCOUNT FOR A WHOLE VOTING PERIOD

	""")

	input("\n\tPRESS ENTER TO CONTINUE")
	voting()

def mwave() : 
	system("cls")
	print("""

		WHAT IS MWAVE ? 
	[1] - MWAVE IS AN APP USED TO VOTE FOR MUSICSHOWS
	[2] - IT WILL HELP TO GIVE BLACKPINK MORE POINTS IN MUSICSHOWS

		HOW TO VOTE :
	[1] - SIGN IN TO YOUR ACCOUNT
	[2] - CLICK THE THREE BARS ON TOP RIGHT
	[3] - CLICK PREVOTING
	[4] - SEARCH FOR LOVESICK GIRLS AND CLICK VOTE
	[5] - ENTER THE CHARACTERS TO VERIFY YOUR ANSWER
	[6] - YOU ONLY CAN VOTE ONCE EVERYDAY FOR EACH ACCOUNT

	""")

	input("\n\tPRESS ENTER TO CONTINUE")
	voting()

def aaa() : 
	system("cls")
	print("""

		WHAT IS CHOEAEDOL ? 
	[1] - AN APP THAT IS USED TO VOTE BETWEEN GIRLGROUPS
	[2] - THIS YEAR, SORIBADA AWARD AND AAA USES THIS APP

		HOW TO USE CHOEAEDOL ? 
	[1] - SIGN IN TO CHOEAEDOL USING YOUR ACCOUNT
	[2] - WATCH ADS 10 TIMES EACH HOUR AND COLLECT HEART BOXES EVERY 4 HOURS
	[3] - EVER HEARTS WILL NEVER EXPIRE BUT DAILY HEART WILL EXPIRE 
	[4] - VOTE ON COMMUNITY BANNER NOT ON THE CHARTS 
	[5] - YOU WILL RECEIVE 10% REBATES WHEN YOU VOTE FOR COMMUNITY BANNER

	""")

	input("\n\tPRESS ENTER TO CONTINUE")
	voting()

def mubeat() : 
	system("cls")
	print("""

		WHAT IS MUBEAT?
	[1] - MUBEAT IS AN APP USED TO VOTE FOR MUSICSHOWS
	[2] - IT WILL HELP TO GIVE BLACKPINK MORE POINTS IN MUSICSHOWS

		HOW TO VOTE : 
	[1] - SIGN IN TO YOUR ACCOUNT COULD BE GOOGLE, TWITTER, FACEBOOK, ETC
	[2] - CLICK THE STORE ON TOP RIGHT
	[3] - WATCH ADS FOR 3 BEATS
	[4] - COLLECT BEATS AND USE IT TO VOTE FOR BLACKPINK 
	[5] - 3 BEATS ARE USED FOR 1 VOTE

	""")

	input("\n\tPRESS ENTER TO CONTINUE")
	voting()

def mtv() : 
	system("cls")
	print("""

		MTV EMA NOMINATION
	[1] - BLACKPINK FOR BEST GROUP
	[2] - ICE CREAM FOR BEST COLLABORATION

		HOW TO VOTE : 
	[1] - OPEN THE MTVEMA WEBSITE 
	[2] - SEARCH FOR BEST GROUP AND BEST COLLABORATION CATEGORIES
	[3] - VOTE FOR BLACKPINK AND ICE CREAM
	[4] - UNLIMITED VOTING 

	""")

	input("\n\tPRESS ENTER TO CONTINUE")
	voting()

def pca() : 
	system("cls")
	print("""

		PCAs AWARD NOMINATION
	[1] - BLACKPINK FOR THE GROUP
	[2] - ICE CREAM FOR THE MUSIC VIDEO

		HOW TO VOTE : 
	[1] FROM TWITTER : 
		[A] MAKE YOUR OWN TWEET, IT MUST INCLUDE #BLACKPINK #TheGroup #PCAs @BLACKPINK
		[B] MAKE YOUR OWN TWEET, IT MUST INCLUDE #IceCream #TheMusicVideo #PCAs @BLACKPINK @SelenaGomez

	[2] FROM WEBSITE : 
		[A] OPEN PCAs WEBSITE AND SEARCH FOR THE GROUP AND THE MUSIC VIDEO CATEGORIES
		[B] YOU CAN VOTE 25 TIMES EACH EMAIL EVERY DAY

	""")

	input("\n\tPRESS ENTER TO CONTINUE")
	voting()

def breaktudo() : 
	system("cls")
	print("""

		BREAKTUDO AWARD NOMINATION
	[1] - FEMALE KPOP GROUP
	[2] - INTERNATIONAL GROUP
	[3] - INTERNATIONAL MUSIC VIDEO
	[4] - COLLAB OF THE YEAR
	[5] - INTERNATIONAL FANDOM


		HOW TO VOTE : 
	[1] - OPEN THE PROVIDED LINK OF EACH CATEGORIES
	[2] - CLICK VOTAR (VOTE) UNDER BLACKPINK'S NAME
	[3] - VERIFY THAT YOU'RE NOT A BOT BY DOING THE RECAPTCHA
	[4] - VOTE
	[5] - IT'S UNLIMITED VOTINGS

	""")

	input("\n\tPRESS ENTER TO CONTINUE")
	voting()

def voting() : 
	system("cls")
	menu = """

	THESE ARE THE CURRENT VOTING FOR BLACKPINK
	INCLUDING WITH THE VOTING TUTORIAL

	[A] - PCAs 
	[B] - MTV EMA
	[C] - MUBEAT
	[C] - AAA ON CHOEAEDOL
	[E] - MWAVE
	[F] - WHOSFAN
	[G] - IDOLCHAMP

	[Q] - BACK
	"""
	print(menu)

	user = input("Input Here : ")
	user = user.upper()

	if user == "A" : 
		pca()
	elif user == "B" : 
		mtv()
	elif user == "C" : 
		mubeat()
	elif user == "D" : 
		aaa()
	elif user == "E" : 
		mwave()
	elif user == "F" : 
		whosfan()
	elif user == "G" : 
		idolchamp()
	elif user == "Q" : 
		view_menu()
	else : 
		system("cls")
		print("Error 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		voting()

def pinks(member_name) : 
	system("cls")
	member_name = str(member_name)
	name = pinks_profile[member_name]
	msg = pinks_profile[member_name]["Msg"]
	print(msg)

	input("\tPRESS ENTER TO CONTINUE")
	the_pinks()

def update_thepinks(member) : 
	system("cls")
	new = input("INPUT THEIR NEW PROFILE HERE : ")

	resp = input("ARE YOU SURE YOU WANT TO CHANGE THEIR PROFILE ? (Y/N) : ")
	if verify_ans(resp) : 
		system("cls")
		member = str(member)
		pinks_profile[member]["Msg"] = new
		time.sleep(1)
		print("\n\n\tTHE PROFILE HAS BEEN CHANGED")
		input("\tPRESS ENTER TO CONTINUE")
		the_pinks()
	else : 
		system("cls")
		print("Error 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		the_pinks()

def edit_thepinks():
	system("cls")
	menu = """
	WHICH MEMBER PROFILE YOU WANT TO EDIT ? 

	[A] - KIM JISOO
	[B] - JENNIE KIM
	[C] - PARK CHAEYOUNG
	[D] - LALISA MANOBAN

	[Q] - BACK
	"""

	print(menu)

	user = input("Input Here : ")
	user = user.upper()

	if user == "A" : 
		update_thepinks(2)
	elif user == "B" : 
		update_thepinks(3)
	elif user == "C" : 
		update_thepinks(4)
	elif user == "D" : 
		update_thepinks(5)
	elif user == "Q" : 
		view_menu()
	else : 
		system("cls")
		print("Error 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		the_pinks()

	print()

def the_pinks() : 
	system("cls")
	menu = """
	THIS IS BLACKPINK

	[A] - KIM JISOO
	[B] - JENNIE KIM
	[C] - PARK CHAEYOUNG
	[D] - LALISA MANOBAN

	[1] - EDIT THEIR PROFILE
	[Q] - BACK
	"""
	print(menu)

	user = input("Input Here : ")
	user = user.upper()

	if user == "A" : 
		pinks(2)
	elif user == "B" : 
		pinks(3)
	elif user == "C" : 
		pinks(4)
	elif user == "D" : 
		pinks(5)
	elif user == "Q" : 
		view_menu()
	elif user == "1" : 
		edit_thepinks()
	else : 
		system("cls")
		print("Error 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		the_pinks()

def verify_ans(char) : 
	char = char.upper()
	if char == "Y" : 
		return True
	else : 
		return False

def blackpink() : 
	system("cls")
	menu = """
	THIS IS BLACKPINK

	[A] - BLACKPINK

	[1] - EDIT THEIR PROFILE
	[Q] - BACK
	"""
	print(menu)

	user = input("Input Here : ")
	user = user.upper()

	if user == "A" : 
		system("cls")
		msg = pinks_profile["1"]["Msg"]
		print(msg)

		input("\tPRESS ENTER TO CONTINUE")
		blackpink()

	elif user == "Q" : 
		view_menu()

	elif user == "1" : 
		system("cls")
		new = input("INPUT THEIR NEW PROFILE HERE : ")

		resp = input("ARE YOU SURE YOU WANT TO CHANGE THEIR PROFILE ? (Y/N) : ")
		if verify_ans(resp) : 
			system("cls")
			pinks_profile["1"]["Msg"] = new
			time.sleep(1)
			print("\n\n\tTHE PROFILE HAS BEEN CHANGED")
			input("\tPRESS ENTER TO CONTINUE")
			blackpink()
		else : 
			system("cls")
			print("Error 304")
			input("\n\n\tPRESS ENTER TO CONTINUE")
			blackpink()
	else : 
		system("cls")
		print("Error 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		blackpink()

#THIS FINALLY WORKS OMG TO CHANGE THE TRACKS
def songs(hola, code, date) : 
	system("cls")
	A = 0
	numb = 1
	numd = str(numb)
	
	amount = len(list_of_songs[date][code]["TRACKS"])

	while amount > A :  
		print(f"\t OLD TRACKS \t : {list_of_songs[date][code]['TRACKS'][numd]}")
		
		A = A + 1
		numb = numb + 1
		numd = str(numb)

	print()
	new_amounts = input("NEW AMOUNT OF SONGS : ")
	
	amounts = int(new_amounts)
	x = []
	for songs in range(amounts) : 
		songs = input("WHAT IS THE SONG TITLE ? ")
		songs = songs.upper()
		x.append(songs)

	kk = len(list_of_songs[date])
	kks = int(kk) 
	kkz = str(kks)

	jumlah = len(x)

	code = "BP" + kkz
	ans = input("ARE YOU SURE YOU WANT TO ADD THE DISCOGRAPHY ? (Y/N) : ")

	if verify_ans(ans) :
		numb = 1
		nums = 0

		for songs in range(jumlah) : 
			numd = str(numb)

			new_song = x[nums]

			list_of_songs[date][code]['TRACKS'][numd] = new_song

			numb += 1
			nums += 1

		time.sleep(1)
		system("cls")
		print("THE TRACKS HAS BEEN CHANGED")
		input("PRESS ENTER TO CONTINUE")

	else : 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")

#change album title
def elbeom(hola, code, date) : 
	system("cls")
	print(f"OLD ALBUM NAME \t : {list_of_songs[date][code]['ALBUM']}")
	new_album = input("NEW ALBUM NAME \t : ")
	new_album = new_album.upper()
	resp = input("ARE YOU SURE YOU WANT TO CHANGE THE ALBUM NAME ? (Y/N) : ")
	if verify_ans(resp) : 
		system("cls")
		list_of_songs[date][code]["ALBUM"] = new_album
		time.sleep(1)
		print("\n\n\tTHE ALBUM NAME HAS BEEN CHANGED")
		input("\tPRESS ENTER TO CONTINUE")
	else : 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		discography()

#change date
def dateudateu(hola, code, date) : 
	system("cls")
	print(f"OLD DATE \t : {list_of_songs[date][code]['DATE']}")
	new_date = input("NEW DATE \t : ")
	new_date = new_date.upper()
	resp = input("ARE YOU SURE YOU WANT TO CHANGE THE DATE ? (Y/N) : ")
	if verify_ans(resp) : 
		system("cls")
		list_of_songs[date][code]["DATE"] = new_date
		time.sleep(1)
		print("\n\n\tDATE HAS BEEN CHANGED")
		input("\tPRESS ENTER TO CONTINUE")
	else : 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		discography() 

#check which part of discography want to be updated
def checky(answer, code, year) : 
	#if answer == "1" :
	#	change_year(answer, code, year)
	if answer == "1" :
		dateudateu(answer, code, year)
	elif answer =="2" : 
		elbeom(answer, code, year)
	elif answer == "3" : 
		songs(answer, code, year)
	else :
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
	
	discography() 

#print all song in album
def printeu(num, hahaha, years) : 
	system("cls")
	year = str(years)
	date = list_of_songs[year][hahaha]["DATE"]
	album = list_of_songs[year][hahaha]["ALBUM"]
	amount = len(list_of_songs[year][hahaha]["TRACKS"])

	print(f"\t YEAR \t\t : {year}")
	print(f"\t RELEASE DATE \t : {date}")
	print(f"\t ALBUM \t\t : {album}")
	print()

	if amount > 1 : 
		print(f"\t AMOUNT OF SONG  : {amount} SONGS")
	else : 
		print(f"\t AMOUNT OF SONG  : {amount} SONG")

	A = 0
	numb = 1
	numd = str(numb)

	while amount > A :  
		print(f"\t TRACKS \t : {list_of_songs[year][hahaha]['TRACKS'][numd]}")
		
		A = A + 1
		numb = numb + 1
		numd = str(numb)

#menu for update discography
def menuuu():
	menu = """

		WHAT DO YOU WANT TO UPDATE?
		[1] - RELEASE DATE
		[2] - ALBUM NAME
		[3] - TRACKS


	"""

	print(menu)

#input for years and which album want to be updated
def update_disco() : 
	system("cls")
	print("WHICH YEAR OF DISCOGRAPHY YOU WANT TO UPDATE ? ")
	ans = input("Input Here : ")
	
	print()

	if ans in list_of_songs : 
		answ = int(ans)
		year = str(ans)

		if len(list_of_songs[year]) == 0 : 
			print("\n\n\tError 304")
			input("\n\n\tPRESS ENTER TO CONTINUE")
		else : 
			for every_song in list_of_songs[year] : 
				number = every_song[2]
				numbers = str(number)
				album = list_of_songs[year][every_song]["ALBUM"]

				print(f"\t\t{number} - {album}")

		print()
		print("WHICH ALBUM YOU WANT TO UPDATE ? ")
		human = input("Input Here : ")

		print()

		code = "BP" + human
		printeu(human, code, year)

		menuuu()

		answer = input("Input Here : ")
		checky(answer, code, year)

	else : 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		discography()

#add to discography this work omg
def up_2_date(date, album, code, kks, year, tracks) : 
	jumlah = len(tracks)

	years = str(year)

	list_of_songs[years][code] = {
		"DATE" : date, 
		"ALBUM" : album,  
		"TRACKS" : {

			}
		}

	numb = 1
	nums = 0

	for songs in range(jumlah) : 
		numd = str(numb)

		new_song = tracks[nums]

		list_of_songs[years][code]['TRACKS'][numd] = new_song

		numb += 1
		nums += 1

	time.sleep(1)
	system("cls")
	print()
	print("\n\n\tDISCOGRAPHY ADDED")
	input("\tPRESS ENTER TO CONTINUE")
	discography()

#format to add new discography
def format(num, hahaha, years) : 
	system("cls")

	year = str(years)
	date = list_of_songs[year][hahaha]["DATE"]
	album = list_of_songs[year][hahaha]["ALBUM"]
	amount = len(list_of_songs[year][hahaha]["TRACKS"])

	print("\t\t FORMAT EXAMPLE")
	print(f"\t YEAR \t\t : {year}")
	print(f"\t RELEASE DATE \t : {date}")
	print(f"\t ALBUM \t\t : {album}")

	print()

	if amount > 1 : 
		print(f"\t AMOUNT OF SONG  : {amount} SONGS")
	else : 
		print(f"\t AMOUNT OF SONG  : {amount} SONG")

	A = 0
	numn = 1
	numm = str(numn)

	while amount > A :  
		print(f"\t TRACKS \t : {list_of_songs[year][hahaha]['TRACKS'][numm]}")
		
		A = A + 1
		numn = numn + 1
		numm = str(numn)
	

	print()

#deciding the title etc
def add_disco() : 
	system("cls")
	year = input("WHICH YEAR OF DISCOGRAPHY YOU WOULD LIKE TO ADD ? : ")
	years = int(year)

	numb = " "
	code = "BP1"

	format(numb, code, years)

	date = input("WHEN IS THE RELEASE DATE ? : ")
	album = input("WHAT IS THE ALBUM TITLE ? : ")
	amount = input("AMOUNT OF SONGS IN THE ALBUM ? : ")

	amounts = int(amount)
	x = []
	for songs in range(amounts) : 
		songs = input("WHAT IS THE SONG TITLE ? ")
		songs = songs.upper()
		x.append(songs)

	date = date.upper()
	album = album.upper()

	kk = len(list_of_songs[year]) + 1
	kks = int(kk) 
	kkz = str(kks)

	code = "BP" + kkz
	ans = input("ARE YOU SURE YOU WANT TO ADD THE DISCOGRAPHY ? (Y/N) : ")

	if verify_ans(ans) : 
		up_2_date(date, album, code, kks, years, x)

	else : 
		print("\n\n\t\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		discography()

#edit discography
def edit_disco() : 
	system("cls")
	menu = """
		What Would You Like To Edit ?
		[A] - Add A Discography
		[B] - Update Discography

		[Q] - Back
	"""
	print(menu)
	answer = input("Input Here : ")
	answer = answer.upper()

	if answer == "A" :
		add_disco()
	elif answer == "B" : 
		update_disco() 
	elif answer == "Q" : 
		discography()
	else : 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		edit_disco()

#print all songs
def printprint(num, hahaha, years) : 
	system("cls")
	year = str(years)
	date = list_of_songs[year][hahaha]["DATE"]
	album = list_of_songs[year][hahaha]["ALBUM"]
	amount = len(list_of_songs[year][hahaha]["TRACKS"])

	print(f"\t YEAR \t\t : {year}")
	print(f"\t RELEASE DATE \t : {date}")
	print(f"\t ALBUM \t\t : {album}")

	print()

	if amount > 1 : 
		print(f"\t AMOUNT OF SONG  : {amount} SONGS")
	else : 
		print(f"\t AMOUNT OF SONG  : {amount} SONG")

	A = 0
	numn = 1
	numm = str(numn)

	while amount > A :  
		print(f"\t TRACKS \t : {list_of_songs[year][hahaha]['TRACKS'][numm]}")
		
		A = A + 1
		numn = numn + 1
		numm = str(numn)

	input("\n\n\tPRESS ENTER TO CONTINUE")
	discography()

#check album from certain years
def checkcheck(years) : 
	system("cls")
	year = str(years)
	if len(list_of_songs[year]) == 0 : 
		print("\n\n\t\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
	else : 
		print("\t\tWHICH ALBUM YOU WOULD LIKE TO SEE?")
		for every_song in list_of_songs[year] : 
			number = every_song[2]
			numbers = str(number)
			album = list_of_songs[year][every_song]["ALBUM"]

			jumlah = len(list_of_songs[year])

			print(f"\t\t{numbers} - {album}")

	answer = input("Input Here : ")

	answers = str(answer)
	answerd = int(answer)

	if answerd > jumlah: 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		discography()
	else : 
		if answerd > len(list_of_songs[year]) : 
			system("cls")
			print("\tError 304")
			input("\n\n\tPRESS ENTER TO CONTINUE")
			discography()
		else: 
			code = "BP" + answers
			printprint(answers, code, year)

def discography() : 
	system("cls")
	menu = """
	Which Year of BLACKPINK Discography You Would Like To See? 
	[A] - 2016
	[B] - 2017
	[C] - 2018
	[D] - 2019
	[E] - 2020

	[1] - Edit Discography 
	[Q] - Back
	"""
	print(menu)

	user = input("Input Here: ")
	user = user.upper()

	if user == "A" : 
		checkcheck(2016)
	elif user == "B" : 
		checkcheck(2017)
	elif user == "C" : 
		checkcheck(2018)
	elif user == "D" : 
		checkcheck(2019)
	elif user == "E" : 
		checkcheck(2020)
	elif user == "1" : 
		edit_disco()
	elif user == "Q" : 
		view_menu()
	else : 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		discography()
	
#change show episode
def episode_reality(hola, code, date) : 
	system("cls")
	print(f"OLD NUMBER OF EPISODE \t : {reality_show[date][code]['EPISODE']}")
	new_numberepi = input("NEW NUMBER OF EPISODE \t : ")
	new_numberepi = new_numberepi.upper()
	resp = input("ARE YOU SURE YOU WANT TO CHANGE THE NUMBER OF EPISODE ? (Y/N) : ")
	if verify_ans(resp) : 
		system("cls")
		reality_show[date][code]["EPISODE"] = new_numberepi
		time.sleep(1)
		print("\n\n\tTHE NUMBER OF EPISODE HAS BEEN CHANGED")
		input("\tPRESS ENTER TO CONTINUE")
	else : 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		reality_shows()

#change date
def about_reality(hola, code, date) : 
	system("cls")
	print(f"OLD DECRIPTION \t : {reality_show[date][code]['ABOUT']}")
	new_about = input("NEW DESCRIPTION :  ")
	new_about = new_about.upper()
	resp = input("ARE YOU SURE YOU WANT TO CHANGE THE SHOW DESCRIPTION ? (Y/N) : ")
	if verify_ans(resp) : 
		system("cls")
		reality_show[date][code]["ABOUT"] = new_about
		time.sleep(1)
		print("\n\n\tSHOW DESCRIPTION HAS BEEN CHANGED")
		input("\tPRESS ENTER TO CONTINUE")
	else : 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		reality_shows() 

#change show title
def title_reality(hola, code, date) : 
	system("cls")
	print(f"OLD SHOW TITLE \t : {reality_show[date][code]['TITLE']}")
	new_title = input("NEW SHOW TITLE \t : ")
	new_title = new_title.upper()
	resp = input("ARE YOU SURE YOU WANT TO CHANGE THE TITLE NAME ? (Y/N) : ")
	if verify_ans(resp) : 
		system("cls")
		reality_show[date][code]["TITLE"] = new_title
		time.sleep(1)
		print("\n\n\tTHE SHOW TITLE HAS BEEN CHANGED")
		input("\tPRESS ENTER TO CONTINUE")
	else : 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		reality_shows()

#change date
def date_reality(hola, code, date) : 
	system("cls")
	print(f"OLD DATE \t : {reality_show[date][code]['DATE']}")
	new_date = input("NEW DATE \t : ")
	new_date = new_date.upper()
	resp = input("ARE YOU SURE YOU WANT TO CHANGE THE DATE ? (Y/N) : ")
	if verify_ans(resp) : 
		system("cls")
		reality_show[date][code]["DATE"] = new_date
		time.sleep(1)
		print("\n\n\tDATE HAS BEEN CHANGED")
		input("\tPRESS ENTER TO CONTINUE")
	else : 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		reality_shows() 

#check which part of reality show want to be updated
def checky_reality(answer, code, year) : 
	if answer == "1" :
		date_reality(answer, code, year)
	elif answer =="2" : 
		title_reality(answer, code, year)
	elif answer == "3" : 
		about_reality(answer, code, year)
	elif answer == "4" :
		episode_reality(answer, code, year)
	else :
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
	
	reality_shows() 

#print all show in show
def print_reality(num, hahaha, years) : 
	system("cls")
	year = str(years)
	date = reality_show[year][hahaha]["DATE"]
	title = reality_show[year][hahaha]["TITLE"]
	about = reality_show[year][hahaha]["ABOUT"]
	episode = reality_show[year][hahaha]["EPISODE"]

	print(f"\t YEAR \t\t\t : {year}")
	print(f"\t RELEASE DATE \t\t : {date}")
	print(f"\t TITLE \t\t\t : {title}")
	print(f"\t ABOUT \t\t\t : {about}")
	print(f"\t NUMBER OF EPISODES \t : {episode}")

#menu for update reality show
def menu_reality():
	menu = """

		WHAT DO YOU WANT TO UPDATE?
		[1] - RELEASE DATE
		[2] - REALITY SHOW TITLE
		[3] - ABOUT
		[4] - NUMBER OF EPISODES


	"""

	print(menu)

#input for years and which show want to be updated
def update_reality() : 
	system("cls")
	print("WHICH YEAR OF REALITY SHOW YOU WANT TO UPDATE ? ")
	ans = input("Input Here : ")
	
	print()

	if ans in reality_show : 
		answ = int(ans)
		year = str(ans)

		if len(reality_show[year]) == 0 : 
			print("\n\n\tError 304")
			input("\n\n\tPRESS ENTER TO CONTINUE")
		else : 
			for every_song in reality_show[year] : 
				number = every_song[2]
				numbers = str(number)
				title = reality_show[year][every_song]["TITLE"]

				print(f"\t\t{number} - {title}")

		print()
		print("WHICH REALITY SHOW YOU WANT TO UPDATE ? ")
		human = input("Input Here : ")

		print()

		code = "BP" + human
		print_reality(human, code, year)

		menu_reality()

		answer = input("Input Here : ")
		checky_reality(answer, code, year)

	else : 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		discography()

#add to discography this work omg
def up_date(date, title, about, episode, year, code) : 
	years = str(year)

	reality_show[years][code] = {
		"DATE" : date, 
		"TITLE" : title,  
		"ABOUT" : about, 
		"EPISODE" : episode
			}

	time.sleep(1)
	system("cls")
	print()
	print("\n\n\tREALITY SHOW ADDED")
	input("\tPRESS ENTER TO CONTINUE")
	reality_shows()

#format to add new discography
def format_reality(num, hahaha, years) : 
	system("cls")

	year = str(years)
	date = reality_show[year][hahaha]["DATE"]
	title = reality_show[year][hahaha]["TITLE"]
	about = reality_show[year][hahaha]["ABOUT"]
	episode = reality_show[year][hahaha]["EPISODE"]

	print("\t\t FORMAT EXAMPLE\n")
	print(f"\t YEAR \t\t : {year}")
	print(f"\t RELEASE DATE \t : {date}")
	print(f"\t TITLE \t\t : {title}")
	print(f"\t ABOUT \t\t : {about}")
	print(f"\t EPISODE \t : {episode}")

	print()

#deciding the title etc
def add_reality() : 
	system("cls")
	year = input("WHICH YEAR OF REALITY SHOW YOU WOULD LIKE TO ADD ? : ")
	years = int(year)

	numb = " "
	code = "BP1"

	format_reality(numb, code, years)

	date = input("WHEN IS THE RELEASE DATE ? : ")
	title = input("WHAT IS THE SHOW TITLE ? : ")
	about = input("WHAT IS THE SHOW ABOUT ? : ")
	episode = input("HOW MANY EPISODE THE SHOW HAVE ? : ")

	date = date.upper()
	title = title.upper()
	about = about.upper()
	episode = episode.upper()

	kk = len(reality_show[year]) + 1
	kks = int(kk) 
	kkz = str(kks)

	code = "BP" + kkz
	ans = input("ARE YOU SURE YOU WANT TO ADD THE SHOW ? (Y/N) : ")

	if verify_ans(ans) : 
		up_date(date, title, about, episode, years, code)

	else : 
		print("\n\n\t\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		reality_shows()

#print reality shows
def print_show(num, hahaha, years) : 
	system("cls")
	year = str(years)
	date = reality_show[year][hahaha]["DATE"]
	title = reality_show[year][hahaha]["TITLE"]
	about = reality_show[year][hahaha]["ABOUT"]
	episode = reality_show[year][hahaha]["EPISODE"]

	print(f"\t YEAR \t\t\t : {year}")
	print(f"\t RELEASE DATE \t\t : {date}")
	print(f"\t TITLE \t\t\t : {title}")
	print(f"\t ABOUT \t\t\t : {about}")
	print(f"\t NUMBER OF EPISODES \t : {episode}")

	input("\n\n\tPRESS ENTER TO CONTINUE")
	reality_shows()

#check reality shows from certain years
def check_reality(years) : 
	system("cls")
	year = str(years)
	if len(reality_show[year]) == 0 : 
		print("\n\n\t\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
	else : 
		print("\t\tWHICH ALBUM YOU WOULD LIKE TO SEE?")
		for every_show in reality_show[year] : 
			number = every_show[2]
			numbers = str(number)
			show = reality_show[year][every_show]["TITLE"]

			jumlah = len(reality_show[year])

			print(f"\t\t{numbers} - {show}")

	answer = input("Input Here : ")

	answers = str(answer)
	answerd = int(answer)

	if answerd > jumlah: 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		reality_shows()
	else : 
		if answerd > len(reality_show[year]) : 
			system("cls")
			print("\tError 304")
			input("\n\n\tPRESS ENTER TO CONTINUE")
			reality_shows()
		else: 
			code = "BP" + answers
			print_show(answers, code, year)

#edit reality show
def edit_reality() : 
	system("cls")
	menu = """
		What Would You Like To Edit ?
		[A] - Add A Reality Show
		[B] - Update Reality Show

		[Q] - Back
	"""
	print(menu)
	answer = input("Input Here : ")
	answer = answer.upper()

	if answer == "A" :
		add_reality()
	elif answer == "B" : 
		update_reality() 
	elif answer == "Q" : 
		reality_shows()
	else : 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		edit_reality()

def reality_shows() : 
	system("cls")
	menu = """
	Which Year of BLACKPINK Reality Show You Would Like To See? 
	[A] - 2018
	[B] - 2019
	[C] - 2020

	[1] - Edit Reality Show
	[Q] - Back
	"""
	print(menu)

	user = input("Input Here: ")
	user = user.upper()

	if user == "A" : 
		check_reality(2018)
	elif user == "B" : 
		check_reality(2019)
	elif user == "C" : 
		check_reality(2020)
	elif user == "1" : 
		edit_reality()
	elif user == "Q" : 
		view_menu()
	else : 
		system("cls")
		print("\tError 304")
		input("\n\n\tPRESS ENTER TO CONTINUE")
		reality_shows()

def check_input(user) : 
	user = user.upper()
	if user == "1" : 
		discography()
	elif user == "2" : 
		the_pinks()
	elif user == "3" : 
		blackpink()
	elif user == "4" : 
		voting()
	elif user == "5" : 
		reality_shows()
	elif user == "Q" : 
		print("SEE U LATER")
		return True
	elif user == "I" :
		info()

def view_menu() : 
	system("cls")
	menu = """
	WELCOME TO THE MAIN AREA FOR BLINKS!

	[1] - BLACKPINK DISCOGRAPHY
	[2] - BLACKPINK MEMBERS
	[3] - BLACKPINK HISTORY
	[4] - ONGOING VOTING
	[5] - REALITY SHOW

	[Q] - EXIT
	[I] - INFORMATION
	"""
	print(menu)

pinks_profile = {
	"1" : {
		"Name" : "BLACKPINK",
		"Msg" : """

		ABOUT BLACKPINK 

		BLACKPINK (Hangul: 블랙핑크; commonly stylized as BLACKPINK or BLΛƆKPIИK) is 
		a South Korean girl group formed by YG Entertainment, consisting of members 
		Jisoo, Jennie, Rosé, and Lisa. The group debuted in August 2016 with their 
		single album SQUARE ONE, which featured "WHISTLE" and "BOOMBAYAH", their 
		first number-one hits on South Korea's Gaon Digital Chart and the Billboard 
		World Digital Song Sales chart, respectively.

		BLACKPINK is the highest-charting female Korean act on the Billboard Hot 100, 
		peaking at number 13 with their 2020 single "ICE CREAM"). They were the first 
		Korean girl group to enter and top Billboard's Emerging Artists chart and to 
		top the Billboard's World Digital Song Sales chart three times. BLACKPINK is 
		also the first female Korean act to receive a certification from the Recording 
		Industry Association of America (RIAA) with their hit single "DDU-DU DDU-DU" 
		(2018), which currently has the most-viewed music video by a Korean group on 
		YouTube.They have the most top 40 hits in the United Kingdom among all Korean 
		artists.Their 2018 single with Dua Lipa "KISS AND MAKE UP" was the first-ever 
		song by a Korean group to receive a certification from the British Phonographic 
		Industry (BPI) and to be certified platinum by the Australian Recording 
		Industry Association (ARIA). Furthermore, their 2020 single "HOW YOU LIKE THAT" 
		was the first-ever song by a Korean act to receive a certification from 
		Pro-Música Brasil.

		BLACKPINK has broken numerous online records throughout their career; the music 
		videos for "KILL THIS LOVE" (2019), "HOW YOU LIKE THAT", "ICE CREAM" and 
		"LOVESICK GIRLS" (2020) each set records for the most-viewed music video within 
		the first 24 hours of release, with "HOW YOU LIKE THAT" breaking three and setting 
		two Guinness World Records. They are also the first Korean act to have Three music 
		videos with atleast one billion views on YouTube. "HOW YOU LIKE THAT" also became 
		the fastest Korean single to reach double platinum on QQ Music, China's biggest 
		music streaming platform.

		BLACKPINK's other accolades include the New Artist of the Year Awards at the 31st 
		Golden Disc Awards and the 26th Seoul Music Awards, as well as recognition as the 
		most powerful celebrities in South Korea by Forbes Korea in 2019, and as the first 
		female Korean group on Forbes' 30 Under 30 Asia.They were also the first K-pop girlgroup
		to win an MTV Music Video Award. They are currently the most-followed girl group on 
		Spotify and the most-subscribed music group, female act, and Asian act on YouTube.

		Credit : Wikipedia

		"""
	},

	"2" : {
		"Name" : "Kim Jisoo",
		"Msg" : """

		ABOUT KIM JISOO

		Kim Ji-soo (Korean: 김지수; born January 3, 1995), better known mononymously
		as Jisoo, is a South Korean singer and actress. She made her debut in August
		2016 as a member of the girl group Blackpink under YG Entertainment.

		Kim Ji-soo was born on January 3, 1995, in Gunpo, Gyeonggi, South Korea and 
		has an older brother and sister.Jisoo attended high school at the School of 
		Performing Arts Seoul.

		In 2011, Jisoo joined YG Entertainment through auditions as a trainee.In 2015, 
		she made a cameo appearance in the KBS2 drama The Producers with label-mates 
		andara Park of 2NE1 and Kang Seung-yoon of Winner and featured in several 
		advertisements, including those for Samsonite alongside actor Lee Min-ho, 
		Smart Uniform, LG Electronics, and Nikon.

		Jisoo debuted as one of the four members of Blackpink on August 8, 2016, 
		alongside Jennie, Rosé and Lisa, with the release of their single album 
		Square One.Jisoo is the oldest member of Blackpink.

		In September 2018, Jisoo and band-mate Rosé became endorsement models for 
		South Korean cosmetics brand Kiss Me.

		In December 2019, Jisoo became a local ambassador for Dior's cosmetics brand 
		"Dior Beauty". The next summer, Jisoo was recruited to be Dior's muse and
		modelled for Dior's Fall/Winter 2020 collection;In September 2020, Jisoo 
		covered the 155th Edition 2020 of Dazed Korea, where she discussed her work 
		with Dior.She was also appointed as the first protagonist for Cartier Digital 
		Project in the return of "Pasha de Cartier" for Korean MZ generations.


		Credit : Wikipedia

		"""
	},

	"3" : {
		"Name" : "Jennie Kim",
		"Msg" : """

		ABOUT JENNIE KIM

		Jennie Kim (Korean: 김제니; born January 16, 1996), better known by the mononym Jennie, is a 
		South Korean singer and rapper. Born and raised in South Korea, Kim studied in New Zealand
		at the age of eight for five years, before returning to South Korea in 2010. She later 
		debuted as a member of the girl group Blackpink under YG Entertainment in August 2016 and made 
		her solo debut with the single "Solo" on November 12, 2018.

		Jennie Kim was born in the Seoul Capital Area, South Korea on January 16, 1996, as an only child.
		When she was eight years old, she went on a trip with her family to Australia and New Zealand. 
		While in New Zealand, her mother asked her if she liked the place and if she wanted to stay, Kim 
		replied "yes". 
		A year later, she was sent to study at Waikowhai Intermediate School in Auckland, New Zealand and 
		lived with a home-stay family.

		Kim heard of K-pop while residing in New Zealand, particularly finding an interest 
		in YG Entertainment's music.
		Her mother planned to transfer her to the United States in Florida at the age of 14 to continue
		her studies leading to an occupation of a lawyer or teacher, however, the idea wasn't to her liking 
		as she may not find work she liked while residing alone; her family supported her decision and 
		soon had her moved back to South Korea in 2010.

		Jennie was chosen as the new model for Chanel Korea Beauty and shot her first pictorial for the 
		brand with Harper's Bazaar Korea as their new muse in January 2018. Jennie became the Ambassador
		of Chanel Korea in June. A spokesperson from Chanel Korea explained that Jennie's loyalty 
		to the brand as well as her trendy style is in line with Chanel's image, as they seek to target
		young and trendy millennial's in addition to current consumers. Jennie attended the launch of 
		Chanel's new fragrance "Les Eaux De Chanel" in Deauville, France, that same month. She met and 
		interviewed Chanel's in-house perfume creator, Olivier Polge, and shot a pictorial for his new 
		collection of fragrances with Cosmopolitan Korea. In October, she became the Global Ambassador 
		for the French fashion house, joining label-mate G-Dragon. She attended her first Chanel fashion 
		show as a Korean representative during Paris Fashion Week, sitting front row next to 
		Pharrell Williams and Pamela Anderson.

		Hera, a South Korean luxury beauty brand owned by Amore Pacific, announced in January 2019 
		that they had chosen Jennie as their new model due to her "elegant and luxurious" image. She will 
		represent the brand alongside actress Jun Ji-hyun, as the company aims to expand its target audience
		through both models. Jennie's first advertisement for the brand was in February for the Red Vibe 
		lip series, the sales were five times higher than Hera's previous lip product and due to
		the growing popularity they are referred to as "Jennie's lipsticks".

		KT Corporation, South Korea's largest telephone company, recruited Jennie an endorsement model
		alongside Soojoo for the Samsung Galaxy S20 Aura Red and Blue respectively in February 2020. 
		For marketing purposes, the product was also dubbed as "Jennie Red". It was launched exclusively
		for KT customers residing in South Korea. On June 11, 2020 Lotte Confectionery announced 
		Jennie as their brand endorser for their latest snack product, Air Baked. A representative 
		revealed they believed Jennie is considered "trendy" within their targeted customer demographic 
		among women in their 20s and 30s for their latest product.


		Credit : Wikipedia

		"""
	}, 

	"4" : {
		"Name" : "Park Chaeyoung",
		"Msg" : """

		ABOUT PARK CHAEYOUNG

		Roseanne Park (born 11 February 1997), better known by the mononym Rosé (Korean: 로제), is a New Zealand
		singer currently based in South Korea. Rosé signed with South Korean label YG Entertainment following
		an audition in 2012, training there for four years. She eventually made her debut as the main 
		vocalist in the girl group Blackpink in August 2016. As a solo artist, she has featured in 
		labelmate G-Dragon's 2012 track "Without You", which peaked at number ten on the Gaon Music Chart.

		Roseanne Park (Korean: 박채영; Park Chae-young) was born on 11 February 1997 in Auckland, New Zealand, 
		to South Korean immigrant parents. She has an older sister. In 2004, at the age of seven, Rosé
		and her family moved to Melbourne, Australia. Rosé attended Canterbury Girls' Secondary College in 
		Melbourne. She began singing and learned to play guitar and piano as a child and 
		performed in church choirs.

		In 2012, 15-year-old Rosé attended an audition in Australia for South Korean record label YG 
		Entertainment at her father's suggestion and was ranked first among 700 participants.
		Within two months she had signed with the label and moved to Seoul.

		Rosé's voice has received acknowledgement in the K-pop industry for its distinct vocal timbre, 
		following her debut as a member of Blackpink. Following Rosé's performance on an episode
		of Fantastic Duo 2, South Korean singer Gummy, whom Rosé cited as a musical role model, stated that
		"Rosé's voice is so unique, it's the type of voice young people love".

		In 2018, Rosé and fellow Blackpink member Jisoo were selected as endorsement models for 
		the South Korean cosmetics brand Kiss Me. In October 2019, Rosé was revealed as a promotional 
		model for the Perfect World Entertainment's MMORPG Perfect World Mobile. In 2020, Rosé was
		named the global ambassador for Yves Saint Laurent by Anthony Vaccarello.
		She was the global face for Saint Laurent's Fall 2020 campaign.


		Credit : Wikipedia

		"""
	}, 

	"5" : {
		"Name" : "Lalisa Manoban",
		"Msg" : """

		ABOUT LALISA MANOBAN

		Lalisa Manoban (Thai: ลลิษา มโนบาล; born Pranpriya Manoban (Thai: ปราณปรียา มโนบาล) on March 27, 1997), 
		better known by the mononym Lisa (Hangul: 리사), is a Thai rapper, singer and dancer based in 
		South Korea. She is a member of the South Korean girl group Blackpink under YG Entertainment.

		Born as Pranpriya Manoban on March 27, 1997 in Buriram Province, Thailand, she later legally 
		changed her name to Lalisa. She is of Thai descent, and the only child of her Thai mother
		and Swiss step-father.
		Lisa completed secondary education at Praphamontree School I and II. 
		From a young age, Lisa gained an interest in the South Korean pop industry, namely 
		admiring artists Big Bang and 2NE1, and wished to someday follow a similar path.

		In 2010, Lisa auditioned to join YG Entertainment in Thailand. Among the 4,000 applicants, 
		she was the only individual to pass. She officially joined the label as their first 
		non-ethnically Korean trainee on April 11, 2011.

		In August 2016, Lisa debuted as one of four members of South Korean girl group Blackpink, 
		as well as the first non-ethnically Korean to debut under the agency.

		In January 2019, Lisa became the muse of Hedi Slimane, the artistic, creative and image director
		for Celine, a French luxury brand. The same year, in November, Penshoppe revealed Lisa 
		had joined the Penshoppe family as their newest ambassador. Furthermore, on July 24, 2020
		Lisa was officially selected as the newest brand ambassador representing Bulgari, 
		an Italian luxury brand. As an ambassador for Bulgari, she participated in the digital campaigns 
		for the "Serpenti" and "Bzero One" collections.


		Credit : Wikipedia

		"""
	}
}

list_of_songs = {
	"2016" : {	
		"BP1" : {
			"DATE" : "AUGUST 8TH, 8PM KST",
			"ALBUM" : "SQUARE ONE", 
			"TRACKS" : {
				"1" : "BOOMBAYAH", 
				"2" : "WHISTLE"
			}
		}, 
		"BP2" : {
			"DATE" : "NOVEMBER 1ST, 12AM KST",
			"ALBUM" : "SQUARE TWO",
			"TRACKS" : {
				"1" : "PLAYING WITH FIRE", 
				"2" : "STAY"
			}
		}
	},

	"2017" : {	
		"BP1" : {
			"DATE" : "JUNE 22ND, 6PM KST",
			"ALBUM" : "AS IF IT'S YOUR LAST", 
			"TRACKS" : {
				"1" : "AS IF IT'S YOUR LAST" 
			}
		}, 
		"BP2" : {
			"DATE" : "DECEMBER 25TH, 9PM KST", 
			"ALBUM" : "SO HOT THEBLACKLABEL REMIX",
			"TRACKS" : {
				"1" : "SO HOT THEBLACKLABEL REMIX"
			}
		}
	}, 
	
	"2018" : {
		"BP1" : {
			"DATE" : "JUNE 15TH, 6PM KST", 
			"ALBUM" : "SQUARE UP", 
			"TRACKS" : {
				"1" : "DDU-DU DDU-DU",
				"2" : "FOREVER YOUNG",
				"3" : "REALLY",
				"4" : "SEE U LATER" 
			}
		}, 
		"BP2" : {
			"DATE" : "OCTOBER 19TH", 
			"ALBUM" : "DUA LIPA - COMPLETE EDITION", 
			"TRACKS" : {
				"1" : "KISS AND MAKE UP"
			}
		}, 
			
		"BP3" : {
			"DATE" : "NOVEMBER 12TH, 6PM KST", 
			"ALBUM" : "SOLO", 
			"TRACKS" : {
				"1" : "SOLO", 
				"2" : "SOLO INSTRUMENTAL" 
			}
		}
	}, 

	"2019" : {
		"BP1" : {
			"DATE" : "APRIL 5TH, 12AM KST", 
			"ALBUM" : "KILL THIS LOVE", 
			"TRACKS" : {
				"1" : "KILL THIS LOVE", 
				"2" : "DON'T KNOW WHAT TO DO", 
				"3" : "KICK IT", 
				"4" : "HOPE NOT", 
				"5" : "DDU-DU DDU-DU REMIX"
			}
		}
	}, 

	"2020" : {
		"BP1" : {
			"DATE" : "MAY 28TH", 
			"ALBUM" : "LADY GAGA - CHROMATICA", 
			"TRACKS" : {
				"1" : "SOUR CANDY"
			}
		}, 
		"BP2" : {
			"DATE" : "JUNE 26TH, 6PM KST", 
			"ALBUM" : "HOW YOU LIKE THAT",
			"TRACKS" : {
				"1" : "HOW YOU LIKE THAT"
			}
		}, 
		"BP3" : {
			"DATE" : "AUGUST 28TH, 1PM KST", 
			"ALBUM" : "ICE CREAM WITH SELENA GOMEZ", 
			"TRACKS" : {
				"1" : "ICE CREAM "
			}
		}, 
		"BP4" : {
			"DATE" : "OCTOBER 2ND, 1PM KST", 
			"ALBUM" : "THE ALBUM", 
			"TRACKS" : {
				"1" : "HOW YOU LIKE THAT",
				"2" : "ICE CREAM",
				"3" : "PRETTY SAVAGE", 
				"4" : "BET YOU WANNA WITH CARDI B", 
				"5" : "LOVESICK GIRLS", 
				"6" : "CRAZY OVER YOU", 
				"7" : "LOVE TO HATE ME",
				"8" : "YOU NEVER KNOW"
			}
		}, 
		"BP5" : {
			"DATE" : "UNRELEASED BUT PLAYED ON OCTOBER 14TH",
			"ALBUM" : "UNRELEASED",
			"TRACKS" : {
				"1" : "READY FOR LOVE"
			}
		}
	}
}

reality_show = {
	"2018" : {
		"BP1" : {
			"DATE" : "JANUARY 6TH - MARCH 17TH, AUGUST 18TH", 
			"TITLE" : "BLACKPINK HOUSE", 
			"ABOUT" : "100 DAYS HOLIDAY FOR BLACKPINK", 
			"EPISODE" : "12 EPISODES"
		}, 

		"BP2" : {
			"DATE" : "NOVEMBER 18TH - DECEMBER 28TH", 
			"TITLE" : "JENNIE - 'SOLO' DIARY", 
			"ABOUT" : "BEHIND THE SCENES OF JENNIE SOLO", 
			"EPISODE" : "6 EPISODES INCLUDING 1 ADDITIONAL SPECIAL EPISODE" 
		}
	}, 

	"2019" : {
		"BP1" : {
			"DATE" : "FEBRUARY 16TH-OCTOBER 27TH",
			"TITLE" : "BLACKPINK DIARIES",
			"ABOUT" : "BEHIND THE SCENES DURING BLACKPINK WORLD TOUR",
			"EPISODE" : "16 EPISODES"
		}
	}, 

	"2020" : {
		"BP1" : {
			"DATE" : "JULY 4TH - TODAY",
			"TITLE" : "24/365 WITH BLACKPINK", 
			"ABOUT" : "BEHIND THE SCENES OF MV, ADDITIONAL CLIPS OF BLACKPINK PLAYING AROUND",
			"EPISODE" : "14 EPISODES SO FAR"
		}, 

		"BP2" : {
			"DATE" : "OCTOBER 14TH",
			"TITLE" : "BLACKPINK : LIGHT UP THE SKY",
			"ABOUT" : "RECORD-SHATTERING KOREAN GIRL BAND BLACKPINK TELL THEIR STORY\n\t\t\t   AND DETAIL THE HARD-FOUGHT JOURNEY OF THE DREAMS AND TRIALS\n\t\t\t   BEHIND THEIR METEORIC RISE.", 
			"EPISODE" : "1 HOUR 19 MINUTES"
		}
	}
}	

Continue = False

while not Continue : 
	view_menu()
	user_input = input("Where Do You Wanna Go ? : ")
	Continue = check_input(user_input)
