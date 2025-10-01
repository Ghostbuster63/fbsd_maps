#!/usr/bin/env python

#keys dict_keys(['TimeString', 'channel', 'cnt', 'cnt_act', 'count', 'countT', 'deere_act', 'deere_cal', 'end_cnt', 'frequency', 'interval', 'label', 'lbs', 'lbsT', 'lbscal', 'lbsmin', 'lbspulse', 'lbspulse1', 'lbspulse2', 'lbspulse_cnt', 'lbspulse_deere', 'lbssec', 'one', 'prod', 'source', 'str_cnt', 'total', 'ts'])



#TimeString, S1, S2, S3, S4, S5, S6, WS, ac, acA, acT, achr, achrA, achrs, acmile, acmin, acs, acsT, d2c1fL_sp, d2c2fU_sp, duration, interval, inthr, lastInputString, lastInputTime, mph, name, one, s123456ama, s1234w, s12w, s1am, s1ama, s1w, s2am, s2ama, s2w, s3456ama, s3am, s3ama, s3w, s4am, s4ama, s4w, s56am, s56ama, s5am, s5ama, s5w, s6am, s6ama, s6w, speed, timestring, ts, width


#   TimeString, ac, achr, acmile, d2c1fL_sp, d2c2fU_sp, duration, interval, inthr, lastInputString, lastInputTime, mph, name, s1234w, s12w, s1am, s1w, s2am, s2w, s3am, s3w, s4am, s4w, s56am, s5am, s5w, s6am, s6w, speed, timestring, ts, width

#TimeString,2025-04-04 19:43:05.174,ac,0.00036245359419077844,achr,0.2624069374090662,acmile,5.252525252525243,altMSL,781.4570,alt_ft,2563.8353018372677,altitude,781.4570,count,25,course,198.9000,d2c1fL_sp,49,d2c2fU_sp,51,interval,4.972555,inthr,0.0013812652888279,lat,50.511233142500,latitude,50.511233142500,lon,-110.212089430500,longitude,-110.212089430500,mph,0.04995824385288,s1234w,29.166666666666668,s12w,14.166666666666668,s1am,0.9090909090909074,s1w,7.5,s2am,0.8080808080808066,s2w,6.666666666666667,s3am,0.9090909090909074,s3w,7.5,s4am,0.9090909090909074,s4w,7.5,s56am,1.717171717171714,s5am,0.8080808080808066,s5w,6.666666666666667,s6am,0.9090909090909074,s6w,7.5,source,GGA,speed,0.0804,total,2.0100,track,198.9000,ts,1743795785173593,width,43.333333333333336


import sqlite3 as lite

db_file = 'data/d2.sqlite'
con = lite.connect(db_file)

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS gps_data")
    cur.execute(''' CREATE TABLE gps_data
        (id integer primary key autoincrement,
        TimeString text,
        ac float,
        achr float,
        acmile float,
        altMSL float,
        alt_ft float,
        altitude float,
        count integer,
        course float,
        duration float,
        d2c1fL_sp float,
        d2c2fU_sp float,
        interval float,
        inthr float,
        lastInputString text,
        lastInputTime float,
        lat float,
        latitude float,
        lon float,
        longitude float,
        mph float,
        name text,
        s1234w float,
        s12w float,
        s1am float,
        s1w float,
        s2am float,
        s2w float,
        s3am float,
        s3w float,
        s4am float,
        s4w float,
        s56am float,
        s5am float,
        s5w float,
        s6am float,
        s6w float,
        source text,
        speed float,
        total float,
        track float,
        ts integer,
        width float
        );''')


    cur.execute("DROP TABLE IF EXISTS acre_data")
    cur.execute(''' CREATE TABLE acre_data
        (id integer primary key autoincrement,
        TimeString text,
         S1 integer,
         S2 integer,
         S3 integer,
         S4 integer,
         S5 integer,
         S6 integer,
         WS integer,
         ac float,
         acA float,
         acT float,
         achr float,
         achrA float,
         achrs float,
         acmile float,
         acmin float,
         acs float,
         acsT float,
         d2c1fL_sp float,
         d2c2fU_sp float,
         duration float,
         interval float,
         inthr float,
         lastInputString text,
         lastInputTime float,
         mph float,
         name text,
         one float,
         s123456ama float,
         s1234w float,
         s12w float,
         s1am float,
         s1ama float,
         s1w float,
         s2am float,
         s2ama float,
         s2w float,
         s3456ama float,
         s3am float,
         s3ama float,
         s3w float,
         s4am float,
         s4ama float,
         s4w float,
         s56am float,
         s56ama float,
         s5am float,
         s5ama float,
         s5w float,
         s6am float,
         s6ama float,
         s6w float,
         speed float,
         timestring2 text,
         ts integer,
         width float,
         alt_ft float,
         altitude float,
         altMSL float,
         count integer,
         course float,
         lat float,
         lon float,
         latitude float,
         longitude float,
         source text,
         total float,
         track float
        );''')


    cur.execute("DROP TABLE IF EXISTS meter_data")
    cur.execute(''' CREATE TABLE meter_data
        (id integer primary key autoincrement,
        TimeString text,
        channel float,
        cnt float,
        cnt_act float,
        count integer,
        countT integer,
        deere_act float,
        deere_cal float,
        end_cnt integer,
        frequency float,
        interval float,
        label text,
        lbs float,
        lbsT float,
        lbscal float,
        lbsmin float,
        lbspulse float,
        lbspulse1 float,
        lbspulse2 float,
        lbspulse_cnt float,
        lbspulse_deere float,
        lbssec float,
        one integer,
        prod text,
        source text,
        str_cnt integer,
        total float,
        ts integer,
        prod_id integer,
        foreign key (prod_id) references products(id)
        );''')


    cur.execute("DROP TABLE IF EXISTS products")
    cur.execute(''' CREATE TABLE products
        (id integer primary key autoincrement,
        product text
        );''')
