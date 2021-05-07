#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
os.environ['NLS_LANG'] = 'Simplified Chinese_CHINA.ZHS16GBK'

import requests

import logging
import time
import json
import base64
import hashlib
import binascii
import urllib


# 快递鸟接口
# self.kdniaoUrl = "http://api.kdniao.com/api/Eorderservice"
# self.kdniaoUrl = "http://testapi.kdniao.com:8081/api/Eorderservice"
kdniaoUrl = "http://sandboxapi.kdniao.com:8080/kdniaosandbox/gateway/exterfaceInvoke.json"
# kdniaoEbusinessId
eBusinessID = ""
# 快递鸟app_key
app_key = ""


def getCurTime():
    # 获取当前日期和时间
    return (time.strftime("%Y%m%d"), time.strftime("%H%M%S"))

def encrypt(origin_data):
    # origin_data 由字典转换后的字符串
    # appKey 在快递鸟官网申请的api_key(字符串)
    """数据内容签名：把(请求内容(未编码)+AppKey)进行MD5加密，然后Base64编码"""
    m = hashlib.md5()
    m.update((origin_data + app_key).encode("utf8"))
    encodestr = m.hexdigest()
    base64_text = base64.b64encode(encodestr.encode(encoding='utf-8'))
    return base64_text

def reqParams(req_type, data):
    """
        :param str req_type
        :param dict data
    """
    str_data = json.dumps(data, sort_keys = True)
    data_sign = encrypt(str_data)

    params = {
        "RequestData": str_data,
        "EBusinessID": eBusinessID,
        "RequestType": req_type,
        "DataSign": data_sign.decode(),
        "DataType": "2",
    }

    return params

def sendReq(data):
    # data 请求的数据(字典dict) reqParams的返回值
    """发送post请求"""
    headers = {'content-type': 'application/x-www-form-urlencoded','content-Encoding': 'charset=utf-8'}
    rsp = requests.post(kdniaoUrl, data = data, headers = headers)
    rsptext = base64.b64decode(rsp.text)
    return rsptext
