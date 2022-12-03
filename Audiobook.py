import pyttsx3 as pt
book=open(r"New.txt")
book_text=book.readlines()
engine=pt.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()