import webbrowser
from tkinter import Menu

from windows.aboutWindow import AboutWindow
from windows.messageManagerWindow import MessageManagerWindow
from windows.settingsWindow import SettingsWindow

def getMainMenu(win, e):
    rmenu = Menu(e.widget.master, tearoff=0, takefocus=0, bg="#ffffff")

    messagesMenu = Menu(rmenu, tearoff=0, takefocus=0, bg="#ffffff")
    messagesMenu.add_command(label="Edit...", command=lambda: MessageManagerWindow(win))
    messagesMenu.add_command(label="Load", command=lambda: win.loadMessages())
    messagesMenu.add_command(label="Save", command=lambda: win.saveMessages(False))
    messagesMenu.add_command(label="Save as...", command=lambda: win.saveMessages(True))
    messagesMenu.add_command(label="Default", command=lambda: win.loadDefaultMessages())

    settingsMenu = Menu(rmenu, tearoff=0, takefocus=0, bg="#ffffff")
    settingsMenu.add_command(label="Edit...", command=lambda: SettingsWindow(win))
    settingsMenu.add_command(label="Load", command=lambda: win.loadSettings())
    settingsMenu.add_command(label="Save", command=lambda: win.saveSettings(False))
    settingsMenu.add_command(label="Save as...", command=lambda: win.saveSettings(True))
    settingsMenu.add_command(label="Default", command=lambda: win.loadDefaultSettings())

    issueMenu = Menu(rmenu, tearoff=0, takefocus=0, bg="#ffffff")
    issueMenu.add_command(label="via Discord", command=lambda: webbrowser.open('https://discord.gg/nqWxgHm', new=2))
    issueMenu.add_command(label="via Github", command=lambda: webbrowser.open('https://github.com/Go1den/StreamTicker/issues', new=2))

    rmenu.add_cascade(label="  Messages", menu=messagesMenu)
    rmenu.add_cascade(label="  Settings", menu=settingsMenu)
    rmenu.add_separator()
    rmenu.add_checkbutton(label="  Always on Top", variable=win.alwaysOnTop, onvalue=True, offvalue=False, command=lambda: win.updateAlwaysOnTop())
    rmenu.add_separator()
    rmenu.add_cascade(label="  Report Issue", menu=issueMenu)
    rmenu.add_command(label='  Check for Updates', command=lambda: win.checkForUpdates())
    rmenu.add_separator()
    rmenu.add_command(label='  About', command=lambda: AboutWindow(win))
    rmenu.add_command(label='  Exit', command=lambda: win.closeWindow())
    rmenu.tk_popup(e.x_root + 68, e.y_root + 11, entry="0")
    return rmenu
