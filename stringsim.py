from cryptography.fernet import Fernet


key = b'UzVBvZ7o4fnpBWy7gE8yaPLU0Yto7QJZb53xQ-JQhBo='
f = Fernet(key)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
string = 'okay'
print(f.encrypt(str.encode(string)))
token = f.encrypt(str.encode(string))
print(f.decrypt(token))

#
# ipaddress = request.remote_addr
# useragenthttp = headers['User-Agent']
# accept = headers['Accept']
# accept_encoding = headers['Accept-Encoding']
# accept_language = headers['Accept-Language']
# dnt = request.form['dnt']
# adblocker = request.form['adblocker']
# cookies = request.form['cookies']
# languagesjs = request.form['languagesjs']
# platform = request.form['platform']
# plugins = request.form['plugins']
# screenwidth = request.form['screenwidth']
# screenheight = request.form['screenheight']
# screendepth = request.form['screendepth']
# storagelocal = request.form['storagelocal']
# storagesession = request.form['storagesession']
# timezone = request.form['timezone']
# useragentjs = request.form['useragentjs']
# mimetypes = request.form['mimetypes']
# webGLvendor = request.form['webGLvendor']
# webGLrenderer = request.form['webGLrenderer']
# fonts = request.form['fonts']
# canvasprint = request.form['canvasprint']
# audiofingerprint = request.form['audiofingerprint']