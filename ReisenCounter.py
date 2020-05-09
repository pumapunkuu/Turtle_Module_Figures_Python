h=['M','T','WED','THU','FR','SA','SUN'];

def stay(k):
    if(k%7==0):
        print(h[n%7])
    elif(k%7==1):
        print(h[(n+1)%7])
    elif(k%7==2):
        print(h[(n+2)%7])    
    elif(k%7==3):
        print(h[(n+3)%7])
    elif(k%7==4):
        print(h[(n+4)%7])
    elif(k%7==5):
        print(h[(n+5)%7])
    elif(k%7==6):
        print(h[(n+6)%7])
    elif(k%7==7):
        print(h[(n+7)%7])
    


while True:
    n=int(input('Starting Day'))
    print(h[n])
    t=int(input('Length of stayings'))
    stay(t)
   