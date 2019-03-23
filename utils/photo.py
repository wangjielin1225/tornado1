import glob
import os
from PIL import Image

def get_images(path):#函数意义是将某个路径下所有的文件会返回成一个列表
    images = []
    for file in glob.glob(path+'/*.jpg'):#所有目录下面为*.jpg的所有图片，
        images.append(file)#添加所有file，每个file都是一个全路径
    return images

def make_thumb(path):
    file,ext = os.path.splitext(os.path.basename(path))#分离路径
    im = Image.open(path)#打开路径文件
    im.thumbnail((200, 200))#进行减缩
    im.save('./statics/uploads/{}_{}x{}.jpg'.format(file,200,200),'JPEG')#保存在指定的绝对路径下