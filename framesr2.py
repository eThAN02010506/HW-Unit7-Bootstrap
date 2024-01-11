import ttkbootstrap as tb
from ttkbootstrap.constants import *
import requests as req
from K import *


class FrameManager:
    def __init__(self):
        self.frame1 = ButtonGroup()
        self.frame2 = SearchBarGroup()

    def show_frame(self, frame):
        if frame == "frame1":
            self.frame1.pack(fill="both", expand=True)
            self.frame2.pack_forget()
        elif frame == "frame2":
            self.frame2.pack(fill="both", expand=True)
            self.frame1.pack_forget()


class ButtonGroup(tb.Frame):
    def __init__(self):
        super().__init__()
        self.submit_button = tb.Button(self, text="Submit", bootstyle=SUCCESS)
        self.cancel_button = tb.Button(self, text="Cancel", bootstyle=(OUTLINE, SECONDARY))

        self.submit_button.pack(side="right", padx=5)
        self.cancel_button.pack(side="right")

        self.switch_button = tb.Button(
            self, text="Switch to SearchBar", command=lambda: frame_manager.show_frame("frame2")
        )
        self.switch_button.pack(side="left")


class SearchBarGroup(tb.Frame):
    def __init__(self):
        super().__init__()
        self.search_entry = tb.Entry(self)
        self.search_button = tb.Button(self, text="Search", command=self.search_for_record)

        self.search_entry.pack(side="left", expand=True, padx=5)
        self.search_button.pack(side="left")

        self.search_result_label = tb.Label(self, text="", font=("Helvetica", 12))
        self.search_result_label.pack(pady=10)

    def search_for_record(self):
        name = self.search_entry.get()
        if len(name) < 1:
            self.search_result_label.config(text="Error: No query given")
        else:
            url_string = f"http://10.6.21.76:8000/academics/{name}"
            response = req.get(url_string).json()
            if "msg" in response:
                self.search_result_label.config(text=response["msg"])
            else:
                response_string = f"Name: {response['name']}\nChance to fail: {response['chance to fail']}\nGPA: {response['gpa']}"
                self.search_result_label.config(text=response_string)


if __name__ == "__main__":
    app = App(theme="minty")
    app.place_window_center()
    app.mainloop()
