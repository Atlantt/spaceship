print " Hello "
print " It's a little game about space. "
print " The enemy in front of you, shoot his spaceship ."
print " In order to shoot, enter the coordinates of the enemy ship ."
Restart="Yes"
while Restart == "Yes":
    prop=1
    while prop == 1:
        Tx,Ty=input("Enter the coordinates of the ship, separated by commas ")
        if Tx in range(9):
            if Ty in range(9):
                prop=0
        else :
            print "Error , limit 8 "
    limit_shots=0
    while limit_shots <= 1:
        T1x,T1y=input("Enter the coordinates where you want to shoot , separated by commas ")
        if T1x == Tx:
            if T1y == Ty:
                print "Hit !"
                limit_shots=2
                result="You are victorious !!!"
            else:
                print "Miss !!!"
                limit_shots=limit_shots+1
                result="You lose"
                if T1y > Ty:
                    print "Target is located below "
                elif T1y < Ty:
                    print "The target is above "
        else :
            print "Miss !!!"
            limit_shots=limit_shots+1
            result="You lose"
            if T1x > Tx:
                if T1y < Ty:
                    print "Target is located above and to the left "
                elif T1y == Ty:
                    print "The target is to the left "
                elif T1y > Ty:
                    print "The target is below and to the left "
            elif T1x < Tx:
                if T1y < Ty:
                    print "The target is to the right and above "
                elif T1y == Ty:
                    print "The target is to the right "
                elif T1y > Ty:
                    print "The target is to the right and below "
                
    print result
    Restart=raw_input("Enter the Yes to continue or No to end.  ")
