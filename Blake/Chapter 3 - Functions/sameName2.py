# sameName2 from Chapter 3

def spam():
    global eggs
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)
