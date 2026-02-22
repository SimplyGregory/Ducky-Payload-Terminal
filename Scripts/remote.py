import socket
import time
import os
import sys

def send_payload(payload, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(payload.encode('utf-8'))


def hacker_loading_animation(duration=10):
    start_time = time.time()
    loading_chars = ['|', '/', '-', '\\']
    
    while time.time() - start_time < duration:
        for char in loading_chars:
            sys.stdout.write(f'\rLoading... {char}')
            sys.stdout.flush()
            time.sleep(0.2)


def Main_Function():
    os.system("cls")
    computer_name = socket.gethostname()
    print("\033[32m   'smmmmmmmmmmmmmmmmmmmmms.")
    print("  'ymmmmy/..+dmmmmmmmmmmmmmd:")
    print(" 'ommmh:'    -dmmmmmmmmmmmmmm-")
    print(" -dmmy.       +mmmmmy+/odmmmmy'")
    print("'ommy'        :mmm+'    .dmmmm'")
    print("'hmm+        'smd-      'ommmm.")
    print("'hmmmyo/-..-/ymms        /mmmy'")
    print(" -shdmmmmmmmmmmmd.       /mmm:")
    print("  '''.:dmmmmmmmmmmo.    'ommo")
    print("      'smmmmmmmmmmmmdo/-+mmo'")
    print("      :mmmmmmmmmmmsoshmmmh/")
    print("     'smmmmmmmmmm")
    print(" * * * Welcome to the Ducky Payload Terminal * * *")
    print("User: " + computer_name)
    print("Version: 1.5.8")
    print("")
    print("Type 'Start' to begin.")
    print("Type 'Quit' to exit terminal anytime.")

    started_program = False

    while True:
        user_input = input()
        
        if user_input.lower() == 'quit':
            print("Exiting terminal.")
            break
        if user_input.lower() == 'start' and started_program == False:
            started_program = True
            print("* * *")
            print("Type 'Target' to begin connection.")
            print("Type 'Find Targets(FT)' to scan for Targets.")

            user_input = input()
            if user_input.lower() == 'quit':
                print("Exiting terminal.")
                break
            if user_input.lower() == 'target':
                print("* * *")
                print("Target IP: ")
                TargetIP = input()
                TargetPort = 65432
                print("* * *")
                print("Payload path: ")

                Payload_PATH = input()
                if Payload_PATH.lower() == 'quit':
                    print("Exiting terminal.")
                    break
                try:
                    with open(Payload_PATH, 'r') as file:
                        payload_text = file.read()
                        hacker_loading_animation()
                        send_payload(payload_text, TargetIP, TargetPort)
                        sys.stdout.write('\rPayload Sent!\n')
                        time.sleep(5)
                        Main_Function()
                except FileNotFoundError:
                    sys.stdout.write('\rError: Payload not found.\n')
                    time.sleep(2)
                    Main_Function()
                except Exception as e:
                    sys.stdout.write('\rAn error occurred\n')
                    time.sleep(2)
                    Main_Function()


if __name__ == "__main__":
    Main_Function()
