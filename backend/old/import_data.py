#!/usr/bin/env python

import datetime
import csv
import sqlite3 as lite
import sys

db_file = 'data/d2.sqlite'
csv_file = 'data/d2acres.20250401.20250630.canola.csv'

#row  ['TimeString', '2025-05-01 00:45:00.000', 'channel', '25', 'cnt', '270.0', 'cnt_act', '0', 'count', '0', 'countT', '9873547.0', 'deere_act', '1', 'deere_cal', '3.5382', 'end_cnt', '300', 'frequency', '0.0000', 'interval', '5.000000', 'label', 'd1c1m3', 'lbs', '0.0', 'lbsT', '188806.29176240787', 'lbscal', '18', 'lbsmin', '0.0', 'lbspulse', '0.030664400000001174', 'lbspulse1', '0.030664400000001174', 'lbspulse2', '0.0', 'lbspulse_cnt', '0.06666666666666667', 'lbspulse_deere', '0.030664400000001174', 'lbssec', '0.0', 'one', '1', 'prod', 'Canola', 'source', 'deere', 'str_cnt', '30', 'total', '0', 'ts', '1746060299999926']

#keys dict_keys(['TimeString', 'channel', 'cnt', 'cnt_act', 'count', 'countT', 'deere_act', 'deere_cal', 'end_cnt', 'frequency', 'interval', 'label', 'lbs', 'lbsT', 'lbscal', 'lbsmin', 'lbspulse', 'lbspulse1', 'lbspulse2', 'lbspulse_cnt', 'lbspulse_deere', 'lbssec', 'one', 'prod', 'source', 'str_cnt', 'total', 'ts'])


#TimeString,2025-04-03 07:18:56.635,S1,1.0,S2,0.0,S3,0.0,S4,0.0,S5,1.0,S6,1.0,WS,0.0,ac,0.0,acA,0.0,acT,0.0006595841847231198,achr,0.0,achrA,0.0,achrs,0.0,acmile,5.252525252525243,acmin,0.0,acs,0.0,acsT,0.9942695488334968,d2c1fL_sp,49,d2c2fU_sp,51,duration,26077.768159,interval,5,inthr,0.0013888889,lastInputString,04/03/2025 00:04:18,lastInputTime,1743638658866507,mph,0.0,name,los,one,1,s123456ama,2.6262626262626214,s1234w,29.166666666666668,s12w,14.166666666666668,s1am,0.9090909090909074,s1ama,0.9090909090909074,s1w,7.5,s2am,0.8080808080808066,s2ama,0.0,s2w,6.666666666666667,s3456ama,1.717171717171714,s3am,0.9090909090909074,s3ama,0.0,s3w,7.5,s4am,0.9090909090909074,s4ama,0.0,s4w,7.5,s56am,1.717171717171714,s56ama,1.717171717171714,s5am,0.8080808080808066,s5ama,0.8080808080808066,s5w,6.666666666666667,s6am,0.9090909090909074,s6ama,0.9090909090909074,s6w,7.5,speed,0,timestring,04/03/2025 07:18:56,ts,1743664736634666,width,43.333333333333336


####
#check if product exists
####
def get_product_id(prod):
    query = 'SELECT * FROM products WHERE product = ? '
    data = (prod,)
    cur.execute(query,data)
    out = cur.fetchone()
    if out != None:
        prod_id = out['id']
    else:
        query = 'INSERT INTO products (product) VALUES (?) '
        #data = (prod,)
        cur.execute(query,data)
        prod_id = cur.lastrowid
    return prod_id


####
#get id from ts
####
def get_ts_id(ts,table):
    query = 'SELECT * FROM ' + table + ' WHERE ts = ? '
    data = (ts,)
    cur.execute(query,data)
    out = cur.fetchone()
    if out != None:
        return out['id']
    return None


####
#write data
####
def write_table_data(data_dic,table):
    query = 'INSERT INTO ' + table + ' ( '
    data_lst = []
    for inx,key in enumerate(data_dic.keys()):
        data_lst.append(data_dic[key])
        if inx == 0:
           query = query + key
           qmarks = '?'
        else:
           query = query + ', ' + key
           qmarks = qmarks + ', ?'
    query = query + ') VALUES ( '
    query = query + qmarks + ') '
    #print('query',query)
    #print('data',data_lst)
    data = tuple(data_lst)
    cur.execute(query,data)
    row_id = cur.lastrowid
    return row_id


####
#process meter_data
####
def process_meter_data(row_dic):
    row_dic['prod_id'] = 0
    try:
        prod = row_dic['prod']
    except:
        print('Error no prod ')
    else:
        row_dic['prod_id'] = get_product_id(prod)
        row_dic.pop('prod')
    try:
        ts = row_dic['ts']
    except:
        print('Error no ts')
    else:
        existing_id = get_ts_id(ts,'meter_data')

        if existing_id:
            print('ts already entered')
        else:
            meter_data_id = write_table_data(row_dic,'meter_data')
            print('meter_data_id', meter_data_id)
    return


####
#process gps_data
####
def process_gps_data(row_dic):
    try:
        ts = row_dic['ts']
    except:
        print('Error no ts')
    else:
        existing_id = get_ts_id(ts,'gps_data')

        if existing_id:
            print('ts already entered')
        else:
            gps_data_id = write_table_data(row_dic,'gps_data')
            print('gps_data_id', gps_data_id)
    return


####
#process acre_data
####
def process_acre_data(row_dic):
    try:
        ts = row_dic['ts']
    except:
        print('Error no ts')
    else:
        existing_id = get_ts_id(ts,'acre_data')

        if existing_id:
            print('ts already entered')
        else:
            acre_data_id = write_table_data(row_dic,'acre_data')
            print('acre_data_id', acre_data_id)
    return


####
#main
####
csv_file = sys.argv[1]
print('csv_file',csv_file)

type_lst = ['mph','WS','prod']

err_str = False

if err_str:
    print('Error: ',err_str)
else:
    con = lite.connect(db_file)
    con.row_factory = lite.Row
    with con:
        cur = con.cursor()

        with open(csv_file,newline='',encoding='utf-8') as f:
            #rows = csv.reader(f,delimiter=';',quotechar='"')
            rows = csv.reader(f,delimiter=',')
            for row in rows:
                row_dic = {}
                for inx,item in enumerate(row):
                    if (inx % 2) == 0:
                        key = item
                    else:
                        row_dic[key] = item

                if 'prod' in row_dic.keys():
                    process_meter_data(row_dic)
                elif 'WS' in row_dic.keys():
                    process_acre_data(row_dic)
                else:
                    process_gps_data(row_dic)
                #    print('cannot find table for data')


