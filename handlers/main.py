import tornado.web #导入包
import os
from pycket.session import SessionMixin
from utils import photo


class ExploreHandler(tornado.web.RequestHandler): #explore路由
    """
    Explore page,photo of other users 浏览页面和其他用户的照片
    """
    def get(self,*arg,**kwargs):
        images_urls = photo.get_images('./statics/uploads/thumbs')#打开指定路径下的文件
        self.render('explore.html',images=images_urls)#打开explore文件并将图片放上去

class PostHandler(tornado.web.RequestHandler):#post路由
    """
    Single photo page and maybe  单独的照片页
    """
    def get(self, *arg, **kwargs):
        self.render('post.html',post_id = kwargs['post_id']) #根据正则输入的内容，接收到kwargs（关键字），打开相应的图片


class UploadHandler(tornado.web.RequestHandler):
    """
    接收图片上传
    """
    def get(self,*arg,**kwargs):
        self.render('upload.html')#返回这个页面

    def post(self, *args, **kwargs): #接收文件
        img_files = self.request.files.get('newimg',None)#用RequestHandler的一种属性，接收表单上传的时候会有一个属性可以用get访问，默认为空
        for img_file in img_files:#可能同一个上传的文件会有多个文件，所以要用for循环去迭代它
            with open('./statics/uploads/thumbs/'+img_file['filename'], 'wb') as f:#表单提交上来是一个文件，需要用open来打开
                f.write(img_file['body'])#body就是文件的内容即图片

            photo.make_thumb('./statics/uploads/thumbs/'+img_file['filename']) #在创建文件的同时建立减缩图


        self.write({'msg': 'got file:{}'.format(img_files[0]['filename'])})#浏览器显示返回



class AuthBaseHandler(tornado.web.RequestHandler, SessionMixin):
    def get_current_user(self):
        return self.session.get('tudo_user_info')  # session是一种会话状态，跟数据库的session可能不一样

class IndexHandler(AuthBaseHandler):
    """
    Home page for user,photo feeds
    """

    @tornado.web.authenticated  # 要让首页必须登录之后才可以访问，用这个装饰器就可以，但是要在app.py里面设置login_url
    def get(self, *arg, **kwargs):
        images_path = os.path.join(self.settings.get('static_path'), 'uploads')
        images = photo.get_images(images_path)
        self.render('index.html', images=images)