#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wunderpy2
api = wunderpy2.WunderApi()
client = api.get_client("7196edc056e863b88b1d217ffe87fdde59d6800211603c4ae9c009c98872", "a2fcef806cc3fabd1841")
tomorrow_to_do_name = []
tomorrow_to_do_id_revision = []
for item in client.get_tasks(244025185):
	tomorrow_to_do_id_revision.append((item['id'], item['revision']))
	tomorrow_to_do_name.append(item['title'])

for item in tomorrow_to_do_id_revision:
	client.delete_task(item[0], item[1])

for item in tomorrow_to_do_name:
	client.create_task(197330953, item)