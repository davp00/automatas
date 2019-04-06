from tkinter import Entry, StringVar


class Input (Entry):
    def __init__(self, frame, **kw):
        super().__init__(frame, **kw)
        self.value = StringVar()
        self.config(textvariable=self.value)

    def set_text(self, value):
        self.value.set(value)

    def get_text(self):
        return self.value.get()