#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import wunderpy2
api = wunderpy2.WunderApi()
client = api.get_client("7196edc056e863b88b1d217ffe87fdde59d6800211603c4ae9c009c98872", "a2fcef806cc3fabd1841")
tasklist = ["早上单词", "开源项目， 源码阅读:", "阅读课", "数学书：", \
			"中文杂书：", "英文杂书", "论文：", "技术书", "钢琴", "乐谱 sight reading", \
			"面试， 算法题，leetcode", "锻炼身体",   "晚上单词", "水果, 苹果", "六味地黄丸","上传新认识的单词到 shanbay", \
			"凉粉, 芝麻糊", "在 stackoverflow 上问问题和回答问题"]
to_do_list_id = 197330953
for task in tasklist:
    client.create_task(to_do_list_id, task)
