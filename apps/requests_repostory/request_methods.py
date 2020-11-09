import random
import traceback

import requests
import logging
log  = logging.getLogger('log')




def get_proxies():
    # 代理服务器，支持http和https

    return ['192.168.62.10:12000']  #

def req(session, url, proxies=None, debug=0, method='get', timeout=3, retry_times=2, proxy=False,**kwargs):
    request_method = {'get': session.get, 'post': session.post, 'head': session.head, 'options': session.options}
    retry = retry_times
    is_first = True
    # proxy = ""
    while retry > 0:
        try:
            if debug == 0:
                #需要代理
                if proxy:
                    proxies = proxies if proxies else get_proxies()
                    if proxies:
                        proxy = random.choice(proxies)
                        print('proxy:', proxy)
                        # return request_method[method](url, proxies={"http": proxy}, timeout=2, **kwargs)
                        if url[:6] == 'https:':
                            # print('https')
                            return request_method[method](url, proxies={"https": "https://" + proxy}, timeout=timeout,
                                                          **kwargs)
                        # elif url[:6] == 'http:/':
                        else:
                            # print('http')
                            return request_method[method](url, proxies={"http": "http://" + proxy}, timeout=timeout,
                                                          **kwargs)
                    else:
                        return request_method[method](url, timeout=timeout, **kwargs)
                else:
                    return request_method[method](url, timeout=timeout, **kwargs)
            else:
                return request_method[method](url, timeout=timeout, **kwargs)
        except Exception as er:
            retry -= 1
            msg = traceback.format_exc()
            log.error("请求错误--{}".format(msg))

            # if (debug == 0 and retry == 0 and "time out" in msg and "192.168" in msg):
            #     raise Exception("连接代理服务，最后:" + proxy + "超时" + "请求次数:" + str(retry_times + 1))

        try:
            if retry == 0 and debug == 1:
                return request_method[method](url, timeout=timeout, **kwargs)
        except:
            raise Exception("http请求失败：URL地址:" + url + "请求次数:" + str(retry_times + 1))

