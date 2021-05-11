from tkinter import Frame, GROOVE, Label, W, Entry, E

from objects.settingsGUIFields import SettingsGUIFields

class SettingsAPIFrame:
    def __init__(self, master, fields: SettingsGUIFields):
        self.fields = fields
        self.frame = Frame(master, bd=2, relief=GROOVE)

        ROW_API_SETTINGS = 0
        ROW_DIMENSIONS = 1

        Label(self.frame, text="API Settings").grid(row=ROW_API_SETTINGS, column=0, columnspan=3, sticky=W)

        self.frameDimensions = Frame(self.frame)
        self.labelChallongeUsername = Label(self.frameDimensions, text="Challonge.com Username:")
        self.labelChallongeUsername.grid(row=0, column=0, sticky=E, pady=1)
        self.entryChallongeUsername = Entry(self.frameDimensions, textvariable=self.fields.VAR_CHALLONGE_USERNAME, width=50)
        self.entryChallongeUsername.grid(row=0, column=1, sticky=W, pady=1)

        self.labelChallongeAPIKey = Label(self.frameDimensions, text="Challonge.com API Key:")
        self.labelChallongeAPIKey.grid(row=1, column=0, sticky=E, pady=1)
        self.entryChallongeAPIKey = Entry(self.frameDimensions, textvariable=self.fields.VAR_CHALLONGE_API_KEY, width=50)
        self.entryChallongeAPIKey.grid(row=1, column=1, sticky=W, pady=1)

        self.labelSmashggAPIKey = Label(self.frameDimensions, text="Smash.gg API Key:")
        self.labelSmashggAPIKey.grid(row=2, column=0, sticky=E, pady=1)
        self.entrySmashggAPIKey = Entry(self.frameDimensions, textvariable=self.fields.VAR_SMASHGG_API_KEY, width=50)
        self.entrySmashggAPIKey.grid(row=2, column=1, sticky=W, pady=1)
        self.frameDimensions.grid(row=ROW_DIMENSIONS, sticky=W, pady=1)
