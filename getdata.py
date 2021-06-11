
import time
import requests
import zipfile
import io
import shutil

repo_link = 'https://github.com/microsoft/winget-pkgs/archive/refs/heads/master.zip'
data_dir = './data'
root_dir = './winget-pkgs-master'
manifests_dir = root_dir + '/manifests'


def download_repo():
    save_path = "./"
    request = requests.get(repo_link)
    zip_repo = zipfile.ZipFile(io.BytesIO(request.content))
    zip_repo.extractall(save_path)


start_time = time.time()
download_repo()
shutil.move(manifests_dir, data_dir)
shutil.rmtree(root_dir)
print("--- %.2f seconds ---" % (time.time() - start_time))
