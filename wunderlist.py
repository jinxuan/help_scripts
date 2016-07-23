#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import wunderpy2
api = wunderpy2.WunderApi()
client = api.get_client("4571f8d62d1f9ad3a52eac32cfefeaa8191ed750ef017475d2429269bcf3", "a2fcef806cc3fabd1841")
tasklist = ["早上单词", "开源项目， 源码阅读:", "数学书：", "中文杂书：", "英文杂书", "论文：", "技术书", "钢琴", "乐谱 sight reading", "面试， 算法题，leetcode", "锻炼身体",   "晚上单词", "水果, 苹果"]
to_do_list_id = 197330953
for task in tasklist:
    client.create_task(to_do_list_id, task)
