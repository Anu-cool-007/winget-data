import os
import json
import yaml
import time


def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
        with open(path, 'r', encoding="utf8") as infile:
            # PYPrime has tab indented yaml files
            d['content'] = yaml.safe_load(infile.read().replace('\t', ' '))
    return d


def get_company_path(ch_path):
    return [os.path.join(ch_path, x) for x in os.listdir(ch_path)]


def get_company_data(company_path):
    data = []
    company_name = os.path.split(company_path)[1]
    for product_path in [os.path.join(company_path, x) for x in os.listdir(company_path)]:
        product_name = os.path.split(product_path)[1]
        version_data = [path_to_dict(os.path.join(product_path, x)) for x in os.listdir(product_path)]
        product_data = {
            'name': product_name,
            'company': company_name,
            'versions': version_data
        }
        data.append(product_data)
    return data


def extract_data(root_path):
    ch_dir = [os.path.join(root_path, x) for x in os.listdir(root_path)]
    data = []
    for ch_path in ch_dir:
        for company_path in get_company_path(ch_path):
            for product_data in get_company_data(company_path):
                data.append(product_data)
    return data


start_time = time.time()
json_obj = json.dumps(extract_data('./data/manifests'), indent=2)
# Writing to sample.json
with open("data2.json", "w") as outfile:
    outfile.write(json_obj)

print("--- %.2f seconds ---" % (time.time() - start_time))
