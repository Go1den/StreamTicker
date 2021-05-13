import os
from tkinter import Toplevel, NSEW, E, messagebox

from api.challongeAPI import getTournamentInfo
from exceptions.challongeAPIException import ChallongeAPIException
from exceptions.noResultsMatchCriteriaException import NoResultsMatchCriteriaException
from frames.challongeFrame import ChallongeFrame
from frames.challongeOkCancelFrame import ChallongeOkCancelFrame
from utils.helperMethods import readJSON
from utils.stmGeneration import generateStmFile

class ChallongeWindow:
    def __init__(self, parent):
        self.master = Toplevel(parent)
        self.master.withdraw()
        self.parent = parent
        self.master.geometry('+{x}+{y}'.format(x=parent.winfo_x(), y=parent.winfo_y()))
        self.master.wm_attributes("-topmost", 1)
        self.master.focus_force()
        self.master.wm_title("StreamTicker Challonge Import")
        self.master.iconbitmap("imagefiles/stIcon.ico")
        self.master.resizable(False, False)
        self.master.grab_set()

        self.challongeFrame = ChallongeFrame(self)
        self.challongeFrame.frame.grid(row=0, padx=4, pady=4, sticky=NSEW)

        self.challongeOkCancelFrame = ChallongeOkCancelFrame(self)
        self.challongeOkCancelFrame.frame.grid(row=1, padx=4, pady=4, sticky=E)

        if not self.parent.settings.apiSettings.challongeUsername or not self.parent.settings.apiSettings.challongeAPIKey:
            messagebox.showerror("Error", "Missing Challonge username or API key. Did you add them in the Settings menu?", parent=self.master)
            self.master.destroy()
        else:
            self.master.deiconify()
            self.master.mainloop()

    def generateChallongeMessages(self, url: str, includeCompleted: bool, includeInProgress: bool, includeLosersBracket: bool, mostRecentRounds: int):
        try:
            tournamentInfo = getTournamentInfo(self.parent.settings.apiSettings.challongeUsername, self.parent.settings.apiSettings.challongeAPIKey, url, includeCompleted,
                                               includeInProgress, includeLosersBracket, mostRecentRounds)
            template = readJSON("messages/tournamentTemplate.stm")
            generatedFileLocation = generateStmFile(tournamentInfo, template)
            self.parent.load(os.getcwd() + "/" + generatedFileLocation)
            self.master.destroy()
        except NoResultsMatchCriteriaException:
            messagebox.showerror("Error", "No results matched the criteria.", parent=self.master)
        except ChallongeAPIException:
            messagebox.showerror("Error", "An attempt to get this tournament information from Challonge failed. Please verify your URL and Challonge settings.", parent=self.master)
        except Exception as e:
            messagebox.showerror("Error", "Unable to import data. Check that your API key and username are correct.", parent=self.master)
