from tkinter import *

root =  Tk()

# root.geometry("200*530")

cursors = ["Arrow", "Circle" , " Target", "star" , "Spider" ,"heart" , "Pirate" ,"Plus" , "Man" ,
 "Sizing", "Tcross" , "Exchange" , "Fleur" , "Dotbox"]

for list in cursors:
    # print(list)
    Button(root, text=list, cursor=list).pack()

root.mainloop()
