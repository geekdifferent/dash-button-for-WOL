# dash-button-for-home-server
dash-button-for-home-server

For Raspberry PI
```
# m h  dom mon dow   command
@reboot sleep 10 && python /home/pi/.localbin/dash_button_redbull_to_wakeup.py >> /home/pi/.log/dash_button_redbull.txt 2>&1
```

For Home-Server
```
# m h  dom mon dow   command
@reboot sleep 10 && python /home/server/.localbin/dash_button_redbull_shutdown.py >> /home/server/.log/dash_button_redbull_shutdown.txt 2>&1
```
