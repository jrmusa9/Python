import random

def score(val):
    print 'Scores and grades'
    
    for i in range(val):
        x=random.randint(60,100)
        if x >59 and x<70:
            print 'Score: {}; Your grade is D'.format(x)
        elif x >70 and x<79:
            print 'Score: {}; Your grade is C'.format(x)
        elif x >79 and x<89:
            print'Score: {}; Your grade is B'.format(x)
        else:
            print 'Score: {}; Your grade is A'.format(x)
        
score(7)

