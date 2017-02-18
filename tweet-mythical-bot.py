'''

.............................IIII.......
..................ZZ~......?IIIIII?.....
............:.I7=?+Z$$$7ZI7IIIII..,I:...
............,7+?IIII$$$$IIIIIIII,.III7,.
...............+?IIIIIIIIIIIIIIIIIII,...
..................I7IIIIIIIIIIIIIIII....
..................IIIIIIIIIII?+:,=I.....
...............=?IIIIIIIIIII:::::::.....
.,=........,=IIIIIIIIIIIII:::::,:,......
....~?I??IIIIIIIIIIIIIIII:::,:::........
.......+?IIIIIIIIIIIIIII:::::::.. ......
..........~IIIIIIIIIIIII:::::...........
................~?IIIIII=...............
........................................
............. ................. ........
............. ,:::::::::::::::,.........



Mythical-Twitter-bot which lets you to tweet instantly without opening browser.

Time utilized - 1 hrs
Key points - To select form and then tweet it and then select new user everytime.
TEST #1 - At tweet 11 it is still working fine. - ACCEPTED

'''

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    import Cookie
    import cookielib
    import mechanize
    import time
    import os
    from getpass import getpass
    from bs4 import BeautifulSoup
    print bcolors.OKGREEN+'Import: OK'+bcolors.ENDC
except:
    print bcolors.FAIL+'Import: FAILED'+bcolors.ENDC
time.sleep(1)

previous = 'a'
tcount = 1

def loading():
    load = 0
    for i in xrange(1800):
        sys.stdout.write('\r')
        sys.stdout.write("[%-50s] %.2f%%" % ('='*(int(load)/2), load))
        sys.stdout.flush()
        load = ((i+1)/float(1800))*100
        time.sleep(1)

def tweetWork():
    '''Opens given URL page and extract user information.

    Here you need to change the page URL to specify on which page you want to extract user name
    '''
    global tcount
    global previous
    print bcolors.OKGREEN+bcolors.BOLD+'Working on Tweet: '+str(tcount+1)+bcolors.ENDC
    try:
        br.open('https://twitter.com/hashtag/100daysofcode?f=tweets&vertical=default&src=hash')           # Your page url
        print bcolors.OKGREEN+'Connection: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Connetion Lost'+bcolors.ENDC
        while True:
            x = 1
            try:
                br.open('https://twitter.com/hashtag/100daysofcode?f=tweets&vertical=default&src=hash')   # Your page url
                print bcolors.OKGREEN+'Connection: OK'+bcolors.ENDC
                break
            except:
                print bcolors.WARNING+'Trying ... '+x+'/3'
                x+=1
    soup = BeautifulSoup(br.response().read())
    l = soup.find_all('span',{'class': 'username js-action-profile-name'})
    try:
        file = open("user.txt","r")
        names = file.read().splitlines()
        file.close()
    except:
        names = ['a']
        pass
    file = open('user.txt','a+')
    for i in l:
        if str(i.text) in names:
            pass
        else:
            file.write(i.text+'\n')
    file.close()
    user = str(l[0].text)
    print '\n'
    print bcolors.OKGREEN+bcolors.BOLD+user+bcolors.ENDC
    if 'bot' in user or '@_100DaysOfCode'in user:
        print 'Bot found :P'
        tweetWork()
    if user == previous:
        print bcolors.WARNING+'Loading next session'+bcolors.ENDC
        loading()
        tweetWork()
    else:
        previous = user
        tweet(user)


