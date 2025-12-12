#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random

categories={
"fruits" : ['apple', 'banana', 'cherry', 'grape', 'orange', 'kiwi', 'mango', 'pineapple', 'strawberry', 'blueberry', 'pear', 'watermelon'],
"months" : ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
"cities" : ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'Austin', 'Seattle', 'Miami'],
"desserts" : ['ice cream', 'cake', 'pie', 'brownie', 'cookie', 'cupcake', 'cheesecake', 'pudding', 'gelato', 'macaron', 'tiramisu', 'donut'],
"animals" : ['lion', 'tiger', 'elephant', 'zebra', 'giraffe', 'kangaroo', 'panda', 'koala', 'wolf', 'bear', 'rabbit', 'fox']
}

print("WELCOME TO THE WORD GUESSING GAME.")
category_input=input("SELECT A CATEGORY: fruits, months, cities, desserts, animals\n").strip().lower()

if category_input in categories:
    word = random.choice(categories[category_input])
    word=word.lower()
    
else:
    print("Invalid category. Please restart the game.")
miss=5

print(f"""LETS BEGIN THE GAME. 
You have {miss} misses to guess the word from the category: {category_input}""")

unknown_word=[]
for i in range(len(word)):
    if word[i]==" ":
        unknown_word.append(" ")
    else:
        unknown_word.append("_")
guessed_letters=[]
while True:
    guess=input("Enter Letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():  
        print("Invalid input. Please enter a single letter.")
        continue
        
    if guess in guessed_letters:  
        print("You already guessed that letter!")
        continue
        
    guessed_letters.append(guess)
    count=0
    check=0
    for i in range(len(word)):
        if guess==word[i]:
            unknown_word[i]=guess
            count=1
            
            
    if count==0:
        miss -=1
        print(f"Wrong guess! You have {miss} misses left.")
        if miss==0:
            print("GAME OVER! You've used all your misses.")
            print(f"The word was: {word}")
            break
        
    elif count==1:
        print(f"Correct Guess!")
        
    for i in range(len(word)):
        if unknown_word[i]=="_":
            check=1
    if(check!=1):
        print("Current Guesses: ")
        for i in range(len(word)):
            print(unknown_word[i])
        print(f"Congratulations! You guessed the word: {word}")
        break
    
    print("Current Guesses: ")
    for i in range(len(word)):
        print(unknown_word[i])  


# In[ ]:




