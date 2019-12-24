import kdniao

# 测试数据准备
data= {'OrderCode': '012657700387', 'ShipperCode':'SF', 'PayType':1, 'ExpType':1, 'Cost':1.0, 'OtherCost':1.0, 'Sender': {'Company':'LV','Name':'Taylor','Mobile':'15018442396','ProvinceName':u'上海','CityName':u'上海','ExpAreaName':u'青浦区','Address':u'明珠路73号'}, 'Receiver': {'Company':'GCCUI','Name':'Yann','Mobile':'15018442396','ProvinceName':u'北京','CityName':u'北京','ExpAreaName':u'朝阳区','Address':u'三里屯街道雅秀大厦'}, 'Commodity': [{'GoodsName':u'鞋子','Goodsquantity':1,'GoodsWeight':1.0}], 'Weight':1.0, 'Quantity':1, 'Volume':0.0, 'Remark':u'小心轻放', 'IsReturnPrintTemplate':1}

# 生成请求数据
# 电子面单 1007
# 电子面单取消 1147
# 物流跟踪 1008
# 即时查询 1002
req_data = kdniao.reqParams("1007", data)

# 电子面单请求
kdniao.sendReq(req_data)
