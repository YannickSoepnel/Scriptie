from flask import Flask, request, render_template, make_response, redirect, session
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import BINARY
from flask_migrate import Migrate
from random import randint
from werkzeug.security import generate_password_hash, check_password_hash
import flask_login
from pymitter import EventEmitter
from difflib import SequenceMatcher
import datetime
from cryptography.fernet import Fernet
from datetime import timedelta
import time
import atexit
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler
import uuid
import hashlib
# import retention

key = ''
f = Fernet(key)

ee = EventEmitter()

getpost = []

app = Flask(__name__)
app.secret_key = 'ihvhbs93'

#Docker
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://:@172.19.0.2:5432/fingerprint"
#Local
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://:@localhost:5432/fingerprint"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@ee.on("get-event", ttl=10)
def handler1():
    # print()
    print("get-event called")


@ee.on("post-event", ttl=10)
def handler2():
    print(getpost)
    print("post-event called")

class iptofingerprintsModel(db.Model):
    __tablename__ = 'iptofingerprint'

    id = db.Column(db.Integer, primary_key=True)
    ipaddress = db.Column(db.String())
    hash = db.Column(db.String())
    useragenthttp = db.Column(db.String())
    useragent = db.Column(db.LargeBinary())
    accept = db.Column(db.String())
    accept_encoding = db.Column(db.String())
    accept_language = db.Column(db.String())
    dnt = db.Column(db.String())
    adblocker = db.Column(db.String())
    cookies = db.Column(db.String())
    languagesjs = db.Column(db.String())
    platform = db.Column(db.String())
    plugins = db.Column(db.String())
    screenwidth = db.Column(db.String())
    screenheight = db.Column(db.String())
    screendepth = db.Column(db.String())
    storagelocal = db.Column(db.String())
    storagesession = db.Column(db.String())
    timezone = db.Column(db.String())
    useragentjs = db.Column(db.String())
    mimetypes = db.Column(db.String())
    webGLvendor = db.Column(db.String())
    webGLrenderer = db.Column(db.String())
    fonts = db.Column(db.String())
    canvasprint = db.Column(db.String())
    audiofingerprint = db.Column(db.String())
    cookie_id = db.Column(db.String())
    request_header = db.Column(db.String())
    timestamp = db.Column(db.DateTime)

    def __init__(self, ipaddress, hash, useragenthttp, useragent, accept, accept_encoding, accept_language, dnt, adblocker,
                 cookies, languagesjs, platform, plugins, screenwidth, screenheight, screendepth, storagelocal,
                 storagesession, timezone, useragentjs, mimetypes, webGLvendor, webGLrenderer, fonts, canvasprint,
                 audiofingerprint, cookie_id, request_header, timestamp):

        self.ipaddress = ipaddress
        self.hash = hash
        self.useragenthttp = useragenthttp
        self.useragent = useragent
        self.accept = accept
        self.accept_encoding = accept_encoding
        self.accept_language = accept_language
        self.dnt = dnt
        self.adblocker = adblocker
        self.cookies = cookies
        self.languagesjs = languagesjs
        self.platform = platform
        self.plugins = plugins
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.screendepth = screendepth
        self.storagelocal = storagelocal
        self.storagesession = storagesession
        self.timezone = timezone
        self.useragentjs = useragentjs
        self.mimetypes = mimetypes
        self.webGLvendor = webGLvendor
        self.webGLrenderer = webGLrenderer
        self.fonts = fonts
        self.canvasprint = canvasprint
        self.audiofingerprint = audiofingerprint
        self.cookie_id = cookie_id
        self.request_header = request_header
        self.timestamp = timestamp

