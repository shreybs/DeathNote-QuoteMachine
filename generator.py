from tkinter import *
import tkinter.messagebox
import json
import random
import platform

if(platform.system() == 'Windows'):
    import winsound

#JSON String of all quotes and characters below. Skip to Line 114 for the tkinter part.
quotes='''{
  "quotes": [
    {
      "quote": "This world is rotten, and those who are making it rot deserve to die. Someone has to do it, so why not me?",
      "character": "Light Yagami"
    },
    {
      "quote": "The real evil is the power to kill people. Someone who finds himself with that power is cursed. No matter how you use it, anything obtained by killing people can never bring true happiness.",
      "character": "Soichiro Yagami"
    },
    {
      "quote": "When you die, I'll be the one writing your name in my Death Note.",
      "character": "Ryuk"
    },
    {
      "quote": "I am justice!",
      "character": "Light Yagami and L Lawliet"
    },
    {
      "quote": "I’ll take a potato chip AND EAT IT!",
      "character": "Light Yagami"
    },
    {
      "quote": "We've eased each other's boredom for quite a while... It's been quite fun.",
      "character": "Ryuk"
    },
    {
      "quote": "Yagami-san, if I die in the next few days, your son is Kira.",
      "character": "L Lawliet"
    },
    {
      "quote": "Kira is childish and he hates losing... I am also childish and I hate to lose. That's how I know.",
      "character": "L Lawliet"
    },
    {
      "quote": "This has gotta be the longest 40 seconds of my life.",
      "character": "Light Yagami"
    },
    {
      "quote": "If Kira gets caught, he is evil. If Kira rules the world, he is justice.",
      "character": "Light Yagami"
    },
    {
      "quote": "Hear this: I'm not only Kira, but I'm also God of the new world!",
      "character": "Light Yagami"
    },
    {
      "quote": "If you can't win the game, if you can't solve the puzzle, then you're nothing but a loser.",
      "character": "Nate River"
    },
    {
      "quote": "He who strikes first wins.",
      "character": "L Lawliet"
    },
    {
      "quote": "Having finally made his dream reality, he was overwhelmed both by the magnitude of his achievement and by the joy and happiness that it brought him.",
      "character": "Light Yagami"
    },
    {
      "quote": "You're just a murderer, Light Yagami. And this notebook is the deadliest weapon of mass murder in the history of mankind.",
      "character": "Nate River"
    },
    {
      "quote": "Don't worry, Commander Rester, making assumptions is part of any investigation. If we're wrong, all it'll cost is an apology.",
      "character": "Nate River"
    },
    {
      "quote": "In all things, one cannot win with defense alone. To win, you must attack.",
      "character": "Light Yagami"
    },
    {
      "quote": "An eye for an eye my friend",
      "character": "L Lawliet"
    },
    {
      "quote": "Light, my son… from one murderer to another, I'll see you in hell.",
      "character": "Soichiro Yagami"
    },
    {
      "quote": "You can call me what you like, but I will be taking your cake.",
      "character": "L Lawliet"
    },
    {
      "quote": "I'll solve equations with my right hand and write names with my left. I'll take a potato chip... and EAT IT!!",
      "character": "Light Yagami"
    },
    {
      "quote": "Look around you, and all you see are people the world would be better without.",
      "character": "Light Yagami"
    },
    {
      "quote": "I'll kill anyone who gets in my way. I'll be number one.",
      "character": "Mihael Keehl"
    },
    {
      "quote": "Humans are interesting!",
      "character": "Ryuk"
    },
    {
      "quote": "Delete!",
      "character": "Teru Mikami"
    }
  ]
}'''

quoteList=json.loads(quotes)


class Generator:
    def __init__(self, master):
        # GUI Window properties here
        tkinter.messagebox.showinfo('Credits','Made by Shreyas BS for fun purposes. I do not own nor am I affiliated with the Death Note Franchise including the anime and manga series.')
        master.title("Death Note Quote Machine")
        master.geometry("1000x600")
        master.resizable(False,False)
        background_image = PhotoImage(file='background.png')
        #w = background_image.width()
        #h = background_image.height()
        #master.geometry("%dx%d+0+0" % (w, h))
        
        #Widgets from here
        panel1 = Label(master, image=background_image)
        panel1.pack(side='top', fill='both', expand='yes')
        panel1.image = background_image
        i = 1

        buttonFont=('Helvetica',15,'bold')
        generateButton= Button(master, text = "Generate Quote", bd = 6, bg='red', fg='white',height=1,width=15, command = lambda: generateQuotes(i))
        #generateButton.grid(columnspan=3,row=5,pady=5)
        #generateButton.pack(side="bottom",fill=X)
        generateButton.configure(font=buttonFont)
        generateButton.place(x=390,y=530)
       
        quoteFont=('Courier New',14,'bold')
        characterFont=('Courier',14,'bold')
        mainQuote= Label(master,fg='white',bg='black',wraplength=920,justify=CENTER, text=" ")
        mainQuote.configure(font=quoteFont)
        mainQuote.place(x=500,y=400,anchor='center')
        character = Label(master,fg='white',bg='black',justify=CENTER, text=" ")
        character.configure(font=characterFont)
        character.place(x=550,y=450)
        
        def generateQuotes(i):
            number = random.randint(1,25)
            mainQuote.config(text="\" "+quoteList['quotes'][number]['quote']+" \"") 
            character.config(text="- "+quoteList['quotes'][number]['character']+".")           

        



root = Tk()

root.wm_iconbitmap('favicon.ico')

if(platform.system()=='Windows'):
    winsound.PlaySound('death_music.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
    
mainProgram = Generator(root)

root.mainloop()
