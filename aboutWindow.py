import webbrowser
from tkinter import Button, W, Toplevel, Label, LEFT, PhotoImage, Frame, SE

def getAboutWindow(parent):
    aboutWindow = Toplevel(parent)
    aboutWindow.wm_attributes("-topmost", 1)
    aboutWindow.focus_force()
    aboutWindow.iconbitmap("stIcon.ico")
    aboutWindow.title("About")
    aboutWindow.resizable(False, False)
    aboutWindow.grab_set()

    frameTop = Frame(aboutWindow)

    aboutImage = PhotoImage(file="imagefiles/stLogo64.png")
    aboutImageLabel = Label(frameTop, image=aboutImage)
    aboutImageLabel.grid(row=0, column=0, padx=4, pady=4)

    aboutLabel = Label(frameTop, text="StreamTicker\n\nVersion 2.0\n\nReleased: 4/20/2020", justify=LEFT)
    aboutLabel.grid(row=0, column=1, sticky=W, pady=4)

    frameTop.grid(row=0, column=0, sticky=W)

    aboutSupportLabel = Label(aboutWindow,
                              text="Hello. I'm Go1den. I developed StreamTicker.\nI do not plan to charge for this program ever.\nIf you would like to support me:",
                              justify=LEFT)
    aboutSupportLabel.grid(row=1, column=0, sticky=W, padx=4, columnspan=2)

    mySubscribeButton = Button(aboutWindow, text="Subscribe to my Twitch channel!", width=25, command=lambda: webbrowser.open('https://www.twitch.tv/products/go1den', new=2))
    mySubscribeButton.grid(row=2, column=0, columnspan=2, pady=4, padx=4)

    myWebsiteButton = Button(aboutWindow, text="Visit my website!", width=25, command=lambda: webbrowser.open('https://www.go1den.com', new=2))
    myWebsiteButton.grid(row=3, column=0, columnspan=2, pady=4, padx=4)

    aboutThanksLabel = Label(aboutWindow, text="Thank you so much for trying my program!\nIf you enjoy it, please tell others about it.", justify=LEFT)
    aboutThanksLabel.grid(row=4, column=0, sticky=W, pady=4, padx=4)

    okButton = Button(aboutWindow, text="OK", width=8, command=lambda: aboutWindow.destroy())
    okButton.grid(row=5, column=0, sticky=SE, pady=4, padx=4)

    aboutWindow.mainloop()
