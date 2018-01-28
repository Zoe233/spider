#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup

class getUrls(object):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
    }
    aslikang_urls =['http://ypk.familydoctor.com.cn/factory_11255_1_0_0_2_1.html',
                   'http://ypk.familydoctor.com.cn/factory_11255_0_0_0_0_2.html']

    def __init__(self):
        self.session= requests.Session()
        self.session.headers = getUrls.headers
        self.li_list = []
        self.href_src = {}
        self.index = 0
        self.base_dir = '/Users/zoe/文件管理/阿斯利康药品'




    def __getLi(self):
        '''根据url抓取li标签内容,并去重。注意如果涉及到去重，一定要再前面想办法去掉，否则越到后面越复杂不好处理'''
        for i in getUrls.aslikang_urls:
            html = self.session.get(i,timeout=15)
            html.encoding='utf-8'
            soup = BeautifulSoup(html.text,'lxml')
            li = soup.find_all('li',class_='clearfix')

            for j in li:
                self.li_list.append(j)
            li=[]
        self.li_list = set(self.li_list)
        self.li_list = list(self.li_list)
        return self.li_list

    def __getHrefSrc(self):
        '''将Href和Src的链接内容存到一个字典中。'''
        self.__getLi()
        for i in self.li_list:
            subdic={}
            self.href_src[self.index] = subdic
            subdic['href'] = i.a.get('href')
            subdic['instruc_href'] = i.a.get('href') + 'instructions/'
            subdic['src'] = i.a.img.get('src')
            self.index +=1
        return self.href_src

    def __mkDir(self):
        '''根据index创建目录'''
        self.__getHrefSrc()
        if os.path.exists(self.base_dir):
            for k in self.href_src.keys():
                if os.path.exists(os.path.join(self.base_dir,str(k))):
                    continue
                else:
                    os.mkdir(os.path.join(self.base_dir,str(k)))
        else:
            os.os.makedirs(self.base_dir)
        return

    def __getIntroduction(self):
        '''获取说明书信息'''
        for k,v in self.href_src.items():
            html = self.session.get(v['instruc_href'],timeout=10)
            html.encoding = 'utf-8'
            soup = BeautifulSoup(html.text,'lxml')
            table = soup.find('table',class_='table-1')
            trs = table.find_all('tr')

            for t in trs:
                with open(os.path.join(self.base_dir,str(k))+'/instructions.txt','a+') as f:
                    if t.th.string:
                        f.write(t.th.string)
                        try:
                            # f.write(str(t.td.string)) if f.write(t.td.string) else f.write(str(t.td.a.string))
                            f.write(t.td.string)
                        except:
                            pass
                        f.write('\n')

    def __getGeneral(self):
        '''获取概述'''
        for k,v in self.href_src.items():
            if v['href'] =='http://ypk.familydoctor.com.cn/218921/':
                html = self.session.get(v['href'], timeout=10)
                html.encoding = 'utf-8'
                soup = BeautifulSoup(html.text, 'lxml')
                table = soup.find('table', class_='table-1')  # 由于一个page上有两个这样的table，取第一个。
                trs = table.find_all('tr')
                try:
                    # 药品名称
                    med_name_00 = trs[0].th.string
                    med_name_01 = trs[0].td.string

                    # 批准文号
                    approve_code_00 = trs[1].th.string
                    approve_code_01 = trs[1].td.string

                    # 生产企业
                    product_co_00 = trs[2].th.string
                    product_co_01 = trs[2].td.a.string

                    #  # 功效主治
                    main_effect_00 = '功能主治：'
                    main_effect_01 = ''

                    # 治疗疾病
                    cure_disease_00 = trs[3].th.string
                    cure_disease_01 = list(trs[3].td.span.a.string)
                except:
                    raise IndexError
            elif v['href'] == 'http://ypk.familydoctor.com.cn/113985/':
                html = self.session.get(v['href'], timeout=10)
                html.encoding = 'utf-8'
                soup = BeautifulSoup(html.text, 'lxml')
                table = soup.find('table', class_='table-1')  # 由于一个page上有两个这样的table，取第一个。
                trs = table.find_all('tr')
                try:
                    # 药品名称
                    med_name_00 = trs[0].th.string
                    med_name_01 = trs[0].td.string

                    # 批准文号
                    approve_code_00 = trs[1].th.string
                    approve_code_01 = trs[1].td.string

                    # 生产企业
                    product_co_00 = trs[2].th.string
                    product_co_01 = trs[2].td.a.string

                    #  # 功效主治
                    main_effect_00 = trs[3].th.string
                    main_effect_01 = trs[3].td.string

                    # 治疗疾病
                    cure_disease_00 = '治疗疾病：'
                    cure_disease_01 = ''
                except:
                    raise IndexError
            elif v['href'] =='http://ypk.familydoctor.com.cn/203740/':
                html = self.session.get(v['href'], timeout=10)
                html.encoding = 'utf-8'
                soup = BeautifulSoup(html.text, 'lxml')
                table = soup.find('table', class_='table-1')  # 由于一个page上有两个这样的table，取第一个。
                trs = table.find_all('tr')
                try:
                    # 药品名称
                    med_name_00 = trs[0].th.string
                    med_name_01 = trs[0].td.string

                    # 批准文号
                    approve_code_00 = trs[1].th.string
                    approve_code_01 = trs[1].td.string

                    # 生产企业
                    product_co_00 = trs[2].th.string
                    product_co_01 = trs[2].td.a.string

                    #  # 功效主治
                    main_effect_00 = '功能主治：'
                    main_effect_01 = ''

                    # 治疗疾病
                    cure_disease_00 = '治疗疾病：'
                    cure_disease_01 = ''
                except:
                    raise IndexError
            else:
                html = self.session.get(v['href'],timeout=10)
                html.encoding = 'utf-8'
                soup = BeautifulSoup(html.text,'lxml')
                table = soup.find('table',class_ = 'table-1')  # 由于一个page上有两个这样的table，取第一个。
                trs = table.find_all('tr')

                try:
                    # 药品名称
                    med_name_00 = trs[0].th.string
                    med_name_01 = trs[0].td.string

                    # 批准文号
                    approve_code_00 = trs[1].th.string
                    approve_code_01 = trs[1].td.string

                    # 生产企业
                    product_co_00 = trs[2].th.string
                    product_co_01 = trs[2].td.a.string

                    # 功效主治
                    main_effect_00 = trs[3].th.string
                    main_effect_01 = trs[3].td.string

                    # 治疗疾病
                    cure_disease_00 = trs[4].th.string

                    spans = trs[4].find_all('span')
                    sp = []

                    for s in spans:
                        ele = s.string
                        sp.append(ele)
                    cure_disease_01 = sp

                except Exception as e:
                    print(e)

            print('*'*50,v['href'])
            print(med_name_00,med_name_01)
            print(approve_code_00,approve_code_01)
            print(product_co_00,product_co_01)
            print(main_effect_00,main_effect_01)
            print(cure_disease_00,cure_disease_01)

            with open(os.path.join(self.base_dir,str(k))+'/med_general.txt','w') as f:
                f.write(med_name_00)
                f.write(med_name_01)
                f.write('\n')
                f.write(approve_code_00)
                f.write(approve_code_01)
                f.write('\n')
                f.write(product_co_00)
                f.write(product_co_01)
                f.write('\n')
                f.write(main_effect_00)
                f.write(main_effect_01)
                f.write('\n')
                f.write(cure_disease_00)
                f.write(str(cure_disease_01))



    def __getPic(self):
        '''获取图片'''
        for k,v in self.href_src.items():
            print(v['src'])
            html = self.session.get(v['src'],timeout=10)
            with open(os.path.join(self.base_dir,str(k))+'/picture.jpg','wb') as f:
                f.write(html.content)

    def __removeFile(self):
        '''通过批量执行删除写入的不要的说明书文件'''
        for k,v in self.href_src.items():
            if os.path.exists(os.path.join(self.base_dir,str(k))+'/instructions.txt'):
                os.remove(os.path.join(self.base_dir,str(k))+'/instructions.txt')


    def run(self):
        self.__mkDir()
        # self.__getIntroduction()  ## 开发期间是单步执行的，已经完成，可以不用再执行，当然覆盖结果由于是追加模式，所以要变更说明书的名称。
        # self.__getGeneral() # 开发期间是单步执行的，已经完成，可以不用再执行，当然覆盖结果再来也ok
        # self.__getPic() # 开发期间是单步执行的，已经完成，可以不用再执行，当然覆盖结果再来也ok
        # self.__removeFile() # 用来批量删除不要的文件


if __name__== '__main__':
    g = getUrls()
    g.run()



