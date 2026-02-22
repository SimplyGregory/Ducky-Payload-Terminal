import socket
import pyautogui
import os
import sys
import subprocess

def execute_ducky_script(script):
    lines = script.splitlines()
    password_verified = False
    for line in lines:
        if line.startswith("PASSWORD"):
            input_password = line.split(" ", 1)[1]
            if input_password == "0000":
                password_verified = True
            else:
                print("Incorrect password. Canceling payload.")
                return
        elif password_verified:
            if line.startswith("DELAY"):
                delay_time = int(line.split(" ")[1])
                pyautogui.sleep(delay_time / 1000.0)
            elif line.startswith("STRING"):
                text = line.split(" ", 1)[1]
                pyautogui.typewrite(text)
            elif line.startswith("ENTER"):
                pyautogui.press('enter')
            elif line.startswith("ESCAPE"):
                pyautogui.press('escape')
            elif line.startswith("CLICK"):
                coords = line.split(" ", 2)[1:]
                x, y = int(coords[0]), int(coords[1])
                pyautogui.click(x, y)
            elif line.startswith("MOUSEMOVE"):
                coords = line.split(" ", 2)[1:]
                x, y = int(coords[0]), int(coords[1])
                pyautogui.moveTo(x, y)
            elif line.startswith("REM"):
                continue
            elif line.startswith("HOLD"):
                key = line.split(" ", 1)[1]
                pyautogui.keyDown(key)
            elif line.startswith("RELEASE"):
                key = line.split(" ", 1)[1]
                pyautogui.keyUp(key)
    print("Payload execution completed.")
    print("Waiting for a payload...")
    password_verified = False
def receive_Payload(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print("Waiting for a payload...")
        while True:
            conn, addr = s.accept()
            with conn:
                payload = conn.recv(1024).decode('utf-8')
                if not payload:
                    break
                print("Payload Received.")
                execute_ducky_script(payload)
    
if __name__ == "__main__":
    host = "0.0.0.0"
    port = 65432
    receive_Payload(host, port)
