class Tokenizer:
    def __init__(self, vocabsize, data):
        self.vocabsize = vocabsize
        self.data = self.encode(data)
    def encode(self, text):
        final = []
        for i in text:
            final.append(ord(i))
        return final

    def bigram(self, encode):
        bi = []
        for index, j in enumerate(encode):
            if index+1 >= len(encode):
                break
            x = (j, encode[index+1])
            bi.append(x)
        return bi

    def frequency(self, bigram):
        counter = []
        for i in bigram:
            c = 0 
            for j in bigram:
                if i == j:
                    c += 1
            counter.append(c)
        return counter

    def __call__(self):
        vocabsize = self.vocabsize
        text = self.data
        old = text[:]
        dictionary = {}
        k = 256
        
        while len(dictionary) < vocabsize:
            bi = self.bigram(text)
            freq = self.frequency(bi)
            j = 0
            # Get indices sorted by descending values
            indices = sorted(range(len(freq)), key=lambda i: freq[i], reverse=True)
            while len(dictionary) <= vocabsize and j<len(bi): 
                if bi[indices[j]] in dictionary:
                    j += 1
                    continue
                else:
                    dictionary[bi[indices[j]]] = k
                    k += 1
                    j += 1
            newtext = self.merge(text, dictionary)
            
            if old == newtext:
                break
            else:
                text = newtext[:]
                old = newtext[:]
        return dictionary

    def merge(self, text, dictionary):
        i = 0
        new_text = []
        while i < len(text):
            if i < len(text) - 1 and (text[i], text[i+1]) in dictionary:
                new_text.append(dictionary[(text[i], text[i+1])])
                i += 2
            else:
                new_text.append(text[i])
                i += 1
        return new_text
