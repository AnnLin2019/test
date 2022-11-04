# -*- coding: utf-8 -*-
"""
# @Time    :  2022/9/16 13:43
# @Author  : linxiaoyi
# @FileName: processingRelevant.py
#@IDE ：PyCharm
"""

import re,json
class Relevant():
    # 获取参数关联封装
    # relevant = data[excelVarles.case_relevant]

    def intMath(self,match) -> str:
        index = match.group()
        return eval(index)

    # 转换提取参数格式的值，类似[result][items][0][depId]->["result"]["items"][0]["depId"]
    def get_case_relevant(self,relevant,res):
        # [data][access_token]
        relevant_dict = {}
        if relevant:
            relevant_list = relevant.split(";")

            for relevant_i in relevant_list:
                relevant_str = relevant_i.split("=")
                relevant_key = relevant_str[0]
                relevant_value = relevant_str[1]
                # relevant_value.split("][")
                relevant_1 = re.sub(r'\[', '[\"', relevant_value)
                relevant_2 = re.sub(r'\]', '\"]', relevant_1)
                if re.findall(r":", str(relevant_2)):
                    relevant_2 = re.sub(r':', '\"][\"', relevant_2)
                else:
                    relevant_2 = relevant_2
                relevant_eval = re.sub(r'\"[\d]\"', self.intMath, relevant_2)
                # print("提取格式转换后{}".format(relevant_eval))
                relevant_eval_str = str(res) + relevant_eval
                # print("relevant_eval_str：",type(relevant_eval_str))
                relevant_eval_str=re.sub('null','None',relevant_eval_str)
                relevant_eval_str=re.sub('true','True',relevant_eval_str)
                relevant_eval_str=re.sub('false', 'False', relevant_eval_str)
                try:
                    # relevant_last = eval(relevant_eval_str)
                    relevant_last = eval(relevant_eval_str)
                    # relevant_last=json.dumps(relevant_last,ensure_ascii=False)
                    print("提取值是{}".format(relevant_last))
                    # print("type(relevant_dict)是",relevant_dict)
                    relevant_dict[relevant_key] = relevant_last
                    print("relevant_dict是{}".format(relevant_dict))
                except Exception as e:
                    relevant_error="提取{}参数失败,失败原因：{}".format(relevant_key, str(e))
                    # relevant_dict = {}
                    relevant_dict[relevant_key]=relevant_error
                    print(relevant_error)

            return relevant_dict

    # 传入关联参数封装
    def write_case_relevant(self,case_value, relevant_lists):
        # print("type(case_value):",type(case_value))
        # print("write_case_relevant.relevant_dict:",relevant_dict)
        is_relevant = re.findall(r"\${.+?}", str(case_value))
        if is_relevant and len(relevant_lists) > 0:
            print("relevant_list", type(relevant_lists))
            print("relevant_list", relevant_lists)
            for i in range(len(relevant_lists)):
                relevant_i = relevant_lists[i]
                if relevant_i is not None:
                    # if relevant_dict:
                    # print(type(case_value), type(relevant_dict))
                    for relevant_key in relevant_i:
                        print("befor_relevant_dict:", relevant_i)
                        # relevant_key=json.dumps(relevant_key,ensure_ascii=False)
                        # case_value = re.sub(str(relevant_key), str(relevant_dict[relevant_key]), case_value)
                        # case_value=str(case_value).replace(str(relevant_key), json.dumps(relevant_dict[relevant_key],ensure_ascii=False))
                        case_value = str(case_value).replace(str(relevant_key), str(relevant_i[relevant_key]))
                        # case_value=json.dumps(case_value,ensure_ascii=False) #双引号
                        # case_value=case_value.replace("'","\"")
                        # relevant_key_new = json.dumps(relevant_key, ensure_ascii=False)
                        # print("case_value_new是", case_value)
                        # yield case_value
                    # print("relevant_dict___是", relevant_dict)
                else:
                    print("找不到关联参数")
        else:
            # print("无需关联参数")
            pass
        return case_value
    def write_case_relevant2(self,case_value, relevant_dicts):
        # print("type(case_value):",type(case_value))
        # print("case_value:",case_value)
        # print("write_case_relevant.relevant_dict:",relevant_dicts)
        is_relevant = re.findall(r"\${.+?}", str(case_value))
        # print("is_relevant:",is_relevant)
        if is_relevant:
            # print("relevant_list", type(relevant_dicts))
            # print("relevant_list", relevant_dicts)

            if relevant_dicts:
                    print(type(case_value), type(relevant_dicts))
                    for relevant_key in relevant_dicts:
                        # print("befor_relevant_dict:", relevant_dicts[relevant_key])
                        # relevant_key=json.dumps(relevant_key,ensure_ascii=False)
                        # case_value = re.sub(str(relevant_key), str(relevant_dict[relevant_key]), case_value)
                        # case_value=str(case_value).replace(str(relevant_key), json.dumps(relevant_dict[relevant_key],ensure_ascii=False))
                        case_value = str(case_value).replace(str(relevant_key), str(relevant_dicts[relevant_key]))
                        # case_value=json.dumps(case_value,ensure_ascii=False) #双引号
                        # case_value=case_value.replace("'","\"")
                        # relevant_key_new = json.dumps(relevant_key, ensure_ascii=False)
                        # print("case_value_new是", case_value)
                        # yield case_value
                    # print("relevant_dict___是", relevant_dict)
            else:
                print("找不到关联参数")
        else:
            # print("无需关联参数")
            pass
        return case_value

    def update_Relevantdict(self,relevant_dict_global,adict):
        if adict:
            relevant_dict_global.update(adict)
        else:
            relevant_dict_global=relevant_dict_global
        return relevant_dict_global

