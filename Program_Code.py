import random
c=["Rock","Paper","Scissors" ]
d1={}
d2={}
q=0
t=0
l=[]
d='y'
for i in range(1,11):
    p=input("Enter player's choice")
    s=random.choices(c,k=1)
    u= ' '.join(map(str, s))
    print("Computer's choice=%s" %(u))
    d1[i]=p
    d2[i]=u
    if(((p=='Paper') and (u=='Rock')) or ((p=='Scissors') and (u=='Paper'))or ((p=='Rock') and (u=='Scissors'))):
        l.append('P')
        q=q+1
    elif(((u=='Paper') and (p=='Rock')) or ((u=='Scissors') and (p=='Paper')) or ((u=='Rock') and (p=='Scissors'))):
        l.append('C')
        t=t+1
    else:
        l.append('T')
if(q>t):
    print("Player won")
elif (q==t):
    print("Tie")
else:
    print("Computer won")
print("Player's points= %d and Computer's points= %d" %(q,t))
while(d=='y'):
    x=int(input("Enter the round for which you need the information >>"))
    print("Players choice=%s" %(d1[x]))
    print("Computer's choice=%s" %(d2[x]))
    if(l[x-1]=='P'):
        print("Player won round %d" %(x))
    elif(l[x-1]=='C'):
        print("Computer won round %d" %(x))
    else:
        print("Tie")
    d=input("Try again? press 'y' for yes and 'n' for no")
