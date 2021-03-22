def tokenizer(sentence):
    return sentence.lower().split(" ")

def my_stemmer(wordlist):
    stemmer_data_set = {
        'know' : ('know', 'knows', 'knew', 'knowing'),
        'good' : ('good', 'nice', 'great'),
        'place' : ('place', 'places'),
        'nearby' : ('nearby', 'near')
    }
    result =[]
    for word in wordlist:
        for key, value in stemmer_data_set.items():
            if word in value:
                result.append(key)
    return result
    
def remove_stopwords(wordlist):
    stopwords = ['do', 'you', 'i', 'am', 'is', 'was']
    return [word for word in wordlist if word not in stopwords]

def remove_special_symbol(tokens):
    data_r = list()
    for word in tokens:
        a = ""
        for ch in word:
            if ch == '?' or ch == '!' or ch == '@' or ch == '.':
                continue
            else:
                a = a + ch
        data_r.append(a)
    return(data_r)
    
if __name__ == '__main__':
    data = "do you know good places nearby?"
    tokens = tokenizer(data)
    result1 = remove_special_symbol(tokens)
    result2 = remove_stopwords(result1)
    result3 = my_stemmer(result2)
    for s in result3:
        print(s)