def tweet(user):
    '''Takes message and then with given user it will tweet it every 30 min.

    No need to change anything here except the given time in seconds and messages 
    accoding to your needs.
    '''
    global tcount

    # Change your message here
    msg = [' Way to go. You are doing really great work just keep doing it. Happy Coding #100DaysOfCode',' Keep up this good work, What you are doing is really awesome - Happy Coding #100DaysOfCode'," 'No retreat, No surrender', Keep moving forward - Happy Coding #100DaysOfCode"," 'You mustnt be afraid to dream a little bigger', - Happy Coding #100DaysOfCode"," 'If its worth it, fight for it', FIGHT! - Happy Coding #100DaysOfCode"," 'The power to shine is in every one of us', - Happy Coding SHINE Now #100DaysOfCode"," 'Its not gonna be easy, but its gonna be worth it' - Happy Coding #100DaysOfCode"," 'No Excuses', Just do it and do it - Happy Coding #100DaysOfCode"," 'Be YOUR best, despite the odds' - Happy Coding #100DaysOfCode"," 'Dont let anybody tell you that you cant do something'- Happy coding #100DaysOfCode"," 'Nothing stops. Nothing', Confusing? nevermind Keep Coding - #100DaysOfCode"]
    print bcolors.WARNING+'Enabling Tweet setting . . .'
    url = 'https://mobile.twitter.com/compose/tweet'                       #No need to change this it is use to make tweet quickly
    br.open('https://mobile.twitter.com/compose/tweet')
    br.select_form(nr = 0)
    br['tweet[text]'] = user+msg[tcount%11]
    print bcolors.WARNING+'Message: '+user+msg[tcount%11]
    print bcolors.WARNING+'Sending...'+bcolors.ENDC
    try:
        br.submit()
        print bcolors.OKGREEN+'Submit: OK'+bcolors.ENDC
        tcount+=1
    except:
        print bcolors.WARNING+'Submit: Failed'+bcolors.ENDC
    print bcolors.WARNING+'\n\nLoading next session'+bcolors.ENDC
    loading()
    tweetWork()


'''

Below code is used to login into twitter account and save cookies

Avoid changing anything from here until and unless you know what you are doing.
NOTE: COOKIES WILL BE SAVED IN YOUR LOCAL STORAGE SO MAKE SURE YOU TAKE EXTRA CARE
ELSE ANYONE CAN ACCESS YOUR ACCOUNT BY THAT.

'''

print bcolors.OKBLUE+'''
.............................IIII.......
..................ZZ~......?IIIIII?.....
............:.I7=?+Z$$$7ZI7IIIII..,I:...
............,7+?IIII$$$$IIIIIIII,.III7,.
...............+?IIIIIIIIIIIIIIIIIII,...
..................I7IIIIIIIIIIIIIIII....
..................IIIIIIIIIII?+:,=I.....
...............=?IIIIIIIIIII:::::::.....
.,=........,=IIIIIIIIIIIII:::::,:,......
....~?I??IIIIIIIIIIIIIIII:::,:::........
.......+?IIIIIIIIIIIIIII:::::::.. ......
..........~IIIIIIIIIIIII:::::...........
................~?IIIIII=...............
........................................
............. ................. ........
............. ,:::::::::::::::,.........
'''+bcolors.ENDC

if os.path.isfile('./.cookies.txt'):
    print bcolors.OKGREEN+'Compiled: Successfully'+bcolors.ENDC
    time.sleep(1)
    print bcolors.OKGREEN+'Cookies: FOUND'+bcolors.ENDC
    time.sleep(1)
    try:
        br = mechanize.Browser()
        print bcolors.OKGREEN+'Mechanize Browser: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Browser Setting: FAILED'+bcolors.ENDC
    time.sleep(1)
    cookiejar =cookielib.LWPCookieJar()
    br.set_cookiejar(cookiejar)
    cookiejar.load('.cookies.txt', ignore_discard=True, ignore_expires=True)
    br.set_handle_robots(False)
    print bcolors.OKGREEN+'Robots settings: OK'+bcolors.ENDC
    print bcolors.OKGREEN+'\nStatus: ACCESS GRANTED'+bcolors.ENDC
    try:
        br.open('https://mobile.twitter.com/')
        print bcolors.OKGREEN+'Connection: OK'+bcolors.ENDC
    except:
        cou = 0
        print bcolors.FAIL+'Connection: Not Connected'+bcolors.ENDC
        while True:
            print bcolors.WARNING+'Trying again: '+str(cou+1)+'/3'+bcolors.ENDC
            try:
                br.open('https://mobile.twitter.com/')
                print bcolors.OKGREEN+'Connection: OK'+bcolors.ENDC
                break
            except:
                cou+=1
            if cou >= 3:
                print bcolors.FAIL+'Failed Quitting'+bcolors.ENDC
                failno = 1
                break
    soup = BeautifulSoup(br.response().read())
    #coname = soup.find_all('a',{'class': '_5jlw _3t21'})
    #for i in coname:
    #    print bcolors.OKGREEN+'User: '+str(i.text)+bcolors.ENDC
    #    break


