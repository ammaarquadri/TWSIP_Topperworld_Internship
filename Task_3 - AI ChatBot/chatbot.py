# Meet Robo: your friend

# Import necessary libraries
import io
import random
import string  # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
from tkinter import *

nltk.download('popular', quiet=True)  # for downloading packages

# Uncomment the following only the first time
# nltk.download('punkt')  # first-time use only
# nltk.download('wordnet')  # first-time use only

# Reading in the corpus
with open('chatbot.txt', 'r', encoding='utf8', errors='ignore') as fin:
    raw = fin.read().lower()

# Tokenisation
sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)  # converts to list of words

# Preprocessing
lemmer = WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Additional responses
CONVERSATION_INPUTS = ("how are you", "what are you doing", "tell me a joke", "bye", "thank you", "thanks","Fine" 
                       "who are you", "where are you from", "what is your name", "what can you do")
CONVERSATION_RESPONSES = {
    "how are you": ["I'm fine, thank you. How about you?", "Doing great! And you?", "I'm good! How are you?"],
    "Fine" : ["Glad to hear that !"],
    "what are you doing": ["I'm here to chat with you!", "Just chatting with you. What about you?", "Waiting to answer your queries!"],
    "tell me a joke": ["Why don’t scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!", "What do you get when you cross a snowman and a vampire? Frostbite!"],
    "bye": ["Bye! Take care..", "Goodbye! Have a nice day!", "See you later!"],
    "thank you": ["You are welcome!", "No problem!", "My pleasure!"],
    "thanks": ["You are welcome!", "No problem!", "My pleasure!"],
    "who are you": ["I'm Robo, your friendly chatbot!", "I am just a chatbot designed to chat with you!", "I'm an AI chatbot created to assist you!"],
    "where are you from": ["I exist in the digital world!", "I'm wherever you need me to be.", "I'm from the land of ones and zeros!"],
    "what is your name": ["You can call me Robo!", "I'm known as Robo in this chat.", "My name is Robo!"],
    "what can you do": ["I can chat with you, answer your questions, and tell jokes!", "I'm here to help with any questions or just to chat!", "I'm designed to engage in conversations and provide information!"]
}

def conversation(sentence):
    """If user's input matches any conversation input, return an appropriate response"""
    for key in CONVERSATION_INPUTS:
        if key in sentence:
            return random.choice(CONVERSATION_RESPONSES[key])


# Generating response
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response


# Creating the GUI
def send():
    user_input = user_entry.get()
    chat_window.insert(END, "You: " + user_input + "\n")
    user_input = user_input.lower()
    if user_input != 'bye':
        if user_input == 'thanks' or user_input == 'thank you':
            chat_window.insert(END, "ROBO: " + conversation(user_input) + "\n")
        else:
            if greeting(user_input) is not None:
                chat_window.insert(END, "ROBO: " + greeting(user_input) + "\n")
            elif conversation(user_input) is not None:
                chat_window.insert(END, "ROBO: " + conversation(user_input) + "\n")
            else:
                chat_window.insert(END, "ROBO: " + response(user_input) + "\n")
                sent_tokens.remove(user_input)
    else:
        chat_window.insert(END, "ROBO: " + conversation('bye') + "\n")
        user_entry.delete(0, END)
        return
    user_entry.delete(0, END)

# Setting up the main window
root = Tk()
root.title("Robo Chatbot")
root.geometry("400x500")

# Creating the chat window
chat_window = Text(root, bd=1, bg="white", width=50, height=8, font=("Arial", 12))
chat_window.place(x=6, y=6, height=385, width=370)

# Creating the scrollbar
scrollbar = Scrollbar(root, command=chat_window.yview)
chat_window['yscrollcommand'] = scrollbar.set
scrollbar.place(x=375, y=5, height=385)

# Creating the entry box
user_entry = Entry(root, bd=0, bg="white", width=29, font=("Arial", 12))
user_entry.place(x=6, y=400, height=88, width=300)

# Creating the send button
send_button = Button(root, text="Send", width=12, height=5, bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff', command=send)
send_button.place(x=310, y=400, height=88)

root.mainloop()