class cookietofingerprintModel(db.Model):
    __tablename__ = 'cookietofingerprint'

    id = db.Column(db.Integer, primary_key=True)
    ipaddress = db.Column(db.String())
    hash = db.Column(db.String())
    useragenthttp = db.Column(db.String())
    accept = db.Column(db.String())
    accept_encoding = db.Column(db.String())
    accept_language = db.Column(db.String())
    dnt = db.Column(db.String())
    adblocker = db.Column(db.String())
    cookies = db.Column(db.String())
    languagesjs = db.Column(db.String())
    platform = db.Column(db.String())
    plugins = db.Column(db.String())
    screenwidth = db.Column(db.String())
    screenheight = db.Column(db.String())
    screendepth = db.Column(db.String())
    storagelocal = db.Column(db.String())
    storagesession = db.Column(db.String())
    timezone = db.Column(db.String())
    useragentjs = db.Column(db.String())
    mimetypes = db.Column(db.String())
    webGLvendor = db.Column(db.String())
    webGLrenderer = db.Column(db.String())
    fonts = db.Column(db.String())
    canvasprint = db.Column(db.String())
    audiofingerprint = db.Column(db.String())
    cookie_id = db.Column(db.String())
    request_header = db.Column(db.String())
    timestamp = db.Column(db.DateTime)

    def __init__(self, ipaddress, hash, useragenthttp, accept, accept_encoding, accept_language, dnt, adblocker,
                 cookies, languagesjs, platform, plugins, screenwidth, screenheight, screendepth, storagelocal,
                 storagesession, timezone, useragentjs, mimetypes, webGLvendor, webGLrenderer, fonts, canvasprint,
                 audiofingerprint, cookie_id, request_header, timestamp):

        self.ipaddress = ipaddress
        self.hash = hash
        self.useragenthttp = useragenthttp
        self.accept = accept
        self.accept_encoding = accept_encoding
        self.accept_language = accept_language
        self.dnt = dnt
        self.adblocker = adblocker
        self.cookies = cookies
        self.languagesjs = languagesjs
        self.platform = platform
        self.plugins = plugins
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.screendepth = screendepth
        self.storagelocal = storagelocal
        self.storagesession = storagesession
        self.timezone = timezone
        self.useragentjs = useragentjs
        self.mimetypes = mimetypes
        self.webGLvendor = webGLvendor
        self.webGLrenderer = webGLrenderer
        self.fonts = fonts
        self.canvasprint = canvasprint
        self.audiofingerprint = audiofingerprint
        self.cookie_id = cookie_id
        self.request_header = request_header
        self.timestamp = timestamp

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))

def check_cookie_id(cookie_id):
    pass
    # fingerprints = cookietofingerprintModel.query.filter_by(cookie_id=str(cookie_id)).all()
    # if (len(fingerprints) >= 1):
    #     print('bestaat al')
    #     return 'bestaat'
    # else:
    #     pass


