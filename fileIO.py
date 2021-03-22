import re

data=""
with open('sample.txt','r') as file:
    data = file.read()
file.close()
    
keyword = input("Enter the keyword\n")

count = len(re.findall(keyword, data, re.IGNORECASE))
print(f'{keyword} occurs {count} times')

keyword_replace = input("Enter the new word\n")

text = re.sub(keyword, keyword_replace, data, flags=re.IGNORECASE)

with open('sample.txt','w') as file:
    file.write(text)

print("New text:\n",text)
file.close()