# -*- coding:utf-8  -*-

from query_api import query_pre_n_layer_company
from query_api import query_next_n_layer_company
from util import company_add_prefix_and_suffix
from util import company_delete_prefix_and_suffix


def get_one_layer(company):
    print()
    print("get_one_layer:")
    pre_result = query_pre_n_layer_company(company_add_prefix_and_suffix(company),1)
    for r in pre_result["results"]["bindings"]:
        p = r["p"]["value"]
        a = r["a"]["value"]
        print(f"{company_delete_prefix_and_suffix(a)} -> {company_delete_prefix_and_suffix(company)}")
    print()
    next_result = query_next_n_layer_company(company_add_prefix_and_suffix(company),1)
    for r in next_result["results"]["bindings"]:
        p = r["p"]["value"]
        b = r["b"]["value"]
        print(f"{company_delete_prefix_and_suffix(company)} -> {company_delete_prefix_and_suffix(b)}")
    print()


def get_two_layer(company):
    print()
    print("get_two_layer:")
    pre_result = query_pre_n_layer_company(company_add_prefix_and_suffix(company),2)
    for r in pre_result["results"]["bindings"]:
        p = r["p"]["value"]
        a = r["a"]["value"]
        b = r["b"]["value"]
        print(f"{company_delete_prefix_and_suffix(a)} -> {company_delete_prefix_and_suffix(b)} -> {company_delete_prefix_and_suffix(company)}")
    print()
    next_result = query_next_n_layer_company(company_add_prefix_and_suffix(company),2)
    for r in next_result["results"]["bindings"]:
        p = r["p"]["value"]
        b = r["b"]["value"]
        c = r["c"]["value"]
        print(f"{company_delete_prefix_and_suffix(company)} -> {company_delete_prefix_and_suffix(b)} -> {company_delete_prefix_and_suffix(c)}")
    print()

def get_three_layer(company):
    print()
    print("get_three_layer:")
    pre_result = query_pre_n_layer_company(company_add_prefix_and_suffix(company),3)
    for r in pre_result["results"]["bindings"]:
        a = r["a"]["value"]
        b = r["b"]["value"]
        c = r["c"]["value"]
        print(f"{company_delete_prefix_and_suffix(a)} -> {company_delete_prefix_and_suffix(b)} -> {company_delete_prefix_and_suffix(c)} -> {company_delete_prefix_and_suffix(company)}")
    print()
    next_result = query_next_n_layer_company(company_add_prefix_and_suffix(company),3)
    for r in next_result["results"]["bindings"]:
        b = r["b"]["value"]
        c = r["c"]["value"]
        d = r["d"]["value"]
        print(f"{company_delete_prefix_and_suffix(company)} -> {company_delete_prefix_and_suffix(b)} -> {company_delete_prefix_and_suffix(c)} -> {company_delete_prefix_and_suffix(d)}")
    print()


if __name__ == "__main__":
    company = "C"
    get_one_layer(company)
    get_two_layer(company)
    get_three_layer(company)



