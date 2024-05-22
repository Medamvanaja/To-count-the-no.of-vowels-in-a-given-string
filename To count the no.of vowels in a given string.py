string="vanaja"
worldlist=string.split()
vowels=['a','e','i','o','u','A','E','I','O','U']
for word in worldlist:
    vowelCount=0
    for i in range(0,len(word)):
        if word[i] in vowels:
            vowelCount+=1
print("The word is", word, "and it contains", vowelCount, "vowels in it")        
