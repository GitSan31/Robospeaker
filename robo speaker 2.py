import pyttsx3

e = pyttsx3.init()
e.setProperty('rate',120) #speech rate
e.setProperty('volume', 50)  #volume
voices = e.getProperty('voices')
e.setProperty('voice',voices[1].id)#change voice
print("Welcome to robot speaker by Sanskar")
e.say("Welcome to robot speaker by Sanskar")
e.runAndWait()

e.say("Enter speech rate(default is 120): ")
e.runAndWait()
rate = input("Enter speech rate(default is 120): ")
if rate:
    e.setProperty('rate', int(rate))

e.say("Enter speech volume(default is 50): ")
e.runAndWait()
volume = input("Enter speech volume(default is 50): ")


while True:
    x = input("Enter what you want me to say: ")
    if x=="q":
        e.say("Bye Bye friend")
        e.runAndWait()
        break

    e.say(x)
    e.runAndWait()










