# sameName3 from Chapter 3

def spam():
    global eggs
    eggs = 'spam' # this is the global
    
def bacon():
    eggs = 'bacon' # this is a local
    Functions 71

def ham():
    print(eggs) # this is the global
    
eggs = 42 # this is the global
spam()
print(eggs)
