# def draw_stars(val):
#     for i in range(0,len(val)):
#         print val[i]*'*'


# x=[4, 6, 1, 3, 5, 7, 25]
# draw_stars(x)


def draw_stars(val):
    # print val[0][0]
    for i in range(0,len(val)):
        if type(val[i])== str:
            print val[i][0].lower()*len(val[i])
        else:
            print val[i]*'*'


x=["Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)