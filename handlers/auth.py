import tornado.web
from utils.account import authenticate
from .main import AuthBaseHandler


class LoginHandler(AuthBaseHandler): #登录的路由

    def get(self, *args, **kwargs):
        if self.current_user:#如果用户已经登录
            self.redirect('/')#那么就直接跳转到主页
        self.render('login.html')

    def post(self, *args, **kwargs):
        username = self.get_argument('username',None) #获取用户
        password = self.get_argument('password',None) #获取密码
        print(username)
        print(password)

        passed = authenticate(username, password)#调用用户密码校验函数
        print(passed)

        if passed:
            self.session.set('tudo_user_info',username)#将前面设置的session设置为username，保存用户登录信息
            self.redirect('/') #跳转主页路由

        else:
            self.write({'msg':'login fail'})#不通过，有问题

class LogoutHandler(AuthBaseHandler):#登出的路由

    def get(self):
        self.session.set('tudo_user_info','')#将用户的cookie清除
        self.redirect('/login')#返回登录路由

class SignupHandler(AuthBaseHandler):#注册的路由

    def get(self,*args,**kwargs):
        self.render('signup.html')

    def post(self):
        username = self.get_argument('username','')
        email = self.get_argument('email','')
        password1 = self.get_argument('password1','')
        password2 = self.get_argument('password2','')

        if username and password1 and password2:
            if password1 != password2:
                self.write({'mfg':'两次输入的密码不同'})
            else:
                self.write('注册成功')