if __name__ == '__main__':
    d={'${access_token}': '9bf7408d-deaa-4ee9-ad36-7b4a78cb2d34', '${depId1}': 556261, '${depId2}': 556047,
     '${parentid}': 555765, '${department}': 569511, '${userId0}': 7241577,
     '${userId1}': '提取${userId1}参数失败,失败原因：list index out of range',
     '${userId2}': '提取${userId2}参数失败,失败原因：list index out of range',
     '${userId3}': '提取${userId3}参数失败,失败原因：list index out of range',
     '${userId4}': '提取${userId4}参数失败,失败原因：list index out of range',
     '${userId5}': '提取${userId5}参数失败,失败原因：list index out of range',
     '${userId6}': '提取${userId6}参数失败,失败原因：list index out of range', '${department2}': 569511, '${department3}': 569513}
    print(d['${department2}'])
    Relevant=Relevant()
    relevant='${roomId}=[result][data:0][roomId]'
    res='{"result":{"data":[{"roomId":1016003,"roomName":"py匿名用户号可加入",' \
        '"status":"1","inviteCode":"767715004","inviteStatus":true,"showMeetingControl":true}]}}'
    Relevant.get_case_relevant(relevant,res)
    relevant2='${clientid}=[result][data:0][id]'
    res2='{"result":{"data":[{"id":2450556,"createTime":"2022-10-28 10:57:40","clientId":"c65f7dd5-27de-4ded-85d8-137f9a0658bc","secret":"ba720bf4-4f3c-4597-8261-bc9e981d59c6","clientName":"py自动化应用","status":true},{"id":2450557,"createTime":"2022-11-01 15:10:21","clientId":"fee23823-ee01-473f-ab89-6e56c6125497","secret":"2f4e559d-6825-4129-af4c-79de386ed4b5","clientName":"py自动化应用","status":true},{"id":2450558,"createTime":"2022-11-02 11:24:53","clientId":"318d1e1b-31ef-42e0-b9fa-8a3acdffbcab","secret":"b7852aa5-d88a-42e4-94a8-4c9d192cc326","clientName":"py自动化应用","status":true},{"id":2450559,"createTime":"2022-11-02 11:39:36","clientId":"bec13634-f205-4cbf-a777-fc97070eda55","secret":"9073b4be-ccb0-4059-acc7-381b865a8ede","clientName":"py自动化应用","status":true}],"count":4},"resCode":0,"resMessage":"success"}'
    Relevant.get_case_relevant(relevant2, res2)
    # a={"result":{"data":[{"roomId":1016003,"roomName":"py匿名用户号可加入",' \
    #     '"status":"1","inviteCode":"767715004","inviteStatus":True,"showMeetingControl":True}]}}
    # print(a['result']['data'][0]['roomId'])