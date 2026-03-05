#To reverse a String
print("Reversing a String")
string = "Hello world"
print(string[::-1])

#Python program to count vowel or consonant of the given string
print("Count vowels and consonants")
str=input("Please enter a string as you wish: ");
vowels=0
consonants=0
for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowels+1;#vowel counter is incremented by 1
    else:
        consonants=consonants+1;
#consonant counter is incremented by 1
print("The number of vowels:",vowels)
print("\nThe number of consonant:",consonants)

#Write a program to remove duplicates in a string.
print("To remove duplicates in a String")
text_str="hello hello how how are u u ?"
l = text_str.split() #split() returns a list.

temp = []
for x in l:
    if x not in temp:
        temp.append(x)
        
newlist= " ".join(temp) #join() returns a string.
print(newlist)

#Write a program using split
print("Another example using split")
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 2)

print(x)

#Write a program to count the number of words in a String
print("The number of words in a String")
countWords=len("How many words are here ?".split())
print(countWords)
countChar=len("How many words are here ?")
print(countChar)
print("Excluding space the number of characters or letters")
# Excluding space
text = "Number of characters in this text"
c=0
for i in text:
    if i==" ":
        c=c+1
print("No of characters without space : ",len(text)-c)   

#Python program to search a specific word in a string
print("To search a specific word in a String")
str = 'Check if string contains the required word?'
sub_index = str.find('contains')
print("The source string:" ,str)
print("The position of 'contains' word: ", sub_index)

#Write a program in Python to count lower, upper, numeric and special characters in a string.

str=input("Please enter a string: ")#take input from the user
upper, lower, num, special=0,0,0,0;#variable declaration and initilization
for i in range(len(str)):
  if(str[i]>='A' and str[i]<='Z'):#check upper case letters
     upper+=1
  elif(str[i]>='a' and str[i]<='z'):#check lower case letter
     lower+=1
  elif(str[i]>='1' and str[i]<='9'):#check numeric value
      num+=1
  else:
      special+=1
print("Upper case letters: ",upper)
print("\nLower case letters: ",lower)
print("\nnumbers: ",num)
print("\nSpecial characters: ",special)


