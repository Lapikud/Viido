# Viido
Viido projektori arvuti repo

# Setup
Assuming you're using some debian derivative  
else ... figure it out yourself!

$CLONE is your repo clone path  
commands as #root

#### TODO: autostart
#
#### TODO: bin
#
#### nginx config
Install nginx ofc
```
mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak
ln -s $CLONE/nginx/default /etc/nginx/default
```
#
#### projektor
```
ln -s $CLONE/projektor /opt/projektor
apt install python3-serial python3-bottle
```
Optionally, set keyboard hotkeys from projektor/hotkey_commands.txt

#
#### web
```
mv /var/www/html /var/www/html.bak
ln -s $CLONE/www /var/www/html
```
#
#### noVNC
```
apt install novnc
ln -s /usr/share/novnc /var/www/noVNC
gsettings set org.gnome.Vino require-encryption false
dbus-launch gsettings set org.gnome.Vino prompt-enabled false
```
#
#### systemd services
```
ln -s $CLONE/systemd/projektor.service /etc/systemd/system/
systemctl enable projektor.service
systemctl start projektor.service
ln -s $CLONE/systemd/websockify.service /etc/systemd/system/
systemctl enable websockify.service
systemctl start websockify.service
```
#
Now, essential code seems to be symlinked and `git pull` keeps everything up-to-date..  
  
  And as always, this readme is under destruction :)
