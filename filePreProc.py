from translate import Translator

def tokenizer(text):
    text2 = text.lower()
    words = text2.split('|')
    return words

def extract(text):
    return text.split(" ")

def extract_reviews(text):
    for line in text:
        print(line, '\n')

def delstopwords(table):
    stopwords = ['i', 'me', 'my', 'myself', 'our', 'ours', 'ourselves','it','is', 'its', 'itself', 'they', 'them', 'their', 'theirs',
                 'themselves', 'what', 'which', 'you', "you're", "you've", "you'll",
                 "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's",
                 'her', 'hers', 'herself', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is',
                 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did',
                 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'while', 'of', 'at',
                 'by', 'any' ,'for', 'with', 'about', 'between', 'into',"shouldn't", "wasn't", "weren't", 
                 "won't", "wouldn't"]
    temp=[]
    for word in table.keys():
        if word in stopwords:
            temp.append(word)
    for word in temp:
        table.pop(word)
    return table

def mkcollection(text):
    words = []
    for line in text:
        words.extend(extract(tokenizer(line)[1]))
    return words

def mkdict(words):
    table = {}
    for word in words:
        table[word] = words.count(word)
    return table

def translate_all(table):
    translate = Translator(to_lang = 'hi')
    dict1 = {}
    for word in table.keys():
        dict1[word] = translate.translate(word)
    return dict1

if __name__ == "__main__":
    text = open('reviews.txt')
    words = mkcollection(text)
    text.close()
    table = mkdict(words)
    table2 = delstopwords(table)
    table3 = translate_all(table2)
    text = ""
    for word in table3.keys():
        text = text + word + " : " + table3[word] + "\n"
    print(text)