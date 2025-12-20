import nltk
import random
import webbrowser
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

# Custom Chat class so Peter can trigger cutaways
class PeterChat(Chat):
    def respond(self, str):
        response = super().respond(str)

        # If the response contains a special trigger, open the link
        if response and "[CUTAWAY]" in response:
            url = "https://youtu.be/d2aeRg_yMSE?si=97HuOO0Alq7abc6n"
            webbrowser.open(url)
            print("Peter: Heheheheheheheh, here's Conway Twitty!!!")
            response = response.replace("[CUTAWAY]", "")

        return response


pairs = [
    [r"hi|hello|hey", [
        "Heheheheheheheh, hey there.",
        "Sweet!",
        "Oh Jeez, hey.",
        "Holy crap, you're back!"
    ]],

    [r"what is your name\??", [
        "I'm Peter Griffin. Hehehehehehehehehehehehehehehehehehehehehehehehehehe"
    ]],

    [r"how are you\??", [
        "Bird Is The Word.",
        "Shutup meg.",
        "I'm doing better than Joe after he fell down the stairs again."
    ]],

    [r"(.*) your favorite (.*)?", [
        "I have an idea so smart that my head would explode if I even began to know what I'm talking about."
    ]],

    [r"bye|exit|quit", [
        "Thanks for giving me an excuse not to talk to my daughter.",
        "Come on, let's go drink until we can't feel feelings anymore."
    ]],

    # Chaotic Peter-triggered cutaway
    [r"(.*)twitty(.*)", [
        "Oh this reminds me of that one time... [CUTAWAY]"
    ]],

    # Even more chaotic random cutaway
    [r"(.*)", [
        "Oh, my God, who the hell cares?",
        "You know what I haven't had in a while? Big League Chew.",
        "Welp, time to be hitting the old dusty trail.",
        "Why is there no hole in this wall?",
        "This reminds me of that one time I fought a giant chicken... [CUTAWAY]"
    ]]
]

chatbot = PeterChat(pairs, reflections)

print("Peter: Alright, time to go to the clam with the boys. Type 'quit' to leave this stupid program or whatever Brian said about AI.")

chatbot.converse()
