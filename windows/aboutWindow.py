import webbrowser
from tkinter import Button, W, Toplevel, Label, LEFT, PhotoImage, Frame, SE

class AboutWindow:
    def __init__(self, parent):
        self.aboutWindow = Toplevel(parent)
        self.aboutWindow.withdraw()
        self.aboutWindow.geometry('+{x}+80'.format(x=parent.winfo_x()))
        self.aboutWindow.wm_attributes("-topmost", 1)
        self.aboutWindow.focus_force()
        self.aboutWindow.iconbitmap("stIcon.ico")
        self.aboutWindow.title("About")
        self.aboutWindow.resizable(False, False)
        self.aboutWindow.grab_set()

        self.frameTop = Frame(self.aboutWindow)

        self.aboutImage = PhotoImage(file="imagefiles/stLogo64.png")
        self.aboutImageLabel = Label(self.frameTop, image=self.aboutImage)
        self.aboutImageLabel.grid(row=0, column=0, padx=4, pady=4)

        self.aboutLabel = Label(self.frameTop, text="StreamTicker\n\nVersion 2.0\n\nReleased: 4/20/2021", justify=LEFT)
        self.aboutLabel.grid(row=0, column=1, sticky=W, pady=4)

        self.frameTop.grid(row=0, column=0, sticky=W)

        self.aboutSupportLabel = Label(self.aboutWindow,
                                       text="Hello. I'm Go1den. I developed StreamTicker.\nI do not plan to charge for this program ever.\nIf you would like to support me:",
                                       justify=LEFT)
        self.aboutSupportLabel.grid(row=1, column=0, sticky=W, padx=4, columnspan=2)

        self.mySubscribeButton = Button(self.aboutWindow, text="Subscribe to my Twitch channel!", width=25,
                                        command=lambda: webbrowser.open('https://www.twitch.tv/products/go1den', new=2))
        self.mySubscribeButton.grid(row=2, column=0, columnspan=2, pady=4, padx=4)

        self.myWebsiteButton = Button(self.aboutWindow, text="Visit my website!", width=25, command=lambda: webbrowser.open('https://www.go1den.com', new=2))
        self.myWebsiteButton.grid(row=3, column=0, columnspan=2, pady=4, padx=4)

        self.aboutThanksLabel = Label(self.aboutWindow, text="Thank you so much for trying my program!\nIf you enjoy it, please tell others about it.", justify=LEFT)
        self.aboutThanksLabel.grid(row=4, column=0, sticky=W, pady=4, padx=4)

        self.okButton = Button(self.aboutWindow, text="OK", width=8, command=lambda: self.aboutWindow.destroy())
        self.okButton.grid(row=5, column=0, sticky=SE, pady=4, padx=4)

        self.aboutWindow.deiconify()
        self.aboutWindow.mainloop()
