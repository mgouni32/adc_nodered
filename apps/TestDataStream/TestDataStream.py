import paho.mqtt.client as paho
import time, os, io, sys, csv
from pathlib import Path
from collections import defaultdict

sample_flows = Path("/mqtt/Amann_Raw_epoch_csv_test").glob("*.csv")
client = paho.Client()
#client.on_connect = on_connect
client.connect("mqtt", 1883, 60)

for p in sample_flows:
    with open(str(p)) as afile:
        mereader = csv.DictReader(afile)
        for row in mereader:
            time.sleep(.05)
            #json = "{ \"ts\" : "+str(round(time.time()))+" , \"flow_rate\" : "+str(float(row["FlowRate [gal/min]"])) + " }"
            d = dict()
            d["ts"] = round(time.time())
            d["flow_rate"] = float(row["FlowRate [gal/min]"])
            client.publish("mqttSampleTopic",str(d))

client.disconnect()