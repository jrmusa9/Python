# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# PART I
# def names(list):
#     for i in range(0,len(list)):
#         for key,val in list[i].items():
#             print val,
#         print '\r'

# names(students)




# PART II

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def names(list):
    
    for key,val in list.items():  #MAIN ITEMS
        x=1
        print key
        for i in val: #LIST OF DICTS
            print x,'-',
            length=0
            for key, val in i.items(): # KEYS AND VALS OF DIST.
                print val,
                length+=len(val)
            print '- ',length    
            x+=1



names(users)