else:
    cookiejar =cookielib.LWPCookieJar('.cookies.txt')
    print bcolors.OKGREEN+'Compiled: Successfully'+bcolors.ENDC
    print bcolors.OKGREEN+'Cookies.txt: NOT FOUND'+bcolors.ENDC
    time.sleep(1)
    try:
        br = mechanize.Browser()
        print bcolors.OKGREEN+'Mechanize Browser: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Browser Setting: FAILED'+bcolors.ENDC
        failno = 1
    time.sleep(1)
    try:
        br.set_cookiejar(cookiejar)
        print bcolors.OKGREEN+'Browser cookies: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Browser cookies: FAILED'+bcolors.ENDC
        failno = 1
    time.sleep(1)
    # Robots is not false
    #br.set_handle_robots(False)
    print bcolors.OKGREEN+'Robots settings: OK'+bcolors.ENDC
    failno = 0
    try:
        br.open('https://mobile.twitter.com/login')
        print bcolors.OKGREEN+'Connection: OK'+bcolors.ENDC
    except:
        cou = 0
        print bcolors.FAIL+'Connection: Not Connected'+bcolors.ENDC
        while True:
            print bcolors.WARNING+'Trying again: '+str(cou+1)+'/3'+bcolors.ENDC
            try:
                br.open('https://mobile.twitter.com/login')
                print bcolors.OKGREEN+'Connection: OK'+bcolors.ENDC
                break
            except:
                cou+=1
            if cou >= 3:
                print bcolors.FAIL+'Failed Quitting'+bcolors.ENDC
                failno = 1
                break
    if failno == 0:
        br._factory.is_html = True
        try:
            br.select_form(nr = 0)
            print bcolors.OKGREEN+'Form selected: OK'+bcolors.ENDC
        except:
            print bcolors.FAIL+'Form selected: FAILED'+bcolors.ENDC
        print bcolors.BOLD + "Email:" + bcolors.ENDC,
        email = raw_input()
        br['session[username_or_email]'] = email
        passw = getpass()
        print bcolors.OKBLUE+'\nSubmitting:'+ bcolors.ENDC,
        br['session[password]'] = passw
        try:
            br.submit()
            print bcolors.OKGREEN+'OK'+bcolors.ENDC
        except:
            cou = 0
            print bcolors.FAIL+'FAILED'+bcolors.ENDC
            while True:
                print bcolors.WARNING+'Trying again: '+str(cou+1)+'/3'+bcolors.ENDC
                try:
                    br.submit()
                    print bcolors.OKGREEN+'OK'+bcolors.ENDC
                except:
                    cou += 1
                if cou>= 3:
                    print bcolors.FAIL+'Failed Quitting'+bcolors.ENDC
                    failno = 1
                    break

        cookiejar.save()
        soup = BeautifulSoup(br.response().read())

if 'try again' in str(soup):
    print bcolors.FAIL+'Log in: Failed'+bcolors.ENDC
else:
    print bcolors.OKGREEN+bcolors.BOLD+'Log in: Accepted'+bcolors.ENDC
    print bcolors.OKGREEN+'Mythical Bot is ready'+bcolors.ENDC
    check = raw_input('Press Enter to continue')
    tweetWork()
