import webbrowser
from tkinter import W, Toplevel, Label, LEFT, PhotoImage, Frame, SE, GROOVE

from utils.hoverButton import HoverButton

class AboutWindow:
    def __init__(self, parent):
        self.aboutWindow = Toplevel(parent)
        self.aboutWindow.withdraw()
        self.aboutWindow.geometry('+{x}+{y}'.format(x=parent.winfo_x(), y=parent.winfo_y()))
        self.aboutWindow.wm_attributes("-topmost", 1)
        self.aboutWindow.focus_force()
        self.aboutWindow.iconbitmap("imagefiles/stIcon.ico")
        self.aboutWindow.title("About")
        self.aboutWindow.resizable(False, False)
        self.aboutWindow.grab_set()

        self.frameTop = Frame(self.aboutWindow)

        self.aboutImage = PhotoImage(file="imagefiles/stLogo64.png")
        self.aboutImageLabel = Label(self.frameTop, image=self.aboutImage)
        self.aboutImageLabel.grid(row=0, column=0, padx=4, pady=4)

        self.aboutLabel = Label(self.frameTop, text="StreamTicker\n\nVersion 3.0.0\n\nReleased: 6/24/2024", justify=LEFT)
        self.aboutLabel.grid(row=0, column=1, sticky=W, pady=4)

        self.frameTop.grid(row=0, column=0, sticky=W)

        self.aboutSupportLabel = Label(self.aboutWindow,
                                       text="Hello. I'm Go1den. I developed StreamTicker.\nThis program is available to use for free.\nThat being said, I devoted many hours to it.\n\nPlease consider supporting me if you enjoy it:",
                                       justify=LEFT)
        self.aboutSupportLabel.grid(row=1, column=0, sticky=W, padx=4, columnspan=2)

        self.myPaypalImage = PhotoImage(file="imagefiles/donate.png")
        self.myPaypalButton = Label(self.aboutWindow, image=self.myPaypalImage, cursor="hand2")
        self.myPaypalButton.bind("<Button-1>", lambda x: webbrowser.open('https://www.paypal.com/donate/?hosted_button_id=LXMBXT59KL578', new=2))
        self.myPaypalButton.grid(row=2, column=0, columnspan=2, pady=4, padx=4)

        self.aboutThanksLabel = Label(self.aboutWindow, text="Thank you so much for trying my program!\nIf you enjoy it, please tell others about it.", justify=LEFT)
        self.aboutThanksLabel.grid(row=3, column=0, sticky=W, pady=4, padx=4)

        self.okButton = HoverButton(self.aboutWindow, text="OK", width=10, bd=2, relief=GROOVE, command=lambda: self.aboutWindow.destroy())
        self.okButton.grid(row=4, column=0, sticky=SE, pady=4)

        self.aboutWindow.deiconify()
        self.aboutWindow.mainloop()
