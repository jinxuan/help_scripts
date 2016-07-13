#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import wunderpy2
api = wunderpy2.WunderApi()
client = api.get_client("4571f8d62d1f9ad3a52eac32cfefeaa8191ed750ef017475d2429269bcf3", "a2fcef806cc3fabd1841")
tasklist = ["面试， 算法题， leetcode", "锻炼身体", "开源项目， 源码阅读", "技术书", "钢琴", "单词", "数学", "杂书", "论文"]
to_do_list_id = 197330953
for task in tasklist:
    client.create_task(to_do_list_id, task)
