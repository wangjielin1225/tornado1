from tornado.web import RequestHandler
class ItcastHandler(RequestHandler):
    def initialize(self, subject):
        self.subject = subject

    def get(self):
        self.write(self.subject)


import hashlib#系统自带的加密库 hash加密


USER_DATA = {#用于判断用户密码是否匹配
    'name':'tudo',
    'password':hashlib.md5('123qwe'.encode('utf8')).hexdigest(),#给密码加密，用hashlib来算法加密，utf8不加的话就是默认utf8
}

def authenticate(username,password):#用户密码匹配判断函数
    if username and password:
        hash_pw = hashlib.md5(password.encode()).hexdigest()#给输入的密码进行算法加密
        print(hash_pw)
        print(11111111111111111111111)
        print(username)
        print(USER_DATA['name'])
        print(USER_DATA['password'])
        if username == USER_DATA['name'] and hash_pw == USER_DATA['password']:#如果用户密码与数据库里面的用户密码匹配
            return True
    return False