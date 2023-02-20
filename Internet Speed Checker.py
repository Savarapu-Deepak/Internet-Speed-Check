# Python Program to check Internet Speed Checker.

from speedtest import Speedtest
import pyttsx3

speed = Speedtest()
download = speed.download()
download_speed_mbps = round(download / (10 ** 6))
upload = speed.upload()
upload_speed_mbps = round(download / (10 ** 6))

print(f'Download Speed : {download_speed_mbps} mb/s')
print(f'Upload Speed : {upload_speed_mbps} mb/s')

pyttsx3.speak(f'Your Download speed is  {download_speed_mbps} mb per second')
pyttsx3.speak(f'Your Upload Speed is  {upload_speed_mbps} mb per second')