#django restframework
import json
import logging

import demjson
from django.conf import settings
from pypinyin import lazy_pinyin
from requests import session
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import generics
from django_redis import get_redis_connection
from requests_repostory.request_methods import req
from v1.serializers import MapCitySerializer
from .models import MapCity

# Create your views here.

log = logging.getLogger('log')





class IndexView(APIView):

    def __init__(self):
        super(APIView).__init__()
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
        }
    def get(self,request,*args,**kwargs):
        ip=request.META.get("REMOTE_ADDR")
        # query2 = request.GET.get("type")
        # query = request.META.get("HTTP_TYPE")
        data={
            "status":0,
            "data":"successe"
        }
        return Response(data,status=200)


class TenMapViewSet(viewsets.ViewSet):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        }
        self.session = session()
    #     #百度地图
    #     self.url_ip = 'http://apis.map.qq.com/ws/location/v1/ip'
    #


    def list(self, request):
        type = request.GET.get("type")
        many=None
        if type == "guess":
            try:
                city = self.get_city_name(request)
                city_info = self.city_guess(city)
            except Exception as e:
                log.error("not find city_info")


        # elif type == "hot":
        #     cityName = "hotcities"
        #     try:
        #         queryset = MapCity.objects.get(name=cityName)
        #     except Exception as e:
        #         log.error("mapcity is not find")
        #         return Response({"errsmg": "查询数据出错"})
        #
        # elif type == "group":
        #     many=True
        #     try:
        #         queryset = MapCity.objects.all().exclude(name="hotcities")
        #     except Exception as e:
        #         log.error("mapcity is not find")
        #         return Response({"errsmg": "查询数据出错"})

        else:
            log.error("参数错误")
            return Response({"stauts": 1, "errmsg": "参数错误"})

        # serializer = MapCitySerializer(city_info,many=many)
        # print(serializer.data)
        return Response(city_info)
        # return Response(serializer.data)

    @action(detail=False)
    def getCityById(self,request):
        cityid = request.GET.get("id")
        try:
            cityid = int(cityid)
        except:
            Response({"errmsg":"cityid is not allow"})
        if not cityid:
            return Response({"errmsg":"not find cityid","status":0})
        try:
            queryset = MapCity.objects.all().exclude(name="hotcities")[0:1]
        except Exception as e:
            log.error("mapcity is not find")
            return Response({"errsmg": "查询数据出错"})
        for lists in queryset:
            for k,v in lists.title_head.items():
                for dat in v:

                    if cityid == int(dat["id"]):
                        return Response(dat)

        return Response({"errmsg":"not find citydata"})

    # @action(detail=False)
    # def  getExactAddress(self,request):

    # // 获取定位地址
    def guessPosition(self,request):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
        else:
            ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip

        if not ip:
            log.info("没有获取到ip地址")
            return {"status":0,"errmsg":"没有获取到ip地址"}

        defaultIp = '118.206.226.90'
        if ip and not ip == "127.0.0.1":
            ip = ip
        else:
            ip = defaultIp
        params = {
            "ip": ip,
            "key":settings.TENXEN_KEY
        }
        url = "http://apis.map.qq.com/ws/location/v1/ip"
        try:
            result = req(self.session, url, headers=self.headers,params=params).text
            result_list = json.loads(result)
            if result_list.get("status") == 0:
                try:
                    result_list = json.loads(result)
                    #腾讯查询
                    lng = result_list.get("result").get("location").get("lng")
                    lat = result_list.get("result").get("location").get("lat")
                    city = result_list.get("result").get("ad_info").get("city")
                    city = city.replace("市", "")
                    cityInfo = {
                        "lat":lat,
                        "lng":lng,
                        "city":city
                    }
                    return cityInfo
                except:
                    log.error("ip查询地址错误")
                    return Response({"errmsg":"ip查询地址错误"})

            else:
                log.error("获取位置信息错误")

                return {"errmsg":"ip查询地址错误"}
        except Exception as e:
            log.error(e)
            return {"errmsg":"获取位置信息错误"}

    #通过ip地址获取精确位置
    def geocoder(self,request):

        adds = self.guessPosition(request)
        parmas = {
            "key":settings.TENXEN_KEY,
            "location":"{0},{1}".format(adds.get("lat"),adds.get("lng"))
        }
        url = "http://apis.map.qq.com/ws/geocoder/v1/"

        try:
            result = req(self.session, url, headers=self.headers,params=parmas).text
            result_list = json.loads(result)
            if result_list.get("status") == 0:
                return result_list

            else:
                log.error(result_list)
                return {"errmsg":"获取精确位置错误"}
        except Exception as e:
            log.error(e)
            return {"errmsg": "获取精确位置错误"}

    def getpois(self,lat,lng):
        if not all([lat,lng]):
            return {"errmsg":"lat,lng must be require"}

        parmas = {
            "key": settings.TENXEN_KEY,
            "location": "{0},{1}".format(lat, lng)
        }
        url = "http://apis.map.qq.com/ws/geocoder/v1/"

        try:
            result = req(self.session, url, headers=self.headers, params=parmas).text
            result_list = json.loads(result)
            if result_list.get("status") == 0:
                return result_list

            else:
                log.error(result_list)
                return {"errmsg": "获取精确位置错误"}
        except Exception as e:
            log.error(e)
            return {"errmsg": "获取精确位置错误"}
    def get_city_name(self,request):
        try:
            city_info = self.guessPosition(request)
            city_pinyins = lazy_pinyin(city_info.get("city"))
            city_name = ""
            for city_pinyin in city_pinyins:
                city_name += city_pinyin
            return city_name
        except Exception as e:
            log.error(e)
            return "长沙"
    def city_guess(self,city):
        name = city[0:1].lower()
        try:
            queryset = MapCity.objects.get(name=name)
        except Exception as e:
            log.error("mapcity is not find")
            return Response({"errsmg": "查询数据出错"})

        demjson_lists = demjson.decode(queryset.title_head)
        for lists in demjson_lists.get(name.upper()):
            if lists.get("pinyin") == city:
                return lists

    @action(detail=False)
    def getExactAddress(self,request):
        try:
            positon = self.geocoder(request)
            return Response(positon)
        except Exception as e:
            return  Response({"errmsg":"err data"})



    @action(detail=False)
    def pois(self,request):
        geohash = request.GET.get("geohash")
        if not geohash:
            return Response({"errsmg":"geohash not find"})

        poisArr =  geohash.split(",")
        print(poisArr)
        try:
            result = self.getpois(poisArr[0],poisArr[1])
            address = {
                            "address": result.get("result").get("address"),
                            "city": result.get("result").get("address_component").get("province"),
                            "latitude": poisArr[0],
                            "longitude": poisArr[1],
                            "geohash":geohash,
                            "name": result.get("result").get("formatted_addresses").get("recommend")
                     }
            return Response(address)
        except Exception as e:
            log.error(e)
            return Response({"errmsg":"err data"})
class MapList(generics.ListCreateAPIView):

    queryset = MapCity.objects.all()
    serializer_class = MapCitySerializer



