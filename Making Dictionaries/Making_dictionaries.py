

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane"]
fav_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def concat(a,b):
    if len(a)>len(b) or len(a)==len(b):
        return zip(a,b)
    else:
        return zip(b,a)

print concat(name,fav_animal)


    
