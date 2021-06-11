import os

path = './data/manifests'


def get_company_data(ch_path):
    return [os.path.join(path, x) for x in os.listdir(ch_path)]


def extract_data(root_path):
    ch_dir = [os.path.join(path, x) for x in os.listdir(root_path)]
    data = []
    for ch_path in ch_dir:
        for company_path in get_company_data(ch_path):
            data.append(company_path)
    return data


data = extract_data(path)
print(data)
