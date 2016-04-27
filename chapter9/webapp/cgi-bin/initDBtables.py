# -*- coding:utf-8 -*-
import sqlite3
import glob
import athletemodel

connection=sqlite3.connect("../data/coachdata.sqlite")
cursor=connection.cursor()
data_files=glob.glob("../data/*txt")
athletes=athletemodel.put_to_store(data_files)

for each_data in athletes:
    name=athletes[each_data].name
    dob=athletes[each_data].dob
    cursor.execute("INSERT INTO athletes (name,dob) VALUES (?,?)",(name,dob))
    cursor.execute("SELECT id FROM athletes WHERE name=? AND dob=?",(name,dob))
    the_current_id=cursor.fetchone()[0]
    for each_time in athletes[each_data].clean_data:
        cursor.execute("INSERT INTO timing_data (athlete_id,value) VALUES (?,?)",(the_current_id,each_time))
        connection.commit()

connection.close()