me={
    'nickname': 'Juan',
    'age' : '34',
    'country of birth':'USA',
    'favorite language':'Python'
}

def myself(dict):
    for x, y in dict.items():
        print '{}:{}'.format(x,y)


myself(me)