@app.route('/', methods=["GET", "POST"])
def hello_world():
    # cookie_id = randint(0, 100)
    # print(cookie_id)
    cookie_id = uuid.uuid4()
    # cookie_id = 40
    print(uuid.uuid4())
    # print('cookie_id random')
    # print(cookie_id)
    if request.method == 'GET':
        headers = request.headers
        ip_address = request.remote_addr
        useragenthttp = headers['User-Agent']
        useragent = f.encrypt(str.encode(headers['User-Agent']))
        # print(f.encrypt(str.encode(headers['User-Agent'])))
        accept = headers['Accept']
        accept_encoding = headers['Accept-Encoding']
        accept_language = headers['Accept-Language']
        dnt = "NoJS"
        adblocker = "NoJS"
        cookies = "NoJS"
        languagesjs = "NoJS"
        platform = "NoJS"
        plugins = "NoJS"
        screenwidth = "NoJS"
        screenheight = "NoJS"
        screendepth = "NoJS"
        storagelocal = "NoJS"
        storagesession = "NoJS"
        timezone = "NoJS"
        useragentjs = "NoJS"
        mimetypes = "NoJS"
        webGLvendor = "NoJS"
        webGLrenderer = "NoJS"
        fonts = "NoJS"
        canvasprint = "NoJS"
        audiofingerprint = "NoJS"
        timestamp = datetime.datetime.now()
        hash = hashlib.md5(str([headers, ip_address, useragenthttp, accept, accept_encoding, accept_language, dnt, adblocker, cookies,
                                            languagesjs, platform, plugins, screenwidth, screenheight, screendepth, storagelocal, storagesession,
                                            timezone, useragentjs, mimetypes, webGLvendor, webGLrenderer, fonts, canvasprint, audiofingerprint]).encode()).hexdigest()

        ip_address = request.remote_addr
        useragenthttp = headers['User-Agent']
        accept = headers['Accept']
        accept_encoding = headers['Accept-Encoding']
        accept_language = headers['Accept-Language']
        dnt = "NoJS"
        adblocker = "NoJS"
        cookies = "NoJS"
        languagesjs = "NoJS"
        platform = "NoJS"
        plugins = "NoJS"
        screenwidth = "NoJS"
        screenheight = "NoJS"
        screendepth = "NoJS"
        storagelocal = "NoJS"
        storagesession = "NoJS"
        timezone = "NoJS"
        useragentjs = "NoJS"
        mimetypes = "NoJS"
        webGLvendor = "NoJS"
        webGLrenderer = "NoJS"
        fonts = "NoJS"
        canvasprint = "NoJS"
        audiofingerprint = "NoJS"
        f.encrypt(str.encode(headers['User-Agent']))

        if (not request.cookies):
            # Checken of cookie_ID voorkomt in database: Zoja genereer nieuwe cookie_ID,
            # Zo niet gebruik dan deze cookie_ID
            while(len(cookietofingerprintModel.query.filter_by(cookie_id=str(cookie_id)).all()) >= 1):
                cookie_id = randint(0, 100)
            # fingerprints = cookietofingerprintModel.query.filter_by(cookie_id=str(cookie_id)).all()
            # # if (len(fingerprints) >= 1):
            # #     print('bestaat al')
            # #     return 'bestaat'
            # if(check_cookie_id(cookie_id) == 'bestaat'):
            #     cookie_id = randint(0, 100)
            #     # print('eerste keer bestaat al')
            # if(check_cookie_id(cookie_id) == 'bestaat'):
            #     # print('tweede keer bestaat al')
            #     cookie_id = randint(0, 100)
            # else:
                print('not cookie')
                print(cookie_id)
            #Fingerprint in database zetten met request_header = "GET"
            check_ip_fingerprints = iptofingerprintsModel.query.filter_by(ipaddress=ip_address,
                                                                          request_header="GET").all()
            if (len(check_ip_fingerprints) == 0):
                new_ip_fingerprint = iptofingerprintsModel(hash=hash, ipaddress=ip_address, useragenthttp=f.encrypt(str.encode(useragenthttp)), accept=accept, accept_encoding=accept_encoding,
                                                           accept_language=accept_language, dnt=dnt, adblocker=adblocker, cookies=cookies, languagesjs=languagesjs,
                                                           platform=platform, plugins=plugins, screenwidth=screenwidth, screenheight=screenheight, screendepth=screendepth,
                                                           storagelocal=storagelocal, storagesession=storagesession, timezone=timezone, useragentjs=useragentjs,
                                                           mimetypes=mimetypes, webGLvendor=webGLvendor, webGLrenderer=webGLrenderer, fonts=fonts, canvasprint=canvasprint,
                                                           audiofingerprint=audiofingerprint,cookie_id=cookie_id,request_header="GET", timestamp=timestamp)
                db.session.add(new_ip_fingerprint)
                db.session.commit()
            else:
                # Kijken of nieuwe fingerprint hetzelfde is als de oude, Zo niet schrijf nieuwe fingerprint naar DB
                # anders oude fingerprint cookie_ID aanpassen met nieuwe cookie_id
                new_fingerprintstring = [useragenthttp, accept, accept_encoding, accept_language, dnt, adblocker,
                 cookies, languagesjs, platform, plugins, screenwidth, screenheight, screendepth, storagelocal,
                 storagesession, timezone, useragentjs, mimetypes, webGLvendor, webGLrenderer, fonts, canvasprint,
                 audiofingerprint]
                for finger in check_ip_fingerprints:
                    fingerprintstring = [finger.useragenthttp, finger.accept, finger.accept_encoding, finger.accept_language,
                                         finger.dnt, finger.adblocker, finger.cookies, finger.languagesjs, finger.platform,
                                         finger.plugins, finger.screenwidth, finger.screenheight, finger.screendepth, finger.storagelocal,
                                         finger.storagesession, finger.timezone, finger.useragentjs, finger.mimetypes, finger.webGLvendor,
                                         finger.webGLrenderer, finger.fonts, finger.canvasprint, finger.audiofingerprint]
                    if (SequenceMatcher(None, str(new_fingerprintstring), str(fingerprintstring)).ratio() > 0.75):
                    # if (fingerprintstring == new_fingerprintstring):
                        ratio = SequenceMatcher(None, str(new_fingerprintstring), str(fingerprintstring)).ratio()
                        print(ratio)
                        iptofingerprintsModel.query.filter_by(id=finger.id).delete()
                        print('fingerprints zijn hetzelfde')
                    else:
                        print('niet helemaal zelfde')
                        ratio = SequenceMatcher(None, str(new_fingerprintstring), str(fingerprintstring)).ratio()
                        print(ratio)

                new_ip_fingerprint = iptofingerprintsModel(hash=hash, ipaddress=ip_address, useragenthttp=useragenthttp, accept=accept, accept_encoding=accept_encoding,
                                                           accept_language=accept_language, dnt=dnt, adblocker=adblocker, cookies=cookies, languagesjs=languagesjs,
                                                           platform=platform, plugins=plugins, screenwidth=screenwidth, screenheight=screenheight, screendepth=screendepth,
                                                           storagelocal=storagelocal, storagesession=storagesession, timezone=timezone, useragentjs=useragentjs,
                                                           mimetypes=mimetypes, webGLvendor=webGLvendor, webGLrenderer=webGLrenderer, fonts=fonts, canvasprint=canvasprint,
                                                           audiofingerprint=audiofingerprint,cookie_id=cookie_id,request_header="GET", timestamp=timestamp)
                db.session.add(new_ip_fingerprint)
                db.session.commit()


            new_cookie_fingerprint = cookietofingerprintModel(hash=hash, ipaddress=ip_address, useragenthttp=useragenthttp, accept=accept, accept_encoding=accept_encoding,
                                                           accept_language=accept_language, dnt=dnt, adblocker=adblocker, cookies=cookies, languagesjs=languagesjs,
                                                           platform=platform, plugins=plugins, screenwidth=screenwidth, screenheight=screenheight, screendepth=screendepth,
                                                           storagelocal=storagelocal, storagesession=storagesession, timezone=timezone, useragentjs=useragentjs,
                                                           mimetypes=mimetypes, webGLvendor=webGLvendor, webGLrenderer=webGLrenderer, fonts=fonts, canvasprint=canvasprint,
                                                           audiofingerprint=audiofingerprint,cookie_id=cookie_id,request_header="GET", timestamp=timestamp)
            db.session.add(new_cookie_fingerprint)
            db.session.commit()
            # resp = make_response(render_template('tinka-new/Tinka.html', cookie_id=cookie_id))
            resp = make_response(render_template('finger.html', cookie_id=cookie_id))
            resp.set_cookie('fingerprint', str(cookie_id))
            print('cookie geset met ID:' + str(cookie_id))
            return resp
        else:
            # Ophalen cookie_id uit cookie. Vervolgens kijken of fingerprint overeenkomt met fingerprint die er staat
            # Zo niet plaats GET fingerprint in de tabel cookie DB.
            cookie_id = request.cookies['fingerprint']
            check_ip_fingerprints = iptofingerprintsModel.query.filter_by(ipaddress=ip_address, cookie_id=cookie_id,
                                                                          request_header="GET").all()
            if (len(check_ip_fingerprints) == 0):
                new_ip_fingerprint = iptofingerprintsModel(hash=hash, ipaddress=ip_address, useragenthttp=useragenthttp, useragent=useragent, accept=accept, accept_encoding=accept_encoding,
                                                           accept_language=accept_language, dnt=dnt, adblocker=adblocker, cookies=cookies, languagesjs=languagesjs,
                                                           platform=platform, plugins=plugins, screenwidth=screenwidth, screenheight=screenheight, screendepth=screendepth,
                                                           storagelocal=storagelocal, storagesession=storagesession, timezone=timezone, useragentjs=useragentjs,
                                                           mimetypes=mimetypes, webGLvendor=webGLvendor, webGLrenderer=webGLrenderer, fonts=fonts, canvasprint=canvasprint,
                                                           audiofingerprint=audiofingerprint,cookie_id=cookie_id,request_header="GET", timestamp=timestamp)
                db.session.add(new_ip_fingerprint)
                db.session.commit()
            else:
                # Oude fingerprint wijzigen met nieuwe fingerprint aangezien cookie_ID zelfde is, is apparaat ook hetzelfde
                pass
            #Ophalen bestaande GET fingerprint in database mbv cookie_ID
            try:
                fingerprint = cookietofingerprintModel.query.filter_by(cookie_id=str(cookie_id)).first()
                if(fingerprint is None):
                    new_cookie_fingerprint = cookietofingerprintModel(hash=hash, ipaddress=ip_address, useragenthttp=useragenthttp,
                                                                      accept=accept, accept_encoding=accept_encoding,
                                                                      accept_language=accept_language, dnt=dnt,
                                                                      adblocker=adblocker, cookies=cookies,
                                                                      languagesjs=languagesjs,
                                                                      platform=platform, plugins=plugins,
                                                                      screenwidth=screenwidth,
                                                                      screenheight=screenheight,
                                                                      screendepth=screendepth,
                                                                      storagelocal=storagelocal,
                                                                      storagesession=storagesession, timezone=timezone,
                                                                      useragentjs=useragentjs,
                                                                      mimetypes=mimetypes, webGLvendor=webGLvendor,
                                                                      webGLrenderer=webGLrenderer, fonts=fonts,
                                                                      canvasprint=canvasprint,
                                                                      audiofingerprint=audiofingerprint,
                                                                      cookie_id=cookie_id, request_header="GET", timestamp=timestamp)
                    db.session.add(new_cookie_fingerprint)
                else:
                    #Aanpassen nieuwe waarde
                    fingerprint.hash = hash
                    fingerprint.ipaddress = request.remote_addr
                    fingerprint.useragenthttp = headers['User-Agent']
                    fingerprint.accept = headers['Accept']
                    fingerprint.accept_encoding = headers['Accept-Encoding']
                    fingerprint.accept_language = headers['Accept-Language']
                    fingerprint.dnt = dnt
                    fingerprint.adblocker = adblocker
                    fingerprint.cookies = cookies
                    fingerprint.languagesjs = languagesjs
                    fingerprint.platform = platform
                    fingerprint.plugins = plugins
                    fingerprint.screenwidth = screenwidth
                    fingerprint.screenheight = screenheight
                    fingerprint.screendepth = screendepth
                    fingerprint.storagelocal = storagelocal
                    fingerprint.storagesession = storagesession
                    fingerprint.timezone = timezone
                    fingerprint.useragentjs = useragentjs
                    fingerprint.mimetypes = mimetypes
                    fingerprint.webGLvendor = webGLvendor
                    fingerprint.webGLrenderer = webGLrenderer
                    fingerprint.fonts = fonts
                    fingerprint.canvasprint = canvasprint
                    fingerprint.audiofingerprint = audiofingerprint
                    fingerprint.request_header = "GET"
                    fingerprint.timestamp = timestamp
            except:
                pass
            db.session.commit() #Nieuwe waardes committen
            # resp = make_response(render_template('tinka-new/tinka.html', cookie_id=cookie_id))
            resp = make_response(render_template('finger.html', cookie_id=cookie_id))
            print(request.cookies['fingerprint'])
            print('GET')
            return resp
        # new_fingerprint = FingerprintsModel(ipaddress=ip_address, useragenthttp=useragenthttp, useragentjs=useragentjs, platform=platform,
        #                                     languagesjs=languagesjs, cookie_id=cookie_id, request_header="GET")
        # db.session.add(new_fingerprint)
        # db.session.commit()
    # return render_template('finger.html')

