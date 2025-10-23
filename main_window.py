import tkinter as tk

class MainWindow:
    def __init__(self, master):
        self.master = master

        self.button = tk.Button(master, text="C", command=self.toggle_checklist_item)
        self.button.pack(anchor="nw")

        self.text_box = tk.Text(master)
        self.text_box.pack()
        self.text_box.focus_set()

        self.master.bind("<Control-F>", self.toggle_checklist_item)

        self.text_box.tag_configure("checklist", background="pink")
        self.text_box.tag_configure("checked", overstrike=True)
        self.text_box.tag_bind("checklist", "<Button-1>", self.toggle_checked)

    def toggle_checklist_item(self, event=None):
        # check if text is highlighted
        try:
            start = self.text_box.index("sel.first")
            end = self.text_box.index("sel.last")
        except tk.TclError:
            return

        #
        if "checklist" in self.text_box.tag_names("sel.first"):
            self.text_box.tag_remove("checklist", start, end)
        else:
            self.text_box.tag_add("checklist", start, end)

    def toggle_checked(self, event=None):
        index = self.text_box.index(f"@{event.x},{event.y}")
        tags = self.text_box.tag_names(index)

        if "checked" in tags:
            line_start = self.text_box.index(f"{index} linestart")
            line_end = self.text_box.index(f"{index} lineend")
            self.text_box.tag_remove("checked", line_start, line_end)
        else:
            line_start = self.text_box.index(f"{index} linestart")
            line_end = self.text_box.index(f"{index} lineend")
            self.text_box.tag_add("checked", line_start, line_end)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x375")
    app = MainWindow(root)
    root.mainloop()
