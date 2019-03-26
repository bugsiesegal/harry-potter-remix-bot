from numpy import argmax
from numpy import array
from numpy import argmax
from keras.utils import to_categorical

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
def one_hot_encode(books,vocab):
    # One hot encodes what is put into it
    # define input string
    data = books
    # define universe of possible input values
    alphabet = vocab
    print(len(alphabet))
    # define a mapping of chars to integers
    char_to_int = dict((c, i) for i, c in enumerate(alphabet))
    int_to_char = dict((i, c) for i, c in enumerate(alphabet))
    # integer encode input data
    integer_encoded = [char_to_int[char] for char in data]
    # define example
    data = integer_encoded
    data = array(data)
#     print(data.shape)
#     print(data)
    # one hot encode
    encoded = to_categorical(data,num_classes=len(vocab))
    return encoded
def one_hot_decode(one_hot_encode, vocab):
    alphabet=vocab
    inverted = argmax(one_hot_encode)
    int_to_char = dict((i, c) for i, c in enumerate(alphabet))
    return int_to_char[int(inverted)]
def number_encode(vocab,data):
    characters = vocab
    char_to_n = {char:n for n, char in enumerate(characters)}
    listdata=list(data)
    intdata=[]
    for i in listdata:
        intdata.append(char_to_n[i])
    return intdata
def predict_text(model, X, n_to_char):
    string_mapped = X
    full_string = [n_to_char[value] for value in string_mapped]
    # generating characters
    for i in range(1000):
        x = np.reshape(string_mapped,(1,len(string_mapped), 1))
        x = x / float(len(characters))

        pred_index = np.argmax(model.predict(x, verbose=0))
        seq = [n_to_char[value] for value in string_mapped]
        full_string.append(n_to_char[pred_index])

        string_mapped.append(pred_index)
        string_mapped = string_mapped[1:len(string_mapped)]
    txt=""
    for char in full_string:
        txt = txt+char
    print(txt)
	

def make_loss_graph(fitmodel):
	history=fitmodel
	plt.plot(history.history['loss'])
	plt.plot(history.history['val_loss'])
	plt.title('model loss')
	plt.ylabel('loss')
	plt.xlabel('epoch')
	plt.legend(['train', 'test'], loc='upper left')
	plt.show()