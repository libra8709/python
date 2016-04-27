# -*- coding:utf-8 -*-
import yate
import os
import time
import sys
import cgi

print(yate.start_response("text/plain"))
addr=os.environ["REMOTE_ADDR"]
host=os.environ["REMOTE_HOST"]
method=os.environ["REQUEST_METHOD"]
cur_time=time.asctime(time.localtime())
print(host+", "+addr+", "+cur_time+": "+method+": ",end='',file=sys.stderr)

form=cgi.FieldStorage()
for each_from in form.keys():
    print(each_from+"->"+form[each_from].value,end='',file=sys.stderr)
print(file=sys.stderr)
print("ok.")