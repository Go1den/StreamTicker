import sys
import webbrowser
from tkinter import Menu, filedialog

from aboutWindow import getAboutWindow
from settingsGUIWindow import getSettingsWindow

def loadMessages():
    fileToLoad = filedialog.askopenfilename(initialdir=sys.argv[0], title="Load messages", filetypes=[("StreamTicker Messages", "*.stm")])
    if not fileToLoad or fileToLoad is None:
        return
    else:
        print(fileToLoad)

def loadSettings():
    fileToLoad = filedialog.askopenfilename(initialdir=sys.argv[0], title="Load settings", filetypes=[("StreamTicker Messages", "*.sts")])
    if not fileToLoad or fileToLoad is None:
        return
    else:
        print(fileToLoad)

def getMainMenu(e):
    rmenu = Menu(e.widget.master, tearoff=0, takefocus=0)

    messagesMenu = Menu(rmenu, tearoff=0, takefocus=0)
    messagesMenu.add_command(label="Edit...")
    messagesMenu.add_command(label="Load", command=lambda: loadMessages())

    settingsMenu = Menu(rmenu, tearoff=0, takefocus=0)
    settingsMenu.add_command(label="Edit...", command=lambda: getSettingsWindow())
    settingsMenu.add_command(label="Load", command=lambda: loadSettings())
    issueMenu = Menu(rmenu, tearoff=0, takefocus=0)
    issueMenu.add_command(label="via Discord", command=lambda: webbrowser.open('https://discord.gg/nqWxgHm', new=2))
    issueMenu.add_command(label="via Github", command=lambda: webbrowser.open('https://github.com/Go1den/StreamTicker/issues', new=2))

    rmenu.add_cascade(label="  Messages", menu=messagesMenu)
    rmenu.add_cascade(label="  Settings", menu=settingsMenu)
    rmenu.add_separator()
    rmenu.add_cascade(label="  Report Issue", menu=issueMenu)
    rmenu.add_separator()
    rmenu.add_command(label='  About StreamTicker', command=lambda: getAboutWindow())
    rmenu.add_command(label='  Exit', command=quit)
    rmenu.tk_popup(e.x_root + 74, e.y_root + 11, entry="0")
    return rmenu
