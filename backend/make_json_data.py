#!/usr/bin/env python

import datetime
import csv
import sqlite3 as lite
import json
#import sys

db_file = 'data/d2.sqlite'
#csv_file = 'data/map.csv'
#head_file = 'data/html/head.html'
#tail_file = 'data/html/tail.html'

####
#process acre_data
####
def get_acre_data(ts):
    query = ' SELECT TimeString, WS, lat, lon, acT, mph, speed, course, width, ts FROM acre_data '
    query = query + ' ORDER BY ABS ( ? - ts ) LIMIT 1 '
    data = (ts,)
    cur.execute(query,data)
    row = cur.fetchone()
    return row


#####
#create_json
#####
def create_json(point_lst,prod):
    out = []
    for inx,point in enumerate(point_lst):
        print('point',inx,point)
        out_dic = {}
        lat = point['alat']
        out_dic['lat'] = lat
        lon = point['alon']
        out_dic['lon'] = lon
        name = str(prod) + str(inx+1)
        out_dic['name'] = name
        out_dic['key'] = str(name).replace(' ','_') + str(lat) + str(lon)
        out.append(out_dic)

    with open('data/' + str(prod).replace(' ','_') + '.json','w') as f:
        json.dump(out, f, indent=4)
        #f.write(out)

    return out
       

####
#main
####

#SELECT * FROM products ;
#5   Canola
#6   L340PC Canola
#7   B3020 Canola
#8   L330PC B 4.8TSW Canola
#9   L330PC A4.8TSW Canola
#10  L330PC A4.2TSW Canola
#11  L333PC Canola

#SELECT TimeString, WS, lat, lon, acT, mph, speed, course, width, ts FROM acre_data ORDER BY id desc limit 1;



#SELECT TimeString, prod, prod_id, deere_cal, lbsT, source, ts FROM meter_data ORDER BY id desc limit 10;
#max(ts)           min(ts)
#1758992155000253  1743643450000665

max_ts = 1758992155000253
min_ts = 1743643450000665
freq = 0.1
prod_id_lst = [5,6,7,8,9,10,11]
prod_id_lst = [6]

con = lite.connect(db_file)
con.row_factory = lite.Row
with con:
    cur = con.cursor()

    query = 'SELECT m.TimeString, m.prod, m.prod_id, m.deere_cal, m.lbsT, m.source, m.frequency, m.label, m.ts, p.product FROM meter_data AS m '
    query = query + ' JOIN products AS p ON m.prod_id = p.id '
    query = query + ' WHERE m.ts > ? AND m.ts < ? AND m.frequency > ? AND m.prod_id IN ( '
    data_lst = [min_ts,max_ts,freq]
    for inx,item in enumerate(prod_id_lst):
        data_lst.append(item)
        if inx == 0:
            query = query + ' ? '
        else:
            query = query + ' ,? '
    query = query + ' ) '
    data = tuple(data_lst)
    cur.execute(query,data)
    rows = cur.fetchall()
    lat_sum = 0
    lon_sum = 0
    l_count = 0
    out = []
    for row in rows:
        out_dic = {}
        for key in row.keys():
            out_dic['m'+key] = row[key]
        a_dic = get_acre_data(row['ts'])
        for key in a_dic.keys():
            out_dic['a'+key] = a_dic[key]

        out_dic['delta_ts'] = out_dic['mts'] - out_dic['ats']
        
        if out_dic['alat'] and out_dic['alon']:
            lat_sum = lat_sum + out_dic['alat']
            lon_sum = lon_sum + out_dic['alon']
            l_count = l_count + 1
            out_dic['count'] = l_count
            out.append(out_dic)

lat_cen = lat_sum / l_count
lon_cen = lon_sum / l_count
print('center ',lat_cen,lon_cen,l_count)
prod = out_dic['mproduct']

print('out_dic',out_dic)
p_data = create_json(out,prod)

print(p_data)

#        for key in out_dic.keys():
#            print ('key',key,'data',out_dic[key])
#        choice = input('enter')

