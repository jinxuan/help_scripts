#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import wunderpy2
api = wunderpy2.WunderApi()
client = api.get_client("7196edc056e863b88b1d217ffe87fdde59d6800211603c4ae9c009c98872", "a2fcef806cc3fabd1841")
tasklist = ["洗衣服", "洗毛巾"]
tasklist = ["routing: " + i for i in tasklist]
to_do_list_id = 197330953
for task in tasklist:
    client.create_task(to_do_list_id, task)
