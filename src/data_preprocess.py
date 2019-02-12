

def loaddata(path, numbooks):
# basicly just joins all of the books together
    books=""
    for i in range(numbooks):
        with open(path+str(i+1)+".txt","r", errors='ignore') as f:
            books=books + f.read() + "\n" 
    return books
	
def remove_impuritys(books):
#the name says it all it takes the bad things and grinds them up we leave the good things intact
    return books.replace("\n","").lower()
