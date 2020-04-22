from tkinter import Frame, GROOVE, Label, Checkbutton, E, W

class DepartureFrame:
    def __init__(self, master, fields):
        self.frame = Frame(master, bd=2, relief=GROOVE)

        ROW_DEPARTURE_SETTINGS = 0
        ROW_ALLOW_MESSAGES = 1
        ROW_SLIDING_RIGHT = 2
        ROW_SLIDING_LEFT = 3
        ROW_SLIDING_UP = 4
        ROW_SLIDING_DOWN = 5
        ROW_UP_DOWN_BACKWARDS = 6
        ROW_UP_DOWN_FORWARDS = 7
        ROW_RANDOM_ORDER = 8
        # ROW_RECTANGLES = 9

        Label(self.frame, text="Departure Settings").grid(row=ROW_DEPARTURE_SETTINGS, column=0, columnspan=3, sticky=W)
        Label(self.frame, text="Allow messages to leave the screen by:").grid(row=ROW_ALLOW_MESSAGES, column=0, columnspan=3, sticky=W)

        self.CBOX_SLIDING_RIGHT = Checkbutton(self.frame, variable=fields.VAR_CHECK_SLIDING_RIGHT)
        self.CBOX_SLIDING_RIGHT.grid(row=ROW_SLIDING_RIGHT, column=0, sticky=E)
        Label(self.frame, text="Sliding right").grid(row=ROW_SLIDING_RIGHT, column=1, sticky=W)

        self.CBOX_SLIDING_LEFT = Checkbutton(self.frame, var=fields.VAR_CHECK_SLIDING_LEFT)
        self.CBOX_SLIDING_LEFT.grid(row=ROW_SLIDING_LEFT, column=0, sticky=E)
        Label(self.frame, text="Sliding left").grid(row=ROW_SLIDING_LEFT, column=1, sticky=W)

        self.CBOX_SLIDING_UP = Checkbutton(self.frame, var=fields.VAR_CHECK_SLIDING_UP)
        self.CBOX_SLIDING_UP.grid(row=ROW_SLIDING_UP, column=0, sticky=E)
        Label(self.frame, text="Sliding up").grid(row=ROW_SLIDING_UP, column=1, sticky=W)

        self.CBOX_SLIDING_DOWN = Checkbutton(self.frame, var=fields.VAR_CHECK_SLIDING_DOWN)
        self.CBOX_SLIDING_DOWN.grid(row=ROW_SLIDING_DOWN, column=0, sticky=E)
        Label(self.frame, text="Sliding down").grid(row=ROW_SLIDING_DOWN, column=1, sticky=W)

        self.CBOX_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT = Checkbutton(self.frame, var=fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT)
        self.CBOX_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT.grid(row=ROW_UP_DOWN_BACKWARDS, column=0, sticky=E)
        Label(self.frame, text="Alternating up/down working backwards").grid(row=ROW_UP_DOWN_BACKWARDS, column=1, sticky=W)

        self.CBOX_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT = Checkbutton(self.frame, var=fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT)
        self.CBOX_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT.grid(row=ROW_UP_DOWN_FORWARDS, column=0, sticky=E)
        Label(self.frame, text="Alternating up/down working forwards").grid(row=ROW_UP_DOWN_FORWARDS, column=1, sticky=W)

        self.CBOX_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER = Checkbutton(self.frame, var=fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER)
        self.CBOX_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER.grid(row=ROW_RANDOM_ORDER, column=0, sticky=E)
        Label(self.frame, text="Alternating up/down, random order").grid(row=ROW_RANDOM_ORDER, column=1, sticky=W)

        # self.CBOX_COVERING_WITH_RECTANGLES = Checkbutton(self.frame, var=fields.VAR_CHECK_COVERING_WITH_RECTANGLES)
        # self.CBOX_COVERING_WITH_RECTANGLES.grid(row=ROW_RECTANGLES, column=0)
        # Label(self.frame, text="Covering with rectangles").grid(row=ROW_RECTANGLES, column=1)
