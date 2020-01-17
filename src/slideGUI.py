import tkinter as tk

def addNewSlide():
    print("%s%s%s" % (prefix.get(), text.get(), suffix.get()))

def previewMessage():
    preview.configure(text=prefix.get() + text.get() + suffix.get())

master = tk.Tk()
tk.Label(master, text="Message Prefix").grid(row=0, sticky=tk.E)
tk.Label(master, text="Message Text").grid(row=1, sticky=tk.E)
tk.Label(master, text="Message Suffix").grid(row=2, sticky=tk.E)
tk.Label(master, text="Use Twitch Bit icons").grid(row=3, sticky=tk.E)
tk.Label(master, text="Preview: ").grid(row=4, sticky=tk.E)

prefix = tk.Entry(master)
text = tk.Entry(master)
suffix = tk.Entry(master)
preview = tk.Label(master)
bits = tk.Checkbutton(master)
prefix.insert(0, "")
text.insert(0, "")
suffix.insert(0, "")

prefix.grid(row=0, column=1)
text.grid(row=1, column=1)
suffix.grid(row=2, column=1)
bits.grid(row=3, column=1)
preview.grid(row=4, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=5,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master, text='Show', command=addNewSlide).grid(row=5,
                                                         column=1,
                                                         sticky=tk.W,
                                                         pady=4)
tk.Button(master,
          text='Preview',
          command=previewMessage).grid(row=5,
                                       column=2,
                                       sticky=tk.W,
                                       pady=4)

master.mainloop()
tk.mainloop()
