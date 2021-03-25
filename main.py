import requests
from requests.models import Response

class YaUpLoader:
    def __init__(self, token: str):
        self.token = 'OAuth ' + token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        pos = file_path.rfind('\\')
        file_name = file_path[pos+1:len(file_path)]
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Accept': 'application/json', 'Authorization': self.token}
        params = {'path': file_name, 'overwrite': 'true'}
        resp = requests.get(url, params=params, headers=headers).json()
        upload_url = resp['href']
        resp = requests.put(upload_url, data=open(file_path, 'rb'))
        return resp

if __name__ == '__main__':
    uploader = YaUpLoader('your_token, ONLY token')
    result = uploader.upload('c:\\my_folder\\file.txt')