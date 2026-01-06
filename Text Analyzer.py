''''This is a menu-driven Text Analyzer built using Python.
It allows users to perform different string analysis operations like character count, word count, vowel count, palindrome check, and keyword search using a loop-based menu system.
Functions are used to make the code modular and reusable.'''

'''Concepts Used
✔ Functions
✔ while loop
✔ if-elif-else
✔ String methods
✔ User input'''

def char_count(text):
    print("characters(with spaces):",len(text))
    print("characters(without spaces):",len(text.replace(" ","")))

def word_count(text):
    words=text.split()
    print("Total words:",len(words))

def vowel_count(text):
    vowels="aeiouAEIOU"
    count=sum(1 for ch in text if ch in "aeiouAEIOU")
    for ch in text:
        if ch is vowels:
            count+=1
    print("Toatl Vowels:",count)      


def palindrome_check(text):
    cleaned=text.replace(" ","").lower() 
    if cleaned == cleaned[::-1]:
        print("It is a palindrome")
    else: 
        print("not a plaindrome") 


def keyword_search(text):
    keyword=input("enter keyword to search:")
    print("occurrences",text.count(keyword))
    pos=text.find(keyword)
    if pos!=-1:
        print("first position:",pos)
    else:
        print("keyword not find")    

#--------------Main Program----------------------------
text=input("enter the text:")

while True:
    print("\n---------------TEXT ANALYZER MENU-------------")
    print("1.Character Count")
    print("2.Word Count")
    print("3.vowel Count")
    print("4.Palindrome Check")
    print("5.keyword Search")
    print("6.Exit")
    print("-----------------------------")

    choice=int(input("enter your choice(1-6):"))

    if choice == 1:
        char_count(text)
    elif choice ==2:
        word_count(text)
    elif choice == 3:
        vowel_count(text)
    elif choice ==4:
        palindrome_check(text)
    elif choice ==5:
        keyword_search(text) 
    elif choice == 6:
        print("Existing text Analyzer . Thank Ypu!")
        break
    else:
        print("invalid choice! please selct 1-6")                   











