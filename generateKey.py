import os
import subprocess
import random
import codecs
from datetime import datetime

key_pass = ''
cn = ''  # 名字与姓氏
ou = ''  # 组织单位名称
o = ''  # 组织名称
base_str = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
max_index = len(base_str)-1

if os.path.exists('key.jks'):
    os.remove('key.jks')

key_pass_list = []
pass_len = random.randint(6, 32)
for i in range(pass_len):
    key_pass_list.append(base_str[random.randint(0, max_index)])

key_pass = "".join(key_pass_list)

cn_bool = bool(random.getrandbits(1))
ou_bool = bool(random.getrandbits(1))
o_bool = bool(random.getrandbits(1))

if not cn_bool and not ou_bool and not o_bool:
    cn_bool = True

if cn_bool:
    cn_len = random.randint(2, 10)
    for i in range(cn_len):
        cn = cn + base_str[random.randint(0, max_index)]

if ou_bool:
    ou_len = random.randint(5, 20)
    for i in range(ou_len):
        ou = ou + base_str[random.randint(0, max_index)]

if o_bool:
    o_len = random.randint(5, 20)
    for i in range(o_len):
        o = o + base_str[random.randint(0, max_index)]

cmd = f'keytool -genkeypair -alias key0 -keypass {key_pass} -keyalg RSA -keysize 2048 -validity 36500 -keystore key.jks -storepass {key_pass}'
#cmd = f'keytool -genkeypair -alias key0 -keypass {key_pass} -keyalg RSA -keysize 2048 -validity 36500 -keystore key.jks -storepass {key_pass}'
if cn_bool or ou_bool or o_bool:
    cmd = cmd + ' -dname '
    if cn_bool:
        cmd = cmd + f'CN={cn},'
    if ou_bool:
        cmd = cmd + f'OU={ou},'
    if o_bool:
        cmd = cmd + f'O={o},'
    cmd = cmd[:-1]

print(cmd)
now = datetime.now()
result = subprocess.getoutput(cmd)


info_list = [
    f'generate time:{now}\n',
    f'{cmd}\n\n',
    f'cn={cn} // 名字与姓氏\n',
    f'ou={ou} // 组织单位名称\n',
    f'o={o} // 组织名称\n\n',
    'signingConfigs {\n',
    '    release {\n',
    '        storeFile file(\'./key.jks\')//自行修改路径\n',
    f'        storePassword \'{key_pass}\'\n',
    '        keyAlias \'key0\'\n',
    f'        keyPassword \'{key_pass}\'\n', '    }\n}'
]

info = "".join(info_list)

if os.path.exists('info.txt'):
    os.remove('info.txt')

with codecs.open('info.txt', 'w', encoding='utf8') as f:
    f.write(info)



#keytool -genkeypair -alias key0 -keypass baojian -keyalg RSA -keysize 2048 -validity 36500 -keystore key.jks -storepass baojian -dname CN=ss,OU=sjlfsf,O=jfsljf