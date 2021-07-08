company_prefix="<file:///F:/d2r-server-0.7/holder8.nt#holder_copy/"
company_suffix=">"

company_prefix2="file:///F:/d2r-server-0.7/holder8.nt#holder_copy/"

def company_add_prefix_and_suffix(company_name:str)->str:
    if company_name.startswith(company_prefix) or company_name.startswith(company_prefix):
        return company_name
    return company_prefix + company_name + company_suffix


def company_delete_prefix_and_suffix(company_name:str)->str:
    if company_name.startswith(company_prefix) and company_name.endswith(company_suffix):
        return company_name[len(company_prefix):-len(company_suffix)]
    if company_name.startswith(company_prefix2):
        return company_name[len(company_prefix2):]
    return company_name