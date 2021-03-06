# -*- coding: utf-8 -*-
import json
import time
import datetime
import random

# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Array dei canali 
channels = [1, 2]

# Classe contenente le chiavi per la creazione del JSON
class KeysConstant(object):
    def __init__(self):
        pass    

    key_payload = "payload"
    key_address = "address"
    key_qos = "qos"
    key_values = "values"
    key_timestamp = "timestampDevice"

# Classe per la memorizzazione di una singola misura
class Measure(object):
    def __init__(self, channel, value, timestamp, count=1):
        self.channel = channel
        self.value = value
        self.timestamp = timestamp
        self.read = 0
        self.average = 0
        self.json = 0
        self.count = count

# Classe per la gestione delle liste misura
class MeasureList(object):
    def __init__(self):
        pass

    global kc
    plist = []

    # Aggiunge alla lista una misura dati i valori
    def add_details(self, channel, value, timestamp):
        meas = Measure(channel, value, timestamp)
        self.plist.append(meas)

        # Aggiunge alla lista una misura
    def add_measure(self, meas):
        self.plist.append(meas)

    # Ritorna lista delle misure per singolo canale
    def list_by_channel(self, channel):
        part_list = []
        for meas in self.plist:
            if ((meas.channel == channel) & (meas.read == 0)):
                part_list.append(meas)
                meas.read = 1
        return part_list

   # Ritorna lista delle misure per singolo canale e stato
    def json_dictionary(self):
        dic_list = []
        for meas in self.plist:
            elem_dic = {}
            if (meas.json == 0):
                elem_dic[kc.key_payload] = meas.value
                elem_dic[kc.key_address] = meas.channel
                elem_dic[kc.key_timestamp] = meas.timestamp
                elem_dic[kc.key_qos] = "good"
                dic_list.append(elem_dic)
                meas.json = 1
        return dic_list

    # Ritorna media delle misure per singolo canale e stato
    def avg_by_channel(self, channel):

        # Numero misure contate
        val_count = 0
        val_tot = 0
        val_ts = 0
        val_avg = 0

        # Estraggo le misure e calcolo la media
        for meas in self.plist:
            if ((meas.channel == channel) & (meas.average == 0)):
                if (val_ts == 0):
                    val_ts = meas.timestamp
                val_count = val_count + 1
                val_tot = val_tot + meas.value
                meas.average = 1

        # Calcolo la media delle ultime misure
        if (val_count > 0):
            val_avg = val_tot / val_count
        else:
            val_avg = 0

        meas_avg = Measure(channel, val_avg, val_ts, val_count)

        return meas_avg

    # Elimina gli elementi processati
    def clear_list(self):
        for meas in self.plist:
            if (meas.json == 1):
                self.plist.remove(meas)

    # Ritorna la lista completa
    def list(self):
        return self.plist

   # Classe per eseguire la calibrazione iniziale
class Calibration(object):

    def __init__(self, sensor, pcycles=5, pmin=0, pmax=100):
        self.sensor = sensor
        self.pcycles = pcycles
        self.pmin = pmin
        self.pmax = pmax

    def calibrate(self):

        avg_temp = 0
        calib = 1

        # Avvio fase di calibrazione iniziale: la temperatura media risulta
        # da una media di 5 rilevazioni della temperatura ambiente
        print("Calibrating Sensor: <" + self.sensor + ">")

        while (calib <= self.pcycles):
            avg_temp = avg_temp + sense.get_temperature()
            print ("Calibration [" + str(calib) + "]: <" + str(avg_temp / calib) + ">")
            calib = calib + 1
            time.sleep(1)

        avg_temp = avg_temp / self.pcycles
        print ("Avg: <" + str(avg_temp)+ ">")

        # Fisso i valori di riferimento del range di temperatura
        # (+/- 1C rispetto alla temperatura di calibrazione)
        self.pmax = avg_temp + 1
        self.pmin = avg_temp - 1
        print ("Min: <" + str(self.pmin)+ ">; Max: <" +str(self.pmax)+ ">")




    # Genero il JSON
    main_dic = {}
    main_dic[kc.key_timestamp] = time.time()
    main_dic[kc.key_qos] = "good"
    main_dic[kc.key_values] = measure_list.json_dictionary() 
               


# Write JSON file
with io.open('./MQTT/message.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(mainData,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))






