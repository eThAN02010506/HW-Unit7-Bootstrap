import ttkbootstrap as tb
from ttkbootstrap.constants import *
import requests as req
from K import *

class ButtonGroup(tb.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=PM, pady=PM, fill=X)

        self.submit_button = tb.Button(self, text="Submit", bootstyle=SUCCESS)
        self.cancel_button = tb.Button(self, text="Cancel", bootstyle=(OUTLINE, SECONDARY))

        self.submit_button.pack(side=RIGHT, padx=(PM, 0))
        self.cancel_button.pack(side=RIGHT)

class searchBar(tb.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=PM, pady=(0, PM), fill=BOTH, expand=True)
        self.searchBar = tb.Entry(self)

        self.search = tb.Button(self, text="Search", command=self.search_for_record)
        self.label_text = tb.StringVar(value="")
        self.searchBar.pack(side=LEFT, fill=X, expand=True)
        self.search.pack(side=LEFT, padx=(PXS, 0))
        self.searchResult = tb.Label(
            self,
            textvariable=self.label_text,
            font=LEAD,
            justify=CENTER
        )
        self.searchResult.pack(expand=True, padx=PM, pady=PM, side=BOTTOM)

    def search_for_record(self):
        name = self.searchBar.get()
        if len(name) < 1:
            self.label_text.set(value="Error\n No query given")
        else:
            print(name)
            # Assume self.url_string is defined somewhere
            url_string = f"{self.url_string}{name}"
            response = req.get(url_string).json()
            print(name)
            if "msg" in response:
                self.label_text.set(value=response["msg"])
            else:
                response_string = f"""
                Name: {response["name"]}
                Chance to fail: {response["chance to fail"]}
                GPA: {response["gpa"]}
                """
                self.label_text.set(value=response_string)
                self.searchResult.configure(text=response_string)
            print(response)

class App(tb.Window):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("Frames")

        self.current_frame = "search"

        self.switch_frame_button = tb.Button(
            self,
            text="Switch Frame",
            command=self.switch_frame
        )
        self.switch_frame_button.pack(pady=10)

        self.title_label = tb.Label(
            self,
            text="SMIC RECORDS",
            font=DISPLAY4,
        )
        self.subtitle_label = tb.Label(
            self,
            text="Subtitle!!!",
            font=H1,
        )

        self.title_label.pack(padx=20, pady=20, anchor=W)
        self.subtitle_label.pack(padx=30, anchor=W)

        self.search = searchBar(self)
        self.Buttons = ButtonGroup(self)
        self.frames = {
            "search": self.search,
            "buttons": self.Buttons
        }
        self.set_frame()

    def set_frame(self):
        self.frames[self.current_frame].pack(fill=BOTH, expand=True)

    def remove_frame(self):
        self.frames[self.current_frame].pack_forget()

    def switch_frame(self):
        if self.current_frame == "search":
            self.remove_frame()
            self.current_frame = "buttons"
        else:
            self.remove_frame()
            self.current_frame = "search"
        self.set_frame()

if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()