@app.route('/login', methods=["POST", "GET"])
def login_page():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form.get('username')
        password = request.form.get('password')
        user = users.query.filter_by(username=username).first()
        if(user is None):
            msg = 'Geen geldige gebruikersnaam of wachtwoord!'
        elif(check_password_hash(user.password, password)):
            session['loggedin'] = True
            session['username'] = username
            print('ingelogd')
            return redirect(('/dashboard-ip'))
        else:
            msg = 'Geen geldige gebruikersnaam of wachtwoord!'
    # if(user is None):
    #     pass
    # else:
    #     if(not user or not check_password_hash(user.password, password)):
    #         flash('Please check your login details and try again.')
    #     else:
    #         print(username)
    #         print(password)
    return render_template('login.html', msg=msg)

@app.route('/key', methods=["POST"])
def get_key():
    if request.method == 'POST':
        key = request.form['dnt']
        print(key)
        print(type(key))

    return request.method

@app.route('/test')
def testing():
    cookiefingerprint = cookietofingerprintModel.query.all()
    ipfingerprint = iptofingerprintsModel.query.all()

    for finger in ipfingerprint:
        print(finger.useragent)
        print(type(finger.useragent))
        print(f.decrypt(finger.useragent))
        # token = str.encode(finger.useragent)
        # print(token)
        # print(type(token))
        # print(f.decrypt(token))
    return 'ok'

