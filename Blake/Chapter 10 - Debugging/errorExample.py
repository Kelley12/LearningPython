import traceback

def spam():
    try:
        bacon()
    except:
        errorFile = open('errorInfo.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print(' The traceback info was written to errorInfo.txt')

def bacon():
    raise Exception("This is the error message")

spam()
