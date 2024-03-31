# Social-Media-Brute-Force-tool
Made this tool to play with playwright, learn about proxies and how business like insta keep them safe from brute force attacks.

It is technically not possible to brute force insta accounts by trying large number of random passwords, but i recently came across a password list (From a data breach) of real Indian users and realised that still a large percentage of internet users in India have very weak passwords such as theirname@123, 12345678 or phonenumbers etc, hence i wanted to generate a user specific password list of 60-100 passwords which are not completely random but real world passwords (I created a password list after analyzing several data breach documents) optimised for our specific victim thereby increasing our chances of successfull bruteforce attack!

# How To Use:

1) Use Social Enginnering techniques to gather basic information about your victim such as their first_name, last_name, religion, phone_number, relationship status and names if any, address, DOB, Special Numbers such as vehicle numbers ,house number , room number etc. Note: More the information, longer would be the password list and hence More chances of success
2) Feed This Data to pass_gen.py file in terminal, it will generate a password list as a pass_list.csv file
3) View, Edit This .csv file and Add anyother pass as you wish
4) Next go and edit username of victim in attack.py file under controls section, choose anyother web based proxy service if you wish, by default it uses proxyium.

# Here's How It Works:

1) Based on the most common passwords pass_gen.py will generate a user specific password list  
2) Attack.py file uses proxyium, a webbased proxy to change IP address of attack machine after every 5 unsuccessful attempts as it continues to try each and every password in password list!
3) Also Note that the program is itself able to deal with any unintentional popups during execution such as cookies
4) It is also not marked as bot and returns correct password in most cases!

# What I Wish To Do In Future:

1) Instead of using webbased proxy i should be using a real proxy chain 
2) Optimize password list generating method
3) Fix Problems related to password found function as it fails in few cases and might not be the best solution
4) Do a real world survey to check it's success rate

# Issues:
1) As it uses a webbased proxy, attack unexpectedly crashes sometimes if there's a problem with internet connection
2) Again if weak internet, there's a possibility that program might mark correct password as wrong password because the page fails to load correctly!
