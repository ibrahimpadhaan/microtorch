text = "This is Gada"
text = "The quick brown fox jumps over the lazy dog. The fox was very quick and clever. Every animal in the forest admired the fox for its speed and wit. However, the dog was not amused. He thought the fox was showing off. But in the end, the fox and the dog became good friends."
text = list(text)
encode = []
for i in text:
    encode.append(ord(i))

def bigram(encode):
    bi = []
    for index, j in enumerate(encode):
        if index+1 >= len(encode):
            break
        x = (j, encode[index+1])
        bi.append(x)
    return bi

def frequency(bigram):
    counter = []
    for i in bigram:
        c = 0 
        for j in bigram:
            if i == j:
                c += 1
        counter.append(c)
    return counter

def makeTokens(vocabsize, text):
    dictionary = {}
    bi = bigram(text)
    freq = frequency(bi)
    # Get indices sorted by descending values
    indices = sorted(range(len(freq)), key=lambda i: freq[i], reverse=True)
    k = 255
    j = 0
    while len(dictionary) <= vocabsize and j<len(bi):
        if bi[indices[j]] in dictionary:
            j += 1
            continue
        dictionary[bi[indices[j]]] = k
        k += 1
        j += 1
    return dictionary

def merge(text, dictionary):
    for i in dictionary:
        for index, j in enumerate(text):
            if index+1 >= len(text):
                break
            if i == (j, text[index+1]):
                text[index: index+2] = [dictionary[i]]
    return text
