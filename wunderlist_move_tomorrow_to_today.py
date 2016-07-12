#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wunderpy2
api = wunderpy2.WunderApi()
client = api.get_client("4571f8d62d1f9ad3a52eac32cfefeaa8191ed750ef017475d2429269bcf3", "a2fcef806cc3fabd1841")
tomorrow_to_do_name = []
tomorrow_to_do_id_revision = []
for item in client.get_tasks(244025185):
	tomorrow_to_do_id_revision.append((item['id'], item['revision']))
	tomorrow_to_do_name.append(item['title'])

for item in tomorrow_to_do_id_revision:
	client.delete_task(item[0], item[1])

for item in tomorrow_to_do_name:
	client.create_task(197330953, item)