@app.route('/post', methods=["POST"])
def get_js():
    if request.method == 'POST':
        ip_address = request.remote_addr
        # ip_address = "127.0.0.1"
        cookie_id = request.form['cookieid']
        headers = request.headers
        useragenthttp = headers['User-Agent']
        # accept = headers['Accept']
        # print(accept)
        accept_encoding = headers['Accept-Encoding']
        accept_language = headers['Accept-Language']
        dnt = request.form['dnt']
        adblocker = request.form['adblocker']
        cookies = request.form['cookies']
        languagesjs = request.form['languagesjs']
        platform = request.form['platform']
        plugins = request.form['plugins']
        screenwidth = request.form['screenwidth']
        screenheight = request.form['screenheight']
        screendepth = request.form['screendepth']
        storagelocal = request.form['storagelocal']
        storagesession = request.form['storagesession']
        timezone = request.form['timezone']
        useragentjs = request.form['useragentjs']
        mimetypes = request.form['mimetypes']
        webGLvendor = request.form['webGLvendor']
        webGLrenderer = request.form['webGLrenderer']
        fonts = request.form['fonts']
        canvasprint = request.form['canvasprint']
        audiofingerprint = request.form['audiofingerprint']
        # cookie_id = 84
        # print(request.form)
        # Controleren of cookie_ID voor komt in database
        # Zoja
        fingerprint_ip = iptofingerprintsModel.query.filter_by(ipaddress=ip_address, cookie_id=str(cookie_id)).first()
        accept = fingerprint_ip.accept
        fingerprint_ip.hash = hashlib.md5(str([headers, ip_address, useragenthttp, accept, accept_encoding, accept_language, dnt, adblocker, cookies,
                 languagesjs, platform, plugins, screenwidth, screenheight, screendepth, storagelocal, storagesession,
                 timezone, useragentjs, mimetypes, webGLvendor, webGLrenderer, fonts, canvasprint,
                 audiofingerprint]).encode()).hexdigest()
        fingerprint_ip.ipaddress = request.remote_addr
        # fingerprint_ip.useragenthttp = headers['User-Agent']
        fingerprint_ip.useragenthttp = f.encrypt(str.encode(headers['User-Agent']))
        print('okay')
        print(f.encrypt(str.encode(headers['User-Agent'])))
        fingerprint_ip.accept = accept
        fingerprint_ip.accept_encoding = headers['Accept-Encoding']
        fingerprint_ip.accept_language = headers['Accept-Language']
        fingerprint_ip.dnt = request.form['dnt']
        fingerprint_ip.adblocker = request.form['adblocker']
        fingerprint_ip.cookies = request.form['cookies']
        fingerprint_ip.languagesjs = request.form['languagesjs']
        fingerprint_ip.platform = request.form['platform']
        fingerprint_ip.plugins = request.form['plugins']
        fingerprint_ip.screenwidth = request.form['screenwidth']
        fingerprint_ip.screenheight = request.form['screenheight']
        fingerprint_ip.screendepth = request.form['screendepth']
        fingerprint_ip.storagelocal = request.form['storagelocal']
        fingerprint_ip.storagesession = request.form['storagesession']
        fingerprint_ip.timezone = request.form['timezone']
        fingerprint_ip.useragentjs = request.form['useragentjs']
        fingerprint_ip.mimetypes = request.form['mimetypes']
        fingerprint_ip.webGLvendor = request.form['webGLvendor']
        fingerprint_ip.webGLrenderer = request.form['webGLrenderer']
        fingerprint_ip.fonts = request.form['fonts']
        fingerprint_ip.canvasprint = request.form['canvasprint']
        fingerprint_ip.audiofingerprint = request.form['audiofingerprint']
        fingerprint_ip.request_header = "POST"
        fingerprint_ip.timestamp = datetime.datetime.now()

        iptofingerprintsModel.query.filter_by(ipaddress=ip_address, cookie_id=str(cookie_id), request_header="GET").delete()
        #
        check_ip_fingerprints = iptofingerprintsModel.query.filter_by(ipaddress=ip_address,
                                                                      request_header="POST").all()
        if (len(check_ip_fingerprints) == 0):
            print('none')
            pass
        else:
            headers = request.headers
            new_fingerprintstring = [headers['User-Agent'], accept, headers['Accept-Encoding'], headers['Accept-Language'],
                                    request.form['dnt'], request.form['adblocker'], request.form['cookies'], request.form['languagesjs'],
                                    request.form['platform'], request.form['plugins'], request.form['screenwidth'], request.form['screenheight'],
                                    request.form['screendepth'], request.form['storagelocal'], request.form['storagesession'], request.form['timezone'],
                                    request.form['useragentjs'], request.form['mimetypes'], request.form['webGLvendor'], request.form['webGLrenderer'],
                                    request.form['fonts'], request.form['canvasprint'], request.form['audiofingerprint']]
            for finger in check_ip_fingerprints:
                if(finger.cookie_id == cookie_id):
                    pass
                else:
                    fingerprintstring = [finger.useragenthttp, finger.accept, finger.accept_encoding, finger.accept_language,
                                         finger.dnt, finger.adblocker, finger.cookies, finger.languagesjs, finger.platform,
                                         finger.plugins, finger.screenwidth, finger.screenheight, finger.screendepth, finger.storagelocal,
                                         finger.storagesession, finger.timezone, finger.useragentjs, finger.mimetypes, finger.webGLvendor,
                                         finger.webGLrenderer, finger.fonts, finger.canvasprint, finger.audiofingerprint]
                    #String similarity 0,75
                    if(SequenceMatcher(None, str(new_fingerprintstring), str(fingerprintstring)).ratio() > 0.75):
                        ratio = SequenceMatcher(None, str(new_fingerprintstring), str(fingerprintstring)).ratio()
                        print(ratio)
                    # if(fingerprint_string == new_fingerprintstring):
                        iptofingerprintsModel.query.filter_by(id=finger.id).delete()
                    else:
                        print('niet helemaal zelfde')
                        ratio = SequenceMatcher(None, str(new_fingerprintstring), str(fingerprintstring)).ratio()
                        print(ratio)

        fingerprint_cookie = cookietofingerprintModel.query.filter_by(cookie_id=str(cookie_id)).first()

        fingerprint_cookie.hash = hashlib.md5(str([headers, ip_address, useragenthttp, accept, accept_encoding, accept_language, dnt, adblocker, cookies,
                 languagesjs, platform, plugins, screenwidth, screenheight, screendepth, storagelocal, storagesession,
                 timezone, useragentjs, mimetypes, webGLvendor, webGLrenderer, fonts, canvasprint,
                 audiofingerprint]).encode()).hexdigest()
        fingerprint_cookie.ipaddress = request.remote_addr
        fingerprint_cookie.useragenthttp = headers['User-Agent']
        fingerprint_cookie.accept = accept
        fingerprint_cookie.accept_encoding = headers['Accept-Encoding']
        fingerprint_cookie.accept_language = headers['Accept-Language']
        fingerprint_cookie.dnt = request.form['dnt']
        fingerprint_cookie.adblocker = request.form['adblocker']
        fingerprint_cookie.cookies = request.form['cookies']
        fingerprint_cookie.languagesjs = request.form['languagesjs']
        fingerprint_cookie.platform = request.form['platform']
        fingerprint_cookie.plugins = request.form['plugins']
        fingerprint_cookie.screenwidth = request.form['screenwidth']
        fingerprint_cookie.screenheight = request.form['screenheight']
        fingerprint_cookie.screendepth = request.form['screendepth']
        fingerprint_cookie.storagelocal = request.form['storagelocal']
        fingerprint_cookie.storagesession = request.form['storagesession']
        fingerprint_cookie.timezone = request.form['timezone']
        fingerprint_cookie.useragentjs = request.form['useragentjs']
        fingerprint_cookie.mimetypes = request.form['mimetypes']
        fingerprint_cookie.webGLvendor = request.form['webGLvendor']
        fingerprint_cookie.webGLrenderer = request.form['webGLrenderer']
        fingerprint_cookie.fonts = request.form['fonts']
        fingerprint_cookie.canvasprint = request.form['canvasprint']
        fingerprint_cookie.audiofingerprint = request.form['audiofingerprint']
        fingerprint_cookie.request_header = "POST"
        fingerprint_cookie.timestamp = datetime.datetime.now()
        db.session.commit()
    return request.method

