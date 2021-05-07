import requests
import time
import os

webhook = input ('[~] Webhook; ')

def delete():
    requests.delete(webhook)

    check2 = requests.get(webhook)

    if check2.status_code == 404:
        print("Webhook successfully deleted.")
        time.sleep(999)
    elif check2.status_code == 200:
        print("Webhook failed to delete.")
        time.sleep(999)

check1 = requests.get(webhook)

if check1.status_code == 404:
    print("Invalid webhook has been passed.")
    time.sleep(999)
elif check1.status_code == 200:
    print("Webhook valid, deleting.")
    delete()

os.system("pause")
