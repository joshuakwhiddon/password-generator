
#packages
import random
#Files
file = open('password.txt', 'a')
#variables
website = input('enter name of website for password:')
username = input('enter your username:')
number = input('How long do you want you password:')
number = int(number)
#password key
options = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',':',';','<','>',',','.','/','?','[',']','!','@','#','$','%','^','&','*','(',')','-','=','`','~' ]
#randomization code
answer = random.SystemRandom()
CODE = ""

#generator
while number > 0:
    CODE = CODE + answer.choice(options)
    number = number - 1

#output
if number <= 0:
    print(CODE)
    file.write('------------- \n' + 'website url: ' + website + '\n')
    file.write('\n' + 'Username: ' + username + '\n')
    file.write('Password:' + CODE + '\n------------- \n')
    file.close()
else:
    print('void')
