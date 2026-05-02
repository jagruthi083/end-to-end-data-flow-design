import json, datetime
def log_event(event):
    with open("outputs/logs.json","a") as f:
        f.write(json.dumps({"event":event,"time":str(datetime.datetime.now())})+"\n")
