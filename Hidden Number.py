from getpass import getpass
import time
a=[]
b=[]
valor_a=[]
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Fire in the hole!!') 

def comproba(valor):
    print (valor)
    valor_a=getpass(prompt= "Num: " )
    if (a[1]==valor_a[1]):
        print ("C")            

def inici():
    playerA=input("Nom jugador 1: ")
    playerB=input("Nom jugador 2: ")
    print ("{:s}: ".format(playerA))    
    a=getpass(prompt= "Introdueix el numero: ")
    print (a)
    print ("{:s}: ".format(playerB))
    b=getpass(prompt= "Introdueix el numero: ")
    print (b)
    comproba(a)

inici()

# input time in seconds 
#t = input("Enter the time in seconds: ") 
 
# function call 
#countdown(int(t)) 
