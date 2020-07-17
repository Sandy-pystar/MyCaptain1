freq = {} 
word=input("enter a string :") 
for i in word:
    if i in freq:
        freq[i] += 1
    else: 
        freq[i] = 1


print ("Frequency of characters :\n " +  str(freq))
print("Sorted in decreasing frequency :\n ")

for i in sorted(freq , key=freq.get ,  reverse=True):
    print(i , freq[i])

