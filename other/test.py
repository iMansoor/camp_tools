import pyautogui
import keyboard
import tkinter as tk
from tkinter import filedialog
import time

region_x = 800
region_y = 350
region_width = 1400
region_height = 1050

def screenshot_and_save():
    print("Hotkey detected. Starting Save dialog.")
    try:
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        print("Save dialog opening...")
        filepath = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            title="Save Screenshot As",
            parent=root
        )
        root.destroy()
        print(f"Dialog result: {filepath}")
        if filepath:
            print("Taking screenshot...")
            img = pyautogui.screenshot(region=(region_x, region_y, region_width, region_height))
            img.save(filepath)
            print(f"Screenshot saved: {filepath}")
        else:
            print("Save cancelled by user.")
    except Exception as e:
        print(f"ERROR: {e}")

print("Script running.")
print("Press PgDn to screenshot and save. Press ESC to exit.")

while True:
    if keyboard.is_pressed('page down'):
        print("PgDn pressed.")
        screenshot_and_save()
        while keyboard.is_pressed('page down'):
            time.sleep(0.1)
    if keyboard.is_pressed('esc'):
        print("ESC pressed. Exiting...")
        break
    time.sleep(0.05)
