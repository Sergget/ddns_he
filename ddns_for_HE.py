import requests
import json
import traceback
from datetime import datetime

def obCurrentTime():
    return "["+str(datetime.now())+"] "

# obtain public IP address from https://api.ipify.org
def check_ip():
    res = requests.get("https://api.ipify.org")
    if res.status_code==200:
        return res.text
    else:
        raise ConnectionError("cannot obtain IP, response code:"+res.text) 

def update_dns_record(ip,conf):
    for sub in conf["names"]:
        if ip and sub["name"] and sub["key"]:
            # print(conf["dynUrl"]+sub["name"]+"."+conf["TLD"]+"&password="+sub["key"]+"&myip="+ip)
            r=requests.get(conf["dynUrl"]+sub["name"]+"."+conf["TLD"]+"&password="+sub["key"]+"&myip="+ip)
            if r.text=="badauth":
                raise ConnectionRefusedError("Auth failed for ["+sub["name"]+"]: "+r.text)
            else:
                print(obCurrentTime()+r.text)
        elif not ip:
            raise ValueError("Empty IP!")
        else:
            raise ValueError("Invalid config")
try:
    with open ("./config.json") as f:
        conf=json.loads(f.read())
        update_dns_record(check_ip(),conf)
except FileNotFoundError:
    print(obCurrentTime()+"Config file not found: "+traceback.format_exc())
except ValueError:
    print(obCurrentTime()+traceback.format_exc())
except Exception:
    print(obCurrentTime()+"Error detected: "+traceback.format_exc())
