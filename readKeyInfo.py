import subprocess
import msvcrt

jks = input('请拖入jks文件:')
psw = input('password:')

cmd = f'keytool -v -list -keystore {jks} -storepass {psw}'
result = subprocess.getoutput(cmd)
print('\n')
print(result)

print('\n任意键关闭')
msvcrt.getch()
