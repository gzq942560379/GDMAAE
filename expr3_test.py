# -*- coding:utf-8  -*-
import networkx as nx
from query_api import query_next_n_layer_company
from util import company_add_prefix_and_suffix
from util import company_delete_prefix_and_suffix

#**任务三：**编写sparql语言实现环形持股查询，判断两家公司是否存在环形持股现象，环形持股是指两家公司彼此持有对方的股份。例如：输入“A”和“C”，判断两家公司是否存在环形持股。

def check_ring_hold(company1:str,company2:str):
    G1=nx.DiGraph()
    G1.add_node(company1)
    company1_query_result = query_next_n_layer_company(company_add_prefix_and_suffix(company1),5)
    for r in company1_query_result["results"]["bindings"]:
        b = company_delete_prefix_and_suffix(r["b"]["value"])
        c = company_delete_prefix_and_suffix(r["c"]["value"])
        d = company_delete_prefix_and_suffix(r["d"]["value"])
        e = company_delete_prefix_and_suffix(r["e"]["value"])
        f = company_delete_prefix_and_suffix(r["f"]["value"])
        G1.add_node(b)
        G1.add_node(c)
        G1.add_node(d)
        G1.add_node(e)
        G1.add_node(f)
        G1.add_edge(company1,b)
        G1.add_edge(b,c)
        G1.add_edge(c,d)
        G1.add_edge(d,e)
        G1.add_edge(e,f)
    G2=nx.DiGraph()
    G2.add_node(company2)
    company2_query_result = query_next_n_layer_company(company_add_prefix_and_suffix(company2),5)
    for r in company2_query_result["results"]["bindings"]:
        b = company_delete_prefix_and_suffix(r["b"]["value"])
        c = company_delete_prefix_and_suffix(r["c"]["value"])
        d = company_delete_prefix_and_suffix(r["d"]["value"])
        e = company_delete_prefix_and_suffix(r["e"]["value"])
        f = company_delete_prefix_and_suffix(r["f"]["value"])
        G2.add_node(b)
        G2.add_node(c)
        G2.add_node(d)
        G2.add_node(e)
        G2.add_node(f)
        G2.add_edge(company2,b)
        G2.add_edge(b,c)
        G2.add_edge(c,d)
        G2.add_edge(d,e)
        G2.add_edge(e,f)

    # A 持股 C ， C 持股 A
    found = False
    if company2 in G1.nodes() and company1 in G2.nodes():
        found = True

    if found:
        path1 = nx.all_simple_paths(G1,company1,company2)
        path2 = nx.all_simple_paths(G2,company2,company1)

    return found, path1, path2


if __name__ == "__main__":
    found , path1, path2  = check_ring_hold("A","C")
    if found:
        print("A C 存在环形持股")

        print("paths from A to C")
        for path in path1:
            print(" -> ".join(path))

        print("paths from C to A")
        for path in path2:
            print(" -> ".join(path))



