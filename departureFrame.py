from tkinter import Frame, GROOVE, Label, Checkbutton, E, W, NSEW

class DepartureFrame:
    def __init__(self, master, fields):
        self.frame = Frame(master, bd=2, relief=GROOVE)
        Label(self.frame, text="Departure Settings").grid(row=0, column=0, columnspan=3, sticky=W)
        Label(self.frame, text="Allow messages to leave the screen by:").grid(row=1, column=0, columnspan=3, sticky=W)

        self.CBOX_SLIDING_RIGHT = Checkbutton(self.frame, variable=fields.VAR_CHECK_SLIDING_RIGHT)
        self.CBOX_SLIDING_RIGHT.grid(row=2, column=0, sticky=E)
        Label(self.frame, text="Sliding right").grid(row=2, column=1, sticky=W)

        self.CBOX_SLIDING_LEFT = Checkbutton(self.frame, var=fields.VAR_CHECK_SLIDING_LEFT)
        self.CBOX_SLIDING_LEFT.grid(row=3, column=0, sticky=E)
        Label(self.frame, text="Sliding left").grid(row=3, column=1, sticky=W)

        self.CBOX_SLIDING_UP = Checkbutton(self.frame, var=fields.VAR_CHECK_SLIDING_UP)
        self.CBOX_SLIDING_UP.grid(row=4, column=0, sticky=E)
        Label(self.frame, text="Sliding up").grid(row=4, column=1, sticky=W)

        self.CBOX_SLIDING_DOWN = Checkbutton(self.frame, var=fields.VAR_CHECK_SLIDING_DOWN)
        self.CBOX_SLIDING_DOWN.grid(row=5, column=0, sticky=E)
        Label(self.frame, text="Sliding down").grid(row=5, column=1, sticky=W)

        self.CBOX_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT = Checkbutton(self.frame, var=fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT)
        self.CBOX_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT.grid(row=6, column=0, sticky=E)
        Label(self.frame, text="Alternating up/down working backwards").grid(row=6, column=1, sticky=W)

        self.CBOX_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT = Checkbutton(self.frame, var=fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT)
        self.CBOX_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT.grid(row=7, column=0, sticky=E)
        Label(self.frame, text="Alternating up/down working forwards").grid(row=7, column=1, sticky=W)

        self.CBOX_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER = Checkbutton(self.frame, var=fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER)
        self.CBOX_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER.grid(row=8, column=0, sticky=E)
        Label(self.frame, text="Alternating up/down, random order").grid(row=8, column=1, sticky=W)

        # self.CBOX_COVERING_WITH_RECTANGLES = Checkbutton(self.frame, var=fields.VAR_CHECK_COVERING_WITH_RECTANGLES)
        # self.CBOX_COVERING_WITH_RECTANGLES.grid(row=8, column=0)
        # Label(self.frame, text="Covering with rectangles").grid(row=8, column=1)

        self.frame.grid(row=0, column=0, sticky=NSEW, padx=4, pady=4)
