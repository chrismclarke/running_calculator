#!/usr/bin/python3
'''
Possible distances: 100, 200, 400, 800, 1500, Mile, 5k, 10k, HM, Mar
'''

import numpy as np
import lmc

fields = ('Distance 1', 'Performance 1', 'Distance 2', 'Performance 2',\
             'Distance 3', 'Performance 3','Distance to Predict', 'Predicted Performance')

def portal_to_prediction(x,data,tbc):
    conf = {}
    conf['gender'] = 'Male'
    conf['percentiles'] = [0,25]
    conf['no_events_tried'] = 3
    conf['outlier_threshold'] = 0.05
    x = np.log(x)
    y = np.zeros((x.shape[0]+1,x.shape[1]))
    y[:-1,:] = x
    y[-1,:] = np.log(data)
    tobecompleted = np.zeros(y.shape)
    tobecompleted[-1,:] = tbc
    method_conf = {}
    method_conf['distances'] = np.load('distances.npy')
    method_conf['alg_iterations'] = 5000
    method_conf['r'] = 3
    predicted = lmc.lmc(y,tobecompleted,method_conf)
    return np.exp(predicted[-1,np.where(tbc)[0][0]])

def convert_to_seconds(time):
    hms = time.split(':')
    if len(hms)==1:
        return float(hms[0])
    elif len(hms)==2:
        return float(hms[0])*60+float(hms[1])
    elif len(hms)==3:
        return float(hms[0])*(60*60)+float(hms[1])*60+float(hms[2])
    else:
        raise ValueError

def convert_to_time(seconds):
    hours = int(seconds)/3600
    minutes = int(seconds)/60-hours*60
    seconds = seconds-minutes*60-hours*(60*60)
    return '%g:%02d:%05.2f' % (int(hours), int(minutes), float(seconds))

if __name__ == '__main__':
    pass
