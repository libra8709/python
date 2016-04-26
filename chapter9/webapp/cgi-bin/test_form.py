# -*- coding:utf-8 -*-
import yate

print(yate.start_response())
print(yate.do_form("add_timing_data.py",['TimeValue'],text="Send"))