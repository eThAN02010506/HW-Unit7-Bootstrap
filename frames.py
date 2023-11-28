import ttkbootstrap as tb
from ttkbootstrap.constants import *
from K import *
import requests as req

class ButtonGroup(tb.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=PM, pady=PM, fill=X)

        self.submit_button = tb.Button(self, text="Submit", bootstyle=SUCCESS)
        self.cancel_button = tb.Button(self, text="Cancel", bootstyle=(OUTLINE, SECONDARY))

        self.submit_button.pack(side=RIGHT, padx=(PM, 0))
        self.cancel_button.pack(side=RIGHT)



class searchBar(tb.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack(padx=PM, pady=(0,PM), fill=BOTH,expand=True)
        self.searchBar = tb.Entry(self)

        self.search = tb.Button(self, text="Search", commnad=self.search_for_record())
        # self.label_text = "search Results"
        self.label_text = tb.StringVar(value="")
        self.searchBar.pack(side=LEFT,fill=X,expand=True)
        self.search.pack(side=LEFT, padx=(PXS,0))
        self.searchResult = tb.Label(self,
                                textvariable=self.label_text,
                                     font=LEAD,
                                     justify=CENTER
                               )
        self.searchResult.pack(expand=True,
                              padx=PM, pady=PM, side=BOTTOM)
    def search_for_record(self):
        name = self.searchBar.get()
        if len(name) < 1:
            self.label_text.set(value="Error\n No query given")
            # self.label_text = "Error\n No query given"
            # self.searchResult.configure(text="No query for search")
        else:
            print(name)
            url_string = f"http://10.6.21.76:8000/names/{name}"
            response = req.get(url_string)
            print(name)
            if "msg" in response:
                # self.searchResult.configure(text=response["msg"])
                self.label_text.set(value="msg")
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

        self.title = tb.Label(
            self,
            text="SMIC RECORDS",
            font=DISPLAY4,


        )
        subtitle = "Subtitle!!!"
        # appearance of 2nd label
        self.subtitle = tb.Label(
            self,
            textvariable=subtitle,
            font=H1,



        )


        #self.search = searchBar(self)

        self.title.pack(padx=20,
                              pady=20,
                              anchor=W)
        self.subtitle.pack(padx=30,
                                 anchor=W)

        # self.search.pack(anchor=W, pady=(0, PM), padx=PM)
        self.search = searchBar(self)

        self.Buttons = ButtonGroup(self)
        #self.button_group = ButtonGroup(self)
        #self.button_group_1 = ButtonGroup(self)

if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()