@app.route('/dashboard-ip')
def dashboard_ip():
    string = 'okay'
    token = f.encrypt(str.encode(string))
    if 'loggedin' in session:
        ipadressen = iptofingerprintsModel.query.all()
        # for fingerprint in ipadressen:
            # fingerprint.ipaddress = str(f.decrypt(fingerprint.ipaddress),'utf-8')
            # fingerprint.useragent = str(f.decrypt(fingerprint.useragent),'utf-8')
            # print(fingerprint.useragent)
    # ids = 27
    # iptofingerprintsModel.query.filter_by(id=ids).delete()
    # db.session.commit()
    # print('ok')
        return render_template('dashboard-ip.html', ipadressen=ipadressen, token=token)
    else:
        return redirect('/login')

@app.route('/dashboard-cookie')
def dashboard_cookie():
    if 'loggedin' in session:
        cookiefingerprint = cookietofingerprintModel.query.all()
    # ids = 27
    # iptofingerprintsModel.query.filter_by(id=ids).delete()
    # db.session.commit()
    # print('ok')
        return render_template('dashboard-cookie.html', cookiefingerprint=cookiefingerprint)
    else:
        return redirect('/login')

@app.route('/tinka')
def tinkaweb():
    return render_template('tinka-new/tinka.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect('/login')

# retention.retention_date()
# if __name__ == '__main__':
#     app.run(host="0.0.0.0",
#             port=5000,
#             debug=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=5000,
            debug=True,
            static_folder='web/static',
            template_folder='templates/')
