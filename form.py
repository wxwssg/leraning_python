# Author:wizard_wang
import getpass

_name = 'wizard_wang'
_pwd = '123456'
name = input("name:")
pwd =  getpass.getpass("pwd:")

if _name==name and _pwd==pwd:
    print('ok')
else:
    print('no')