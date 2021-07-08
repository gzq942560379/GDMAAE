# -*- coding:utf-8  -*-

from query_api import query_two_hop_paths
from util import company_add_prefix_and_suffix
from util import company_delete_prefix_and_suffix

def get_two_hop_path(company1,company2):
    result = query_two_hop_paths(company_add_prefix_and_suffix(company1),company_add_prefix_and_suffix(company2))
    for r in result["results"]["bindings"]:
        p = r["p"]["value"]
        o = r["o"]["value"]
        print(f"{(company1)} -> {company_delete_prefix_and_suffix(o)} -> {(company2)}")

if __name__ == "__main__":
    get_two_hop_path("A","C")
