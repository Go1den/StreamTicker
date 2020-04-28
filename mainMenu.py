import webbrowser
from tkinter import Menu

from aboutWindow import getAboutWindow
from messagesGUIWindow import getMessagesWindow
from settingsGUIWindow import getSettingsWindow

def getMainMenu(win, e):
    print("<------------")
    print(win.messages)
    print(win.messagesPath)
    print(win.settings)
    print(win.settingsPath)
    print("------------>")
    rmenu = Menu(e.widget.master, tearoff=0, takefocus=0)

    messagesMenu = Menu(rmenu, tearoff=0, takefocus=0)
    messagesMenu.add_command(label="Edit...", command=lambda: getMessagesWindow(win))
    messagesMenu.add_command(label="Load", command=lambda: win.loadMessages())
    messagesMenu.add_command(label="Save", command=lambda: win.saveMessages(False))
    messagesMenu.add_command(label="Save as...", command=lambda: win.saveMessages(True))
    messagesMenu.add_command(label="Erase All", command=lambda: win.clearMessages())

    settingsMenu = Menu(rmenu, tearoff=0, takefocus=0)
    settingsMenu.add_command(label="Edit...", command=lambda: getSettingsWindow(win))
    settingsMenu.add_command(label="Load", command=lambda: win.loadSettings())
    settingsMenu.add_command(label="Save", command=lambda: win.saveSettings(False))
    settingsMenu.add_command(label="Save as...", command=lambda: win.saveSettings(True))
    settingsMenu.add_command(label="Default")

    issueMenu = Menu(rmenu, tearoff=0, takefocus=0)
    issueMenu.add_command(label="via Discord", command=lambda: webbrowser.open('https://discord.gg/nqWxgHm', new=2))
    issueMenu.add_command(label="via Github", command=lambda: webbrowser.open('https://github.com/Go1den/StreamTicker/issues', new=2))

    rmenu.add_cascade(label="  Messages", menu=messagesMenu)
    rmenu.add_cascade(label="  Settings", menu=settingsMenu)
    rmenu.add_separator()
    rmenu.add_cascade(label="  Report Issue", menu=issueMenu)
    rmenu.add_separator()
    rmenu.add_checkbutton(label="  Always on Top", variable=win.alwaysOnTop, onvalue=True, offvalue=False, command=lambda: win.updateAlwaysOnTop())
    rmenu.add_command(label='  About StreamTicker', command=lambda: getAboutWindow(win))
    rmenu.add_command(label='  Exit', command=quit)
    rmenu.tk_popup(e.x_root + 74, e.y_root + 11, entry="0")
    return rmenu
