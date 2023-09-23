import random
import re

# word="https://www.mit.edu/~ecprice/wordlist.10000"
# response=requests.get(word)
# words=response.content.splitlines()

lists={'fruits' :['banana', 'apple', 'orange', 'lemon', 'lime','strawberry', 'kiwi', 'peach', 'grape', 'pineapple', 'mango'],
       'vehicles':['car','van','bus','cycle','jeep','boart','palne','cart','lorry']}

print("*******************// Here it starts//***********************")

topics=list(lists.keys())
word=random.choice(topics)

print("Guess the Word!")
print(f"HINT: word is a name of a {word}")

if (word == topics[0]):
    frui=random.choice(lists["fruits"])
    replace=re.sub('[A-Za-z]','_',frui )
    print(replace)
    lists=list(frui)
    turn=list(replace)
    chances=len(frui)+2
    
    while chances >0:
        chances=chances-1
        user=input("Enter a letter to guess: ")
        if user.isalpha():
            if user in lists:
                position=(lists.index(user))
                turn[position]=user
                updated_name="".join(turn)
                print(updated_name)
            else:
                print("letter is not in the word")        
        else:
            print("Enter a letter not any charakter")
            continue
    print("your chances are over good bye😉")   
    print(f"And the letter is {frui} ")

if (word == topics[1]):
    vehi=random.choice(lists["vehicles"])
    replace=re.sub('[A-Za-z]','_',vehi)
    chances=len(vehi)+2
    print(replace)
    lists=list(vehi)
    turn=list(replace)  
    chances=len(vehi)+2
     
    while chances >0: 
        chances=chances-1
        user=input("Enter a letter to guess: ")
        if user.isalpha():
            if user in lists:
                position=(lists.index(user))
                turn[position]=user
                updated_name="".join(turn)
                print(updated_name)             
            else:
                print("letter is not in the word")        
        else:
            print("Enter a letter not any charakter")
            continue
    print("your chances are over good bye😉")   
    print(f"And the letter is {vehi} ")
