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
    n=int(input('Starting Day'))#Another possible solution would be 
    print(h[n])#to sum up given two variables which is alternatively
    t=int(input('Length of stayings'))#(n+(t%7))%7 mod explains whether 
    stay(t)#we complete a week or not for all of day accordances stay function compute all conditions
    #By commiting 2 times mod would be adequate and necessary to realize if we already pass the lenght of the list
   
