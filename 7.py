sen = input()
words = sen.split()
vowels = ['a','e','i','o','u']
cap =  ['A','E','I','O','U']
c=0
for i in range(0,len(words)):
    for j in range(0,len(vowels),):
            if(words[i][0]==vowels[j] or words[i][0]==cap[j]):
                 c=c+1
print(c)
