import os

import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define,options

from handlers import main,auth


define('port',default='8000',help='Listening port',type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            ('/',main.IndexHandler),
            ('/explore', main.ExploreHandler),
            ('/post/(?P<post_id>[0-9]+)', main.PostHandler),
            ('/upload', main.UploadHandler),
            ('/login', auth.LoginHandler),
            ('/logout', auth.LogoutHandler),
            ('/signup', auth.SignupHandler),
        ]
        settings = dict(
            debug = True,
            template_path = 'templates',
            static_path = os.path.join(os.path.dirname(__file__),'static'),
            login_url = '/login',#要让必须登录之后才能访问首页
            cookie_secret = '95815451dasdwa1',#加密cookie的字符串
            pycket = { #固定写法packet，用于保存用户登录信息
                'engine':'redis',
                'storage':{
                    'host':'localhost',
                    'port':6379,
                    # 'password':''
                    'db_sessions': 5,
                    'db_notifications':11,
                    'max_connections':2 ** 30
                },
                'cookie':{
                    'expires_days':30,
                },
            }
        )

        super(Application,self).__init__(handlers,**settings)

application = Application()

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application.listen(options.port)
    print("Server start on port {}".format(str(options.port)))
    tornado.ioloop.IOLoop.current().start()