import json
import os
import tkinter
import tkinter.filedialog

window = tkinter.Tk()
window.geometry("500x500")
def process_button_clicked():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*'),
    )
    file_name = tkinter.filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes,
    )
    process(file_name)
process_button = tkinter.Button(window, text="Process", command=process_button_clicked)
process_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def process(file_name):
    pools = []

    with open(file_name) as f:
        lines = f.read().splitlines()

    for line in lines:
        item_name, amount, chance = line.split()
        pools.append({
            "rolls": {
                "type": "minecraft:binomial",
                "n": int(amount),
                "p": float(chance),
            },
            "entries": [
                {
                    "type": "minecraft:item",
                    "name": item_name,
                }
            ]
        })

    base, _ext = os.path.splitext(file_name)
    with open(base + ".json", "w") as f:
        json.dump({
            "pools": pools,
        }, f, indent=4)

window.mainloop()
