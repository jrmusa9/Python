import random
def coins():
    tails=0
    heads=0
    print 'Starting the program...'
    for i in range(1,5001):
        x=round(random.random())
        if x == 1:
            heads+=1
            print 'Attempt #{}: Throwing a coin... It\'s a head! ... Got {} head(s) so far and {} tail(s) so far'.format(i,heads,tails)
        elif x == 0:
            tails+=1
            print 'Attempt #{}: Throwing a coin... It\'s a tails! ... Got {} head(s) so far and {} tail(s) so far'.format(i,heads,tails)
    print 'Ending the program, thank you!'
                

coins()