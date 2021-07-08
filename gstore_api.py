# -*- coding:utf-8  -*-

import json
import requests

accesskeyid = "d247f84aaacc4608a65ea2763354a0f4"
access_secret = "31A2E7513A8C38A1A8B47629EB319B59"

url = "http://cloud.gstore.cn/api"
dbName = "jinrong"


def send_post(sql: str):
    data = {"accesskeyid": accesskeyid, "access_secret": access_secret, "dbName": dbName, "action": "queryDB",
            "sparql": sql}
    # 字符串格式
    res = requests.post(url=url, data=data)
    json_data = json.loads(res.text)
    if json_data["msg"] == "ok":
        return json_data["data"]
    else:
        print(json_data)
        exit(-1)