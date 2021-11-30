Tutorial https://youtu.be/HOJsalRLnEQ
sudo su
 
apt update
apt install -y git build-essential libssl-dev libffi-dev python3-pip python3-dev python3-setuptools python3-venv 
 
adduser newbot
*************
 
whoami
su - newbot
whoami
 
git clone https://github.com/******/newrep
 
cd newrep/
ls -lh
nano newbot.py 
 
 
python3 -m venv .venv
ls -lah
cd
source /home/newbot/newrep/.venv/bin/activate
pip install -r /home/newbot/newrep/requirements.txt
 
/home/newbot/newrep/.venv/bin/python /home/newbot/newrep/newbot.py
 
exit
su - user
sudo su
whoami
 
cd /etc/systemd/system/
 
nano newbot.service
 
[Unit]
Description=My newbot
After=network.target
 
[Service]
User=newbot
Group=newbot
 
WorkingDirectory=/home/newbot/newrep/
Environment="PYTHONPATH=/home/newbot/newrep/"
ExecStart=/home/newbot/newrep/.venv/bin/python /home/newbot/newrep/newbot.py
 
[Install]
WantedBy=multi-user.target
 
sudo systemctl start newbot
sudo systemctl status newbot
sudo systemctl stop newbot
