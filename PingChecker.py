import subprocess
import tkinter as tk
hostname = "104.160.142.3"
font_size = 25


def get_ping():
    output = subprocess.Popen(
        ["ping.exe",hostname],
        stdout =subprocess.PIPE
    ).communicate()[0]
    output = output.decode()
    output = output[63:500]
    start = (output.index('time='))
    end = output.index('TTL')
    return output[start + 5:end - 3]


def main_loop():
    ping = int(get_ping())
    color = "lime"

    if ping > 999:
        ping = 999
        color = "red"
    elif ping > 100:
        color = "red"

    label.config(text=ping, fg=color)
    root.lift()
    root.after(100, main_loop)


root = tk.Tk()
root.title = "Ping"
root.wm_attributes("-topmost", 1)
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+100+-10".format(50, 50))
root.bind("<Button-1>", lambda evt: root.destroy())
root.attributes("-transparentcolor", "black")
root.configure(background='black')
label = tk.Label(text='', font=("Helvetica", font_size), bg="black")
label.pack(expand=True)


main_loop()
root.mainloop()