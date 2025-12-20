import nltk
import random
import string
import webbrowser

from nltk.chat.util import Chat, reflections

# needs the NLTK data downloaded, only for the first time though
nltk.download('punkt')

# define pairs
pairs = [
    [r"hi|hello|hey", ["Heheheheheheheh,", "Sweet!", "Oh Jeez,", "Holy crap!"]],
    [r"what is your name\??", ["I'm Peter Griffin. Hehehehehehehehehehehehehehehehehehehehehehehehehehe"]],
    [r"how are you\??", ["Bird Is The Word.", "Shutup meg."]],
    [r"(.*) your favorite (.*)?", ["I have an idea so smart that my head would explode if I even began to know what I'm talking about."]],
    [r"bye|exit|quit", ["Thanks for giving me an exuse to not to talk to my daughter.", "Come on, let's go drink until we can't feel feelings anymore."]],
    [r"why are you like this\??", ["Now I may be an idiot, but there's one thing I am not sir, and that sir, is an idiot"]],
    [r"whats your view on AI\??", ["Gosh, It's Not Like The Internet To Go Crazy About Something Small And Stupid.", "Whoa, Whoa... Lois, This Is Not My Batman Glass."]],
    [r"do you think of life and death\??", ["I've spontaneously combusted. And its quite alright, I grown tired of living... IS IT RAINING AGAIN?!!"]],
    [r"(.*)", ["Oh, my God, who the hell cares?", "You know what I haven't had in a while? Big League Chew.", "Welp, Time to be hitting the old dusty trail.", "Why is there no hole in this wall?"]]
]

chatbot = Chat(pairs, reflections)

print("Alright, time to go to the clam with the boys. You could type 'quit' to exit to leave this stupid program or whatever Brain said about AI. Can't remember, maybe if I had a few beers, I'll remember. Probably not, but here's Conway Twitty!!!")

url = "https://youtu.be/d2aeRg_yMSE?si=97HuOO0Alq7abc6n"
webbrowser.open(url)
print(f"Opened the video in your web browser: {url}")

chatbot.converse()
