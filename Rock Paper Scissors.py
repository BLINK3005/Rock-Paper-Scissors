import random,time
L=['R','P','S']
sa=0
ss=0
s=1
while True:
    print("1-Play\n2-Help\n3-Quit")
    c=input("Enter Your Choice(1,2,3):")
    if c=='1':
        print("Press 'Q' to Exit!")
        while True:
            print("")
            s=input("Rock[R],Paper[P],Scissors[S]:").strip().upper()
            a=random.choice(L)
            if s==a:
                print("Draw [ You:",ss,'NPC:',sa,']')
            elif s=='R'and a=='P':
                sa+=1
                print("NPC Scored! { You:",ss,'NPC:',sa,'}')
            elif s=='R'and a=='S':
                ss+=1
                print("You Scored! { You:",ss,'NPC:',sa,'}')
            elif s=='P'and a=='R':
                ss+=1
                print("You Scored! { You:",ss,'NPC:',sa,'}')
            elif s=='P' and a=='S':
                sa+=1
                print("NPC Scored! { You:",ss,'NPC:',sa,'}')
            elif s=='S'and a=='R':
                sa+=1
                print("NPC Scored! { You:",ss,'NPC:',sa,'}')
            elif s=='S'and a=='P':
                ss+=1
                print("You Scored! { You:",ss,'NPC:',sa,'}')
            elif s=='Q':
                break
            else:
                print("Invaid Option, Dont Hurry Bro")
    elif c=='2':
        print("-Help Menu-")
        print("1.Same Rules As You Play In Real-Life\n2.Use ShortCuts To Play\n3.Dont Hurry!\n4.Report Button Soon!\n")
    elif c=='3':
        print("Thanks For Playing!<3")
        time.sleep(1.5)
        break
    else:
        print("Enter A Valid Choice!")
        
         
    
