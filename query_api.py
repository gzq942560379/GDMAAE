# -*- coding:utf-8  -*-

from gstore_api import send_post

"""
**任务一**：利用构建好的知识图谱，编写sparql语句查询两个公司之间的关联路径（2-hop）。例如输入公司“招商局轮船股份有限公司”和“招商银行股份有限公司”，得到这两家公司之间的所有路径。
"""
def query_two_hop_paths(company1:str,company2:str):
    # build sql
    sql = f'''
        SELECT ?p ?o 
        WHERE{{
            {company1} ?p ?o .
            ?o ?p {company2}
        }}
        '''
    response = send_post(sql)
    return response



"""
**任务二：**编写sparql语言实现多层股权的穿透式查询，可以根据指定层数获得对应层级的股东，例如：输入“招商局轮船股份有限公司””和层数3，就会把“招商局轮船股份有限公司”所对应公司所有三层以内的公司找出来。
"""
def query_pre_n_layer_company(company:str,layer:int):
    assert layer <= 9
    company_candidate = ["?a", "?b", "?c", "?d", "?e", "?f", "?g", "?h", "?i", "?j"]
    sql_object_list = []
    for i in range(layer):
        sql_object_list.append(company_candidate[i])
        sql_object_list.append("?p")
        sql_object_list.append(company_candidate[i+1])
        sql_object_list.append(".")

    sql_object_list = sql_object_list[:-2]
    sql_part = " ".join(sql_object_list)
    # build sql
    sql = f'''
        SELECT *
        WHERE{{
            {sql_part} {company}
        }}
        '''
    # print(sql)
    response = send_post(sql)
    return response

def query_next_n_layer_company(company:str,layer:int):
    assert layer <= 9
    company_candidate = ["?a", "?b", "?c", "?d", "?e", "?f", "?g", "?h", "?i", "?j"]
    sql_object_list = []
    for i in range(layer):
        sql_object_list.append(company_candidate[i])
        sql_object_list.append("?p")
        sql_object_list.append(company_candidate[i+1])
        sql_object_list.append(".")

    sql_object_list = sql_object_list[1:-1]
    sql_part = " ".join(sql_object_list)
    # build sql
    sql = f'''
        SELECT *
        WHERE{{
            {company} {sql_part} 
        }}
        '''
    # print(sql)
    response = send_post(sql)
    return response
