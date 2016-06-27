# -*- coding: utf-8 -*-
import wunderpy2
api = wunderpy2.WunderApi()
client = api.get_client("4571f8d62d1f9ad3a52eac32cfefeaa8191ed750ef017475d2429269bcf3", "a2fcef806cc3fabd1841")
client.create_task(197330953, "面试， 算法题， leetcode")
client.create_task(197330953, "锻炼身体")
client.create_task(197330953, "开源项目， 源码阅读")
client.create_task(197330953, "技术书")
client.create_task(197330953, "钢琴")
client.create_task(197330953, "单词")
client.create_task(197330953, "数学")
client.create_task(197330953, "杂书")