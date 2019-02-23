# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1
import requests,re,platform,os
sys = platform.system()
if 'Linux' in sys:os.system('clear')
if 'Windows' in sys: os.system('cls')
print('''     ______    _ _             _____             _       
     |  ___|  | | |           |_   _|           (_)      
     | |_ ___ | | | _____      _| __      ____ _ _ _ __  
     |  _/ _ \| | |/ _ \ \ /\ / | \ \ /\ / / _` | | '_ \ 
     | || (_) | | | (_) \ V  V /| |\ V  V | (_| | | | | |
     \_| \___/|_|_|\___/ \_/\_/ \_/ \_/\_/ \__,_|_|_| |_|
                                                    
You can know whether the two users are following each other or not.					
													
         CoDeD By 1337r00t (Twitter: @0x1337r00t)
               BlackfoxsOrg Group © 2019			   
                   Exit -> CTRL + C''')
version = re.findall(r'^[\w\.-]', platform.python_version())
if '2' in version:
	user1 = raw_input("Enter First Username => ")
	user2 = raw_input("Enter Second Username => ")
if '3' in version:
	user1 = str(input("Enter First Username => "))
	user2 = str(input("Enter Second Username => "))
is_it_user1,is_it_user2 = None,None
follow = lambda s,c : requests.get('https://api.twitter.com/1.1/friends/list.json?pc=true&include_user_entities=true&include_profile_interstitial_type=true&screen_name='+s+'&cursor='+c,auth=OAuth1('3nVuSoBZnx6U4vzUxf5w','Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys',decoding=None))
default_cursor = '-1'
##########################
# Check for First Username
do1 = follow(user1,default_cursor).text
while True:
	if '"screen_name":"'+user2+'"' in do1:
		print(user1+' Follows '+user2)
		is_it_user1 = "Follows"
		break
	else:
		print("Not Found ("+default_cursor+" cursor) Generating Cursor !...")
		if default_cursor == '0': break
	default_cursor,is_it_user1 = follow(user1,default_cursor).json()['next_cursor_str'],"Does't Follows"
print("First User / "+user1+" Status : Finished")
default_cursor = '-1'
###########################
# Check for Second Username
do2 = follow(user2,default_cursor).text
while True:
	if '"screen_name":"'+user1+'"' in do2:
		print(user2+' Follows '+user1)
		is_it_user2 = "Follows"
		break
	else:
		print("Not Found ("+default_cursor+" cursor) Generating Cursor !...")
		if default_cursor == '0': break
	default_cursor,is_it_user2 = follow(user1,default_cursor).json()['next_cursor_str'],"Does't Follows"
print("First User / "+user2+" Status : Finished")
if 'Linux' in sys:os.system('clear')
if 'Windows' in sys: os.system('cls')
############################
print('''     ______    _ _             _____             _       
     |  ___|  | | |           |_   _|           (_)      
     | |_ ___ | | | _____      _| __      ____ _ _ _ __  
     |  _/ _ \| | |/ _ \ \ /\ / | \ \ /\ / / _` | | '_ \ 
     | || (_) | | | (_) \ V  V /| |\ V  V | (_| | | | | |
     \_| \___/|_|_|\___/ \_/\_/ \_/ \_/\_/ \__,_|_|_| |_|
                                                    
+--------------------------------------------------+
(@'''+user1+''') '''+is_it_user1+''' (@'''+user2+''')
(@'''+user2+''') '''+is_it_user2+''' (@'''+user1+''')
+--------------------------------------------------+''')
