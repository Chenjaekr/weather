#-*-coding:utf-8-*-

import urllib2
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
import json
# import chardet

a = True

while a:

    print '输入想要查询的城市(拼音或汉字)：'
    city = raw_input()

    web = urllib2.Request('http://apis.baidu.com/heweather/weather/free?city=%s' % city)
    web.add_header("apikey", "5c7e53c9c2e3dad22afdd1b34ebd4510")
    web_result = urllib2.urlopen(web)
    content = web_result.read()




    data = json.loads(content)
    result = data['HeWeather data service 3.0']


    result = result[0]
    # print result
    try:
        print '城市：', result['basic']['city']
    except:
        print '无法查询该城市'
        continue
    try:
        print '体感温度：', result['now']['fl']
        print '实时气温：', result['now']['tmp']
    except:
        print '没有天气数据'
    try:
        print '空气质量(AQI)：', result['aqi']['city']['aqi']
    except:
        print '没有AQI数据'


    print '三小时天气预报：' , result['hourly_forecast'][0]['date']
    for i in result['hourly_forecast']:
        print '时间：', i['date'],'  ','温度：', i['tmp'],'℃'
    print '更新时间：', result['basic']['update']['loc']
    b = raw_input('是否继续查询？(Y/N)\n')
    print b
    if (b == 'Y') or (b == 'y'):
        continue
    else:
        a = False