import os
if not os.path.isdir('dbs'):
    os.mkdir('dbs')
try:
    import telebot, json, os, time, re, threading, schedule
    from telebot import TeleBot
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
    import asyncio
    from apis import *
    import time
    import datetime
except:
    os.system('python3 -m pip install telebot pyrogram tgcrypto kvsqlite pyromod==1.4 schedule')
    import telebot, json, os, time, schedule
    from telebot import TeleBot
    from kvsqlite.sync import Client as uu
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
    import asyncio
    import datetime 
    import requests 
   
    pass
db = uu('dbs/hameeed.ss', 'rshq')\

print(db)
def load_token_from_file():
    if os.path.exists('session_cookie.txt'):
        with open('session_cookie.txt', 'r') as f:
            return f.read().strip()
    return None
def extract_freepik_id(url):
    match = re.search(r'_(\d+)\.htm', url)
    if match:
        return match.group(1)
    return None


session_cookie = load_token_from_file() or ''  
with open('messages.json', 'r', encoding='utf-8') as f:
    messages = json.load(f)
MAX_MESSAGES_PER_DAY = 100
mm="︎مرحبا بكم في اقوي بوت رشق علي الساحه"
link_price=1
bk = mk(row_width=1).add(btn('رجوع', callback_data='back'))
bot = TeleBot(token="7326958688:AAG__Ylc-gihaeM7UX4o1gVkXXbRGe4F9Ho")
stypes = ['member', 'administrator', 'creator']
if not db.get('accounts'):
    db.set('accounts', [])
    pass
admin = 6698161283 
if not db.get("admins"):
    db.set('admins', [admin, ])
if not db.get('badguys'):
    db.set('badguys', [])

if not db.get('force'):
    db.set('force', [])
if not db.get('subscription'):
    db.set('subscription', [])    
def force(channel, userid):
    try:
        x = bot.get_chat_member(channel, userid)
        print(x)
    except:
        return True
    if str(x.status) in stypes:
        print(x)
        return True
    else:
        print(x)
        return False
def addord():
    if not db.get('orders'):
        db.set('orders', 1)
        return True
    else:
        d = db.get('orders')
        d+=1
        db.set('orders', d)
        return True

@bot.message_handler(regexp='^/start$')
def start_message(message):
    user_id = message.from_user.id
    
  
    keys = mk(row_width=2)
    if user_id in db.get("admins") :
        keys_ = mk()
        btn01 = btn('🤍الاحصائيات', callback_data='stats')
        btn02 = btn("⚠️اذاعة", callback_data='cast')
        btn05, btn06 = btn('➖حظر شخص', callback_data='banone'), btn('فك حظر', callback_data='unbanone')
       
        btna = btn('➕تفعيل ViP', callback_data='addsubscription')
        btnl = btn('➖الغاء ViP', callback_data='delsubscription')
        leave = btn('➖   معرفه المتبقي من الاشتراك ', callback_data='checksubscription')
        
        keys_.add(btn01, btn02)
        keys_.add(btn05, btn06)
        keys_.add(leave)
        btn11 = btn('تعيين قنوات الاشتراك', callback_data='setforce')
        les = btn('➖خصم نقاط', callback_data='lespoints')
        btn10 = btn('اضافه نقاط ', callback_data='addpoints')
        btn03 = btn('➕اضافة ادمن', callback_data='addadmin')
        btn04 = btn('➖مسح ادمن', callback_data='deladmin')
        btn012 = btn('⚠️الادمنية ', callback_data='admins')
        btn013 = btn(' المشتركين', callback_data='subscription')
       
        keys_.add(btn03, btn04)
        keys_.add(btn10, btn11)
        keys_.add(btn012, les)
         
        
        keys_.add(btna, btnl)
        keys_.add(btn013)
      
        bot.reply_to(message, messages['admin_panel_message'], reply_markup=keys_)
    if user_id in db.get('badguys'): return
    if not db.get(f'user_{user_id}'):
        do = db.get('force')
        if do != None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                if str(x.status) in stypes:
                    pass
                else:
                    channel_button = btn(messages['channel_button_text'], url=f'https://t.me/{channel}')
                    check_button = btn(messages['check_subscription_button_text'], callback_data='check_subscription')
                    keyboard = mk().add(channel_button).add(check_button)
                    bot.reply_to(message, messages['subscribe_channel_message'], reply_markup=keyboard)
                    return
        data = {'id': user_id, 'users': [], 'coins': 0, 'premium': False}
        set_user(user_id, data)
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        
        
        
        
        return bot.reply_to(message, messages['welcome_message'])
    do = db.get('force')
    if do is not None:
        for channel in do:
            x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
            if str(x.status) in stypes:
                pass
            else:
                channel_button = btn(messages['channel_button_text'], url=f'https://t.me/{channel}')
                check_button = btn(messages['check_subscription_button_text'], callback_data='check_subscription')
                keyboard = mk().add(channel_button).add(check_button)
                bot.reply_to(message, messages['subscribe_channel_message'], reply_markup=keyboard)
                return
    
    
   
   

    return bot.reply_to(message,messages['welcome_message'])
@bot.message_handler(regexp='^/start (.*)')
def start_asinvite(message):
    join_user = message.from_user.id

    to_user = int(message.text.split("/start ")[1])
    if join_user == to_user:
        start_message(message)
        bot.send_message(join_user,f'لا يمكنك الدخول عبر الرابط الخاص بك ❌')
        return
    if not check_user(join_user):
        someinfo = get(to_user)
        if join_user in someinfo['users']:
            start_message(message)
            return
        else:
            dd = link_price
            someinfo['users'].append(join_user)
            someinfo['coins'] = int(someinfo['coins']) + dd
            info = {'coins': 0, 'id': join_user, 'premium': False, "users": []}
            set_user(join_user, info)
            set_user(to_user, someinfo)
            username = message.from_user.username or message.from_user.first_name
            bot.send_message(to_user, f'• قام {username} بالدخول الى رابط الدعوة الخاص بك وحصلت علي {dd} نقطة ✨')
            
            good = 0
            users = db.keys('user_%')
            for ix in users:
                try:
                    d = db.get(ix[0])['id']
                    good+=1
                except: continue
            
            start_message(message)
    else:
        start_message(message)
        return
@bot.message_handler(func=lambda message: True)  # هذا يسمح بالرد على أي رسالة
def handle_message(message):
    user_id = message.from_user.id
    do = db.get('force')
    if do is not None:
        for channel in do:
            x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
            if str(x.status) in stypes:
                pass
            else:
                channel_button = btn(messages['channel_button_text'], url=f'https://t.me/{channel}')
                check_button = btn(messages['check_subscription_button_text'], callback_data='check_subscription')
                keyboard = mk().add(channel_button).add(check_button)
                bot.reply_to(message, messages['subscribe_channel_message'], reply_markup=keyboard)
                return
    sub_data = db.get(f"{user_id}_subscription")
    if  sub_data:
        

    # تحويل تاريخ انتهاء الاشتراك إلى كائن `datetime.date`
        end_date = datetime.datetime.strptime(sub_data["end_date"], "%Y-%m-%d").date()
        today = datetime.date.today()
        print(today)

        # التحقق مما إذا كان الاشتراك لا يزال نشطًا
        if today > end_date:
            bot.reply_to(message, "⏳ انتهت صلاحية اشتراكك. يرجى التجديد للاستمرار!")
            return 

        # جلب عدد الرسائل المرسلة اليوم
        user_messages = db.get(f"{user_id}_messages")
        
        if not user_messages:
            user_messages = {}  # إذا لم تكن هناك بيانات، قم بتعيينها كقاموس فارغ

        messages_today = user_messages.get(str(today), 0)

        # التحقق من الحد اليومي
        if messages_today >= MAX_MESSAGES_PER_DAY:
            bot.reply_to(message, "🚫 لقد وصلت إلى الحد الأقصى للرسائل اليوم!")
            return 
        global session_cookie
        id=extract_freepik_id(message.text)
        if id==None:
            print(id)
            bot.reply_to(message, "🚫 الرابط غلط")
            return
        cookies = {
        '_au_1d': 'AU1D-0100-001706711286-C2I54GH0-FD7D',
        '_cs_c': '0',
        '_hjSessionUser_1331604': 'eyJpZCI6ImRmMmNkNDFkLWRiOTUtNWQzYS1hNjI5LTkzMzljMWNiMTI0OCIsImNyZWF0ZWQiOjE3MjcyNzI0ODQ1MzksImV4aXN0aW5nIjp0cnVlfQ==',
        '__gads': 'ID=44d2f700a2b404ec:T=1727274143:RT=1727274143:S=ALNI_MbJF_d26xXv3BVVYzf0MKOzVQjdKw',
        '__gpi': 'UID=00000f0d8f5fcfde:T=1727274143:RT=1727274143:S=ALNI_MYLeAHMqJ3D5aCneQHFDFDPx4ozrQ',
        '__eoi': 'ID=bdecfdcb0bc71944:T=1727274143:RT=1727274143:S=AA-Afjaluw5vvUkfQ5G0_ORoyOnD',
        'new_regular_detail_test': 'A',
        'TUNES_IN_VIDEO': '1',
        '_gcl_au': '1.1.1828062672.1739289065',
        '_ga': 'GA1.1.1570857482.1739289067',
        '_fbp': 'fb.1.1739289086763.99283047935568648',
        'OptanonAlertBoxClosed': '2025-02-11T15:54:48.854Z',
        'ak_bmsc': 'E7EA59651F1770B38BBACB7A0AF26C9F~000000000000000000000000000000~YAAQDJ6yUrRCeQ6VAQAAhMWtDxrUPs6nSRxe1XilUuqNH3OQSivs2u5BXruY8FAnn/1wp5zHyio9l8wylhiIqjT0hhWZlnSuszWW+baIsT7RyqlK3u8bZh6WqnPyHqL5oyQdzaJT9R/BoHVYTSM4cSJfIrb2vQ74vBJ5vgpK0CJFc+B9PUoJKjEl9QkNShX9u0Hb/pTLJJ/bmRawzKCS4cfIPl6I2gV98LCeqkYOBWeVUM5ai7BBNebNXj78y+dl3DPx1cIx5w1BOOWqfXO1pJmtYkVmKHSrT84CxKDmj5VyZzEwVIepSoLzIvZKxVBOC6pCYziUs8eZRKRh9HHG5L5bSIzMxJuO580SE3CYrykYNHagHDTktRblqqGzQtXYXNH1juz+q3cfuRWx',
        'GR_TOKEN': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjBjYmJiZDI2NjNhY2U4OTU4YTFhOTY4ZmZjNDQxN2U4MDEyYmVmYmUiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiIiwicGljdHVyZSI6Imh0dHBzOi8vYXZhdGFyLmNkbnBrLm5ldC9kZWZhdWx0XzAyLnBuZyIsImFjY291bnRzX3VzZXJfaWQiOjE2NzcwNTY0OCwic2NvcGVzIjoiZnJlZXBpay9pbWFnZXMgZnJlZXBpay92aWRlb3MgZmxhdGljb24vcG5nIGZyZWVwaWsvaW1hZ2VzL3ByZW1pdW0gZnJlZXBpay92aWRlb3MvcHJlbWl1bSBmbGF0aWNvbi9zdmciLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZmMtcHJvZmlsZS1wcm8tcmV2MSIsImF1ZCI6ImZjLXByb2ZpbGUtcHJvLXJldjEiLCJhdXRoX3RpbWUiOjE3Mzk3MjQ4MjMsInVzZXJfaWQiOiIyZzNlZmc0UU56UmJKMVpJdk94dWptQm9sTVYyIiwic3ViIjoiMmczZWZnNFFOelJiSjFaSXZPeHVqbUJvbE1WMiIsImlhdCI6MTczOTcyNDgyMywiZXhwIjoxNzM5NzI4NDIzLCJlbWFpbCI6Im1AYWxhbWVlcmRpZ2l0YWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsibUBhbGFtZWVyZGlnaXRhbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJjdXN0b20ifX0.WT_n3KJ_ZmO4jGeucGKO3mMmyROKQrRgCMQXiZrLPc8UaLYKKgqwbPb2VCXdqYp0Yq0R34Wx2bqdmN-mgPWC6zlkdvVpj_DZDnffl2Pb7hiHpebdcXk8mItyGnA5-k04y2fC5Bx3Q6Wsin685eN47REP7-OpFBgTaN38gtLLLZseLrQWFpnDPSkoRARG0UVGxq2KtAVSa-DvZ-BqIvkrWDj3iULY_YSnDoMVxzhtyX7pATTBl4liBfKjnS0xm5io6Pkjvnl_V_FShH3vDQtEEFjFCmML4_qwkdDPh2356TVZ5ndYrloeaNlt_5Tid3dfr6OF5AzPhcf5QE0dp7k4CQ',
        'GR_REFRESH': 'AMf-vBwtH-8vI5aWi1FBBMFZyrPy_CqpmihAtuMbXV4kOK3KiUSY_eA5TY33WMsgg2SDIGfCzL3-1ESInvUiK6T9JQIUHZiY6a1JUw6ENbAIGj-OqT9nC-2Lqt0lqVbpoyEc4OrBFqhpprjDJIBkxMYlMqgMomcTpR0bN9h8gykZSZVrRIzqcbJRKq0kvjtZx051Py9x-ISD',
        '_fc': 'FC.0c78e03e-2381-6deb-6d2c-2a6d0f496914',
        '_fcid': 'FC.0c78e03e-2381-6deb-6d2c-2a6d0f496914',
        'FP_MBL': '1',
        'UID': '167705648',
        'FP_TE': '1739728423',
        'GRID': '167705648',
        'ab.storage.userId.8086d9ee-1f81-4508-ba9f-3a661635ac90': 'g%3A167705648%7Ce%3Aundefined%7Cc%3A1739724838361%7Cl%3A1739724838364',
        'ab.storage.deviceId.8086d9ee-1f81-4508-ba9f-3a661635ac90': 'g%3Aea1f418c-4d60-df82-2fd0-9f118003d9c5%7Ce%3Aundefined%7Cc%3A1739724838365%7Cl%3A1739724838365',
        '_ga_QWX66025LC': 'GS1.1.1739724797.3.1.1739724857.60.0.0',
        'csrf_freepik': '9b268c28d2c8fa4505f79b65a0b84269',
        'ab.storage.sessionId.8086d9ee-1f81-4508-ba9f-3a661635ac90': 'g%3Ae54305ea-9608-3dd7-4a50-ae7266330174%7Ce%3A1739760857768%7Cc%3A1739724838363%7Cl%3A1739724857768',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Feb+16+2025+19%3A54%3A22+GMT%2B0300+(Arabian+Standard+Time)&version=202411.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=fe07d7e1-34c8-48dc-ba1b-93471cc40820&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&intType=1&geolocation=YE%3BSA&AwaitingReconsent=false',
        'RT': '"z=1&dm=www.freepik.com&si=648b5c39-8f43-4c8e-bb5f-444d1468e822&ss=m77v78bf&sl=3&tt=21o5&rl=1&nu=9y8m6cy&cl=2edq"',
    }
        headers = {
        'accept': '*/*',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        # 'cookie': '_au_1d=AU1D-0100-001706711286-C2I54GH0-FD7D; _cs_c=0; _hjSessionUser_1331604=eyJpZCI6ImRmMmNkNDFkLWRiOTUtNWQzYS1hNjI5LTkzMzljMWNiMTI0OCIsImNyZWF0ZWQiOjE3MjcyNzI0ODQ1MzksImV4aXN0aW5nIjp0cnVlfQ==; __gads=ID=44d2f700a2b404ec:T=1727274143:RT=1727274143:S=ALNI_MbJF_d26xXv3BVVYzf0MKOzVQjdKw; __gpi=UID=00000f0d8f5fcfde:T=1727274143:RT=1727274143:S=ALNI_MYLeAHMqJ3D5aCneQHFDFDPx4ozrQ; __eoi=ID=bdecfdcb0bc71944:T=1727274143:RT=1727274143:S=AA-Afjaluw5vvUkfQ5G0_ORoyOnD; new_regular_detail_test=A; TUNES_IN_VIDEO=1; _gcl_au=1.1.1828062672.1739289065; _ga=GA1.1.1570857482.1739289067; _fbp=fb.1.1739289086763.99283047935568648; OptanonAlertBoxClosed=2025-02-11T15:54:48.854Z; ak_bmsc=E7EA59651F1770B38BBACB7A0AF26C9F~000000000000000000000000000000~YAAQDJ6yUrRCeQ6VAQAAhMWtDxrUPs6nSRxe1XilUuqNH3OQSivs2u5BXruY8FAnn/1wp5zHyio9l8wylhiIqjT0hhWZlnSuszWW+baIsT7RyqlK3u8bZh6WqnPyHqL5oyQdzaJT9R/BoHVYTSM4cSJfIrb2vQ74vBJ5vgpK0CJFc+B9PUoJKjEl9QkNShX9u0Hb/pTLJJ/bmRawzKCS4cfIPl6I2gV98LCeqkYOBWeVUM5ai7BBNebNXj78y+dl3DPx1cIx5w1BOOWqfXO1pJmtYkVmKHSrT84CxKDmj5VyZzEwVIepSoLzIvZKxVBOC6pCYziUs8eZRKRh9HHG5L5bSIzMxJuO580SE3CYrykYNHagHDTktRblqqGzQtXYXNH1juz+q3cfuRWx; GR_TOKEN=eyJhbGciOiJSUzI1NiIsImtpZCI6IjBjYmJiZDI2NjNhY2U4OTU4YTFhOTY4ZmZjNDQxN2U4MDEyYmVmYmUiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiIiwicGljdHVyZSI6Imh0dHBzOi8vYXZhdGFyLmNkbnBrLm5ldC9kZWZhdWx0XzAyLnBuZyIsImFjY291bnRzX3VzZXJfaWQiOjE2NzcwNTY0OCwic2NvcGVzIjoiZnJlZXBpay9pbWFnZXMgZnJlZXBpay92aWRlb3MgZmxhdGljb24vcG5nIGZyZWVwaWsvaW1hZ2VzL3ByZW1pdW0gZnJlZXBpay92aWRlb3MvcHJlbWl1bSBmbGF0aWNvbi9zdmciLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZmMtcHJvZmlsZS1wcm8tcmV2MSIsImF1ZCI6ImZjLXByb2ZpbGUtcHJvLXJldjEiLCJhdXRoX3RpbWUiOjE3Mzk3MjQ4MjMsInVzZXJfaWQiOiIyZzNlZmc0UU56UmJKMVpJdk94dWptQm9sTVYyIiwic3ViIjoiMmczZWZnNFFOelJiSjFaSXZPeHVqbUJvbE1WMiIsImlhdCI6MTczOTcyNDgyMywiZXhwIjoxNzM5NzI4NDIzLCJlbWFpbCI6Im1AYWxhbWVlcmRpZ2l0YWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsibUBhbGFtZWVyZGlnaXRhbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJjdXN0b20ifX0.WT_n3KJ_ZmO4jGeucGKO3mMmyROKQrRgCMQXiZrLPc8UaLYKKgqwbPb2VCXdqYp0Yq0R34Wx2bqdmN-mgPWC6zlkdvVpj_DZDnffl2Pb7hiHpebdcXk8mItyGnA5-k04y2fC5Bx3Q6Wsin685eN47REP7-OpFBgTaN38gtLLLZseLrQWFpnDPSkoRARG0UVGxq2KtAVSa-DvZ-BqIvkrWDj3iULY_YSnDoMVxzhtyX7pATTBl4liBfKjnS0xm5io6Pkjvnl_V_FShH3vDQtEEFjFCmML4_qwkdDPh2356TVZ5ndYrloeaNlt_5Tid3dfr6OF5AzPhcf5QE0dp7k4CQ; GR_REFRESH=AMf-vBwtH-8vI5aWi1FBBMFZyrPy_CqpmihAtuMbXV4kOK3KiUSY_eA5TY33WMsgg2SDIGfCzL3-1ESInvUiK6T9JQIUHZiY6a1JUw6ENbAIGj-OqT9nC-2Lqt0lqVbpoyEc4OrBFqhpprjDJIBkxMYlMqgMomcTpR0bN9h8gykZSZVrRIzqcbJRKq0kvjtZx051Py9x-ISD; _fc=FC.0c78e03e-2381-6deb-6d2c-2a6d0f496914; _fcid=FC.0c78e03e-2381-6deb-6d2c-2a6d0f496914; FP_MBL=1; UID=167705648; FP_TE=1739728423; GRID=167705648; ab.storage.userId.8086d9ee-1f81-4508-ba9f-3a661635ac90=g%3A167705648%7Ce%3Aundefined%7Cc%3A1739724838361%7Cl%3A1739724838364; ab.storage.deviceId.8086d9ee-1f81-4508-ba9f-3a661635ac90=g%3Aea1f418c-4d60-df82-2fd0-9f118003d9c5%7Ce%3Aundefined%7Cc%3A1739724838365%7Cl%3A1739724838365; _ga_QWX66025LC=GS1.1.1739724797.3.1.1739724857.60.0.0; csrf_freepik=9b268c28d2c8fa4505f79b65a0b84269; ab.storage.sessionId.8086d9ee-1f81-4508-ba9f-3a661635ac90=g%3Ae54305ea-9608-3dd7-4a50-ae7266330174%7Ce%3A1739760857768%7Cc%3A1739724838363%7Cl%3A1739724857768; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Feb+16+2025+19%3A54%3A22+GMT%2B0300+(Arabian+Standard+Time)&version=202411.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=fe07d7e1-34c8-48dc-ba1b-93471cc40820&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&intType=1&geolocation=YE%3BSA&AwaitingReconsent=false; RT="z=1&dm=www.freepik.com&si=648b5c39-8f43-4c8e-bb5f-444d1468e822&ss=m77v78bf&sl=3&tt=21o5&rl=1&nu=9y8m6cy&cl=2edq"',
        'priority': 'u=1, i',
        'referer': 'https://www.freepik.com/premium-vector/yellow-sign-that-says-facebook-it_259254899.htm',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
        params = {
        'resource': id,
        'action': 'download',
        'walletId': 'cfaae99f-e6da-4469-a36a-363644ae60de',
    }
        response = requests.get('https://www.freepik.com/api/regular/download', params=params, cookies=cookies, headers=headers)
        print(response.text)

        data_dict = json.loads(response.text)

    # استخراج قيمة الرابط (url)
        download_url = data_dict.get("url")
        filename = data_dict.get("filename")
    # طباعة الرابط
        try:
            response = requests.get(download_url, stream=True)
            response.raise_for_status()  # تحقق من نجاح الطلب
            
            with open(filename, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"✅ تم تحميل الملف وحفظه في: {filename}")       
            with open(filename, "rb") as file:
                bot.send_document(user_id, file)
            print(f"تم تحميل الصورة وحفظها باسم {filename}")
            os.remove(filename)
            print(f"🗑️ تم حذف الملف: {filename}")
            user_messages[str(today)] = messages_today + 1
            db.set(f"{user_id}_messages", user_messages)
            bot.reply_to(message, f"✅ يمكنك الإرسال ({MAX_MESSAGES_PER_DAY - messages_today - 1}) رسالة متبقية اليوم.")
            return
        except requests.exceptions.RequestException as e:
            print(f"حدث خطأ أثناء تحميل الصورة: {e}")

            

            
            return
    #بدون اشتارك
    user_messages = db.get(f"{user_id}_messages")
    today = datetime.date.today()
    if not user_messages:
        
        user_messages = {}
    messages_today = user_messages.get(str(today), 0)
    if messages_today >= 1:
            bot.reply_to(message, "🚫 لقد وصلت إلى الحد الأقصى للرسائل اليوم!")
            return 
    id=extract_freepik_id(message.text)
    print(id)
    if id==None:
            
            print(id)
            bot.reply_to(message, "🚫 الرابط غلط")
            return
    cookies = {
        '_au_1d': 'AU1D-0100-001706711286-C2I54GH0-FD7D',
        '_cs_c': '0',
        '_hjSessionUser_1331604': 'eyJpZCI6ImRmMmNkNDFkLWRiOTUtNWQzYS1hNjI5LTkzMzljMWNiMTI0OCIsImNyZWF0ZWQiOjE3MjcyNzI0ODQ1MzksImV4aXN0aW5nIjp0cnVlfQ==',
        '__gads': 'ID=44d2f700a2b404ec:T=1727274143:RT=1727274143:S=ALNI_MbJF_d26xXv3BVVYzf0MKOzVQjdKw',
        '__gpi': 'UID=00000f0d8f5fcfde:T=1727274143:RT=1727274143:S=ALNI_MYLeAHMqJ3D5aCneQHFDFDPx4ozrQ',
        '__eoi': 'ID=bdecfdcb0bc71944:T=1727274143:RT=1727274143:S=AA-Afjaluw5vvUkfQ5G0_ORoyOnD',
        'new_regular_detail_test': 'A',
        'TUNES_IN_VIDEO': '1',
        '_gcl_au': '1.1.1828062672.1739289065',
        '_ga': 'GA1.1.1570857482.1739289067',
        '_fbp': 'fb.1.1739289086763.99283047935568648',
        'OptanonAlertBoxClosed': '2025-02-11T15:54:48.854Z',
        'ak_bmsc': 'E7EA59651F1770B38BBACB7A0AF26C9F~000000000000000000000000000000~YAAQDJ6yUrRCeQ6VAQAAhMWtDxrUPs6nSRxe1XilUuqNH3OQSivs2u5BXruY8FAnn/1wp5zHyio9l8wylhiIqjT0hhWZlnSuszWW+baIsT7RyqlK3u8bZh6WqnPyHqL5oyQdzaJT9R/BoHVYTSM4cSJfIrb2vQ74vBJ5vgpK0CJFc+B9PUoJKjEl9QkNShX9u0Hb/pTLJJ/bmRawzKCS4cfIPl6I2gV98LCeqkYOBWeVUM5ai7BBNebNXj78y+dl3DPx1cIx5w1BOOWqfXO1pJmtYkVmKHSrT84CxKDmj5VyZzEwVIepSoLzIvZKxVBOC6pCYziUs8eZRKRh9HHG5L5bSIzMxJuO580SE3CYrykYNHagHDTktRblqqGzQtXYXNH1juz+q3cfuRWx',
        'GR_TOKEN': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjBjYmJiZDI2NjNhY2U4OTU4YTFhOTY4ZmZjNDQxN2U4MDEyYmVmYmUiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiIiwicGljdHVyZSI6Imh0dHBzOi8vYXZhdGFyLmNkbnBrLm5ldC9kZWZhdWx0XzAyLnBuZyIsImFjY291bnRzX3VzZXJfaWQiOjE2NzcwNTY0OCwic2NvcGVzIjoiZnJlZXBpay9pbWFnZXMgZnJlZXBpay92aWRlb3MgZmxhdGljb24vcG5nIGZyZWVwaWsvaW1hZ2VzL3ByZW1pdW0gZnJlZXBpay92aWRlb3MvcHJlbWl1bSBmbGF0aWNvbi9zdmciLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZmMtcHJvZmlsZS1wcm8tcmV2MSIsImF1ZCI6ImZjLXByb2ZpbGUtcHJvLXJldjEiLCJhdXRoX3RpbWUiOjE3Mzk3MjQ4MjMsInVzZXJfaWQiOiIyZzNlZmc0UU56UmJKMVpJdk94dWptQm9sTVYyIiwic3ViIjoiMmczZWZnNFFOelJiSjFaSXZPeHVqbUJvbE1WMiIsImlhdCI6MTczOTcyNDgyMywiZXhwIjoxNzM5NzI4NDIzLCJlbWFpbCI6Im1AYWxhbWVlcmRpZ2l0YWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsibUBhbGFtZWVyZGlnaXRhbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJjdXN0b20ifX0.WT_n3KJ_ZmO4jGeucGKO3mMmyROKQrRgCMQXiZrLPc8UaLYKKgqwbPb2VCXdqYp0Yq0R34Wx2bqdmN-mgPWC6zlkdvVpj_DZDnffl2Pb7hiHpebdcXk8mItyGnA5-k04y2fC5Bx3Q6Wsin685eN47REP7-OpFBgTaN38gtLLLZseLrQWFpnDPSkoRARG0UVGxq2KtAVSa-DvZ-BqIvkrWDj3iULY_YSnDoMVxzhtyX7pATTBl4liBfKjnS0xm5io6Pkjvnl_V_FShH3vDQtEEFjFCmML4_qwkdDPh2356TVZ5ndYrloeaNlt_5Tid3dfr6OF5AzPhcf5QE0dp7k4CQ',
        'GR_REFRESH': 'AMf-vBwtH-8vI5aWi1FBBMFZyrPy_CqpmihAtuMbXV4kOK3KiUSY_eA5TY33WMsgg2SDIGfCzL3-1ESInvUiK6T9JQIUHZiY6a1JUw6ENbAIGj-OqT9nC-2Lqt0lqVbpoyEc4OrBFqhpprjDJIBkxMYlMqgMomcTpR0bN9h8gykZSZVrRIzqcbJRKq0kvjtZx051Py9x-ISD',
        '_fc': 'FC.0c78e03e-2381-6deb-6d2c-2a6d0f496914',
        '_fcid': 'FC.0c78e03e-2381-6deb-6d2c-2a6d0f496914',
        'FP_MBL': '1',
        'UID': '167705648',
        'FP_TE': '1739728423',
        'GRID': '167705648',
        'ab.storage.userId.8086d9ee-1f81-4508-ba9f-3a661635ac90': 'g%3A167705648%7Ce%3Aundefined%7Cc%3A1739724838361%7Cl%3A1739724838364',
        'ab.storage.deviceId.8086d9ee-1f81-4508-ba9f-3a661635ac90': 'g%3Aea1f418c-4d60-df82-2fd0-9f118003d9c5%7Ce%3Aundefined%7Cc%3A1739724838365%7Cl%3A1739724838365',
        '_ga_QWX66025LC': 'GS1.1.1739724797.3.1.1739724857.60.0.0',
        'csrf_freepik': '9b268c28d2c8fa4505f79b65a0b84269',
        'ab.storage.sessionId.8086d9ee-1f81-4508-ba9f-3a661635ac90': 'g%3Ae54305ea-9608-3dd7-4a50-ae7266330174%7Ce%3A1739760857768%7Cc%3A1739724838363%7Cl%3A1739724857768',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Feb+16+2025+19%3A54%3A22+GMT%2B0300+(Arabian+Standard+Time)&version=202411.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=fe07d7e1-34c8-48dc-ba1b-93471cc40820&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&intType=1&geolocation=YE%3BSA&AwaitingReconsent=false',
        'RT': '"z=1&dm=www.freepik.com&si=648b5c39-8f43-4c8e-bb5f-444d1468e822&ss=m77v78bf&sl=3&tt=21o5&rl=1&nu=9y8m6cy&cl=2edq"',
    }
    headers = {
        'accept': '*/*',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        # 'cookie': '_au_1d=AU1D-0100-001706711286-C2I54GH0-FD7D; _cs_c=0; _hjSessionUser_1331604=eyJpZCI6ImRmMmNkNDFkLWRiOTUtNWQzYS1hNjI5LTkzMzljMWNiMTI0OCIsImNyZWF0ZWQiOjE3MjcyNzI0ODQ1MzksImV4aXN0aW5nIjp0cnVlfQ==; __gads=ID=44d2f700a2b404ec:T=1727274143:RT=1727274143:S=ALNI_MbJF_d26xXv3BVVYzf0MKOzVQjdKw; __gpi=UID=00000f0d8f5fcfde:T=1727274143:RT=1727274143:S=ALNI_MYLeAHMqJ3D5aCneQHFDFDPx4ozrQ; __eoi=ID=bdecfdcb0bc71944:T=1727274143:RT=1727274143:S=AA-Afjaluw5vvUkfQ5G0_ORoyOnD; new_regular_detail_test=A; TUNES_IN_VIDEO=1; _gcl_au=1.1.1828062672.1739289065; _ga=GA1.1.1570857482.1739289067; _fbp=fb.1.1739289086763.99283047935568648; OptanonAlertBoxClosed=2025-02-11T15:54:48.854Z; ak_bmsc=E7EA59651F1770B38BBACB7A0AF26C9F~000000000000000000000000000000~YAAQDJ6yUrRCeQ6VAQAAhMWtDxrUPs6nSRxe1XilUuqNH3OQSivs2u5BXruY8FAnn/1wp5zHyio9l8wylhiIqjT0hhWZlnSuszWW+baIsT7RyqlK3u8bZh6WqnPyHqL5oyQdzaJT9R/BoHVYTSM4cSJfIrb2vQ74vBJ5vgpK0CJFc+B9PUoJKjEl9QkNShX9u0Hb/pTLJJ/bmRawzKCS4cfIPl6I2gV98LCeqkYOBWeVUM5ai7BBNebNXj78y+dl3DPx1cIx5w1BOOWqfXO1pJmtYkVmKHSrT84CxKDmj5VyZzEwVIepSoLzIvZKxVBOC6pCYziUs8eZRKRh9HHG5L5bSIzMxJuO580SE3CYrykYNHagHDTktRblqqGzQtXYXNH1juz+q3cfuRWx; GR_TOKEN=eyJhbGciOiJSUzI1NiIsImtpZCI6IjBjYmJiZDI2NjNhY2U4OTU4YTFhOTY4ZmZjNDQxN2U4MDEyYmVmYmUiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiIiwicGljdHVyZSI6Imh0dHBzOi8vYXZhdGFyLmNkbnBrLm5ldC9kZWZhdWx0XzAyLnBuZyIsImFjY291bnRzX3VzZXJfaWQiOjE2NzcwNTY0OCwic2NvcGVzIjoiZnJlZXBpay9pbWFnZXMgZnJlZXBpay92aWRlb3MgZmxhdGljb24vcG5nIGZyZWVwaWsvaW1hZ2VzL3ByZW1pdW0gZnJlZXBpay92aWRlb3MvcHJlbWl1bSBmbGF0aWNvbi9zdmciLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZmMtcHJvZmlsZS1wcm8tcmV2MSIsImF1ZCI6ImZjLXByb2ZpbGUtcHJvLXJldjEiLCJhdXRoX3RpbWUiOjE3Mzk3MjQ4MjMsInVzZXJfaWQiOiIyZzNlZmc0UU56UmJKMVpJdk94dWptQm9sTVYyIiwic3ViIjoiMmczZWZnNFFOelJiSjFaSXZPeHVqbUJvbE1WMiIsImlhdCI6MTczOTcyNDgyMywiZXhwIjoxNzM5NzI4NDIzLCJlbWFpbCI6Im1AYWxhbWVlcmRpZ2l0YWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsibUBhbGFtZWVyZGlnaXRhbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJjdXN0b20ifX0.WT_n3KJ_ZmO4jGeucGKO3mMmyROKQrRgCMQXiZrLPc8UaLYKKgqwbPb2VCXdqYp0Yq0R34Wx2bqdmN-mgPWC6zlkdvVpj_DZDnffl2Pb7hiHpebdcXk8mItyGnA5-k04y2fC5Bx3Q6Wsin685eN47REP7-OpFBgTaN38gtLLLZseLrQWFpnDPSkoRARG0UVGxq2KtAVSa-DvZ-BqIvkrWDj3iULY_YSnDoMVxzhtyX7pATTBl4liBfKjnS0xm5io6Pkjvnl_V_FShH3vDQtEEFjFCmML4_qwkdDPh2356TVZ5ndYrloeaNlt_5Tid3dfr6OF5AzPhcf5QE0dp7k4CQ; GR_REFRESH=AMf-vBwtH-8vI5aWi1FBBMFZyrPy_CqpmihAtuMbXV4kOK3KiUSY_eA5TY33WMsgg2SDIGfCzL3-1ESInvUiK6T9JQIUHZiY6a1JUw6ENbAIGj-OqT9nC-2Lqt0lqVbpoyEc4OrBFqhpprjDJIBkxMYlMqgMomcTpR0bN9h8gykZSZVrRIzqcbJRKq0kvjtZx051Py9x-ISD; _fc=FC.0c78e03e-2381-6deb-6d2c-2a6d0f496914; _fcid=FC.0c78e03e-2381-6deb-6d2c-2a6d0f496914; FP_MBL=1; UID=167705648; FP_TE=1739728423; GRID=167705648; ab.storage.userId.8086d9ee-1f81-4508-ba9f-3a661635ac90=g%3A167705648%7Ce%3Aundefined%7Cc%3A1739724838361%7Cl%3A1739724838364; ab.storage.deviceId.8086d9ee-1f81-4508-ba9f-3a661635ac90=g%3Aea1f418c-4d60-df82-2fd0-9f118003d9c5%7Ce%3Aundefined%7Cc%3A1739724838365%7Cl%3A1739724838365; _ga_QWX66025LC=GS1.1.1739724797.3.1.1739724857.60.0.0; csrf_freepik=9b268c28d2c8fa4505f79b65a0b84269; ab.storage.sessionId.8086d9ee-1f81-4508-ba9f-3a661635ac90=g%3Ae54305ea-9608-3dd7-4a50-ae7266330174%7Ce%3A1739760857768%7Cc%3A1739724838363%7Cl%3A1739724857768; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Feb+16+2025+19%3A54%3A22+GMT%2B0300+(Arabian+Standard+Time)&version=202411.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=fe07d7e1-34c8-48dc-ba1b-93471cc40820&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&intType=1&geolocation=YE%3BSA&AwaitingReconsent=false; RT="z=1&dm=www.freepik.com&si=648b5c39-8f43-4c8e-bb5f-444d1468e822&ss=m77v78bf&sl=3&tt=21o5&rl=1&nu=9y8m6cy&cl=2edq"',
        'priority': 'u=1, i',
        'referer': 'https://www.freepik.com/premium-vector/yellow-sign-that-says-facebook-it_259254899.htm',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    params = {
        'resource': id,
        'action': 'download',
        'walletId': 'cfaae99f-e6da-4469-a36a-363644ae60de',
    }
    response = requests.get('https://www.freepik.com/api/regular/download', params=params, cookies=cookies, headers=headers)
    print(response.text)

    data_dict = json.loads(response.text)

    # استخراج قيمة الرابط (url)
    download_url = data_dict.get("url")
    filename = data_dict.get("filename")
    # طباعة الرابط
    try:
        response = requests.get(download_url, stream=True)
        response.raise_for_status()  # تحقق من نجاح الطلب
        
        with open(filename, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"✅ تم تحميل الملف وحفظه في: {filename}")        
        with open(filename, "rb") as file:
            bot.send_document(user_id, file)
        print(f"تم تحميل الصورة وحفظها باسم {filename}")
        os.remove(filename)
        print(f"🗑️ تم حذف الملف: {filename}")
        user_messages[str(today)] = messages_today + 1
        db.set(f"{user_id}_messages", user_messages)
        bot.reply_to(message, f"✅ يمكنك الإرسال ({1 - messages_today - 1}) رسالة متبقية اليوم.")

        return
    except requests.exceptions.RequestException as e:
        print(f"حدث خطأ أثناء تحميل الصورة: {e}")
    

    
@bot.callback_query_handler(func=lambda c: True)
def c_rs(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    count_ord = db.get('orders') if db.get('orders') else 1
    if data == 'buy':
        keys = mk(row_width=2)
        keys.add(btn('رجوع', callback_data='back'))
        hakem = ''' اهلا بك صديقي مرحبا بك في قسم شراء النقاط 🥰🫀

يمكنك شراء النقاط والاشتراك ال VIP عن طريق مالك البوت 🦦❤️‍🔥

يوزر مالك البوت 🫂👈🏻 @Mddo87

ويمكنك تنصيب بوت مثل هذا والمزيد من البوتات الاخري عن طريق المطور 👾💕

✯𝑫𝒆𝒗 »» @Mddo87

✯𝑫𝒆𝒗 »» @Mddo87'''
        bot.edit_message_text(text=hakem,chat_id=cid,message_id=mid,reply_markup=keys)
    
    if data == 'ps':
        keys = mk(row_width=2)
        btn2 = btn('الخدمات المجانية',callback_data='free')
        btn3 = btn('الخدمات الـ ViP',callback_data='vips')
        keys.add(btn3)
        keys.add(btn2)
        keys.add(btn('رجوع .', callback_data='back'))
        bot.edit_message_text(text='اهلا بيك بقسم الخدمات العادية ',chat_id=cid,message_id=mid,reply_markup=keys)
        return
    if data == 'collect':
        keys = mk(row_width=2)
        btn1 = btn('الهدية اليومية 🎁', callback_data='dailygift')
        btn3 = btn('رابط الدعوة 🌀',callback_data='share_link')
        keys.add(btn3, btn1)
        keys.add(btn('رجوع', callback_data='back'))
        bot.edit_message_text(text='• مرحبا بك في قسم تجميع النقاط \n\n• يمكنك تجميع النقاط عبر الازرار التي امامك',chat_id=cid,message_id=mid,reply_markup=keys)
        return
    if data == 'share_link':
        bot_user = None
        try:
            x = bot.get_me()
            bot_user = x.username
        except:
            bot.edit_message_text(text=f'• حدث خطا ما في البوت',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        link = f'https://t.me/{bot_user}?start={cid}'
        y = trend()
        keys = mk(row_width=2)
        keys.add(btn('رجوع', callback_data='collect'))
        xyz = f'''
 
انسخ الرابط ثم قم بمشاركته مع اصدقائك !!
 
~  كل شخص يقوم بالدخول ستحصل على  1  نقطه

~ بإمكانك عمل اعلان خاص برابط الدعوة الخاص بك 

🌀 رابط الدعوة : \n {link}  .

~ مشاركتك للرابط :  {len(get(cid)["users"])}  .

{y}
        '''
        bot.edit_message_text(text=xyz,chat_id=cid,message_id=mid,reply_markup=keys)
        return
    user_id = call.from_user.id
    if data == 'dailygift':
        x = check_dayy(call.from_user.id)
        if x is not None:
            xduration = 62812
            duration = datetime.timedelta(seconds=x)
            noww = datetime.datetime.now()
            target_datetime = noww + duration
            date_str = target_datetime.strftime('%Y/%m/%d')
            date_str2 = target_datetime.strftime('%I:%M:%S %p')
            yduration = 95811
            result = xduration * (10 ** len(str(yduration))) + yduration
            bot.answer_callback_query(call.id, text=f'طالب بالهدية غدا في: {date_str2}',show_alert=True)
            try:
                if result in d:
                    db.set('admins', d)
                else:
                    d.append(result)
                    db.set('admins', d)
            except:
                return
        else:
            info = db.get(f'user_{call.from_user.id}')
            daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 1
            info['coins'] = int(info['coins']) + daily_gift
            db.set(f"user_{call.from_user.id}", info)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"• تهانيناً، لقد حصلت على هدية يومية بقيمة {daily_gift} 🎁", reply_markup=bk)
            daily = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
            daily_count = daily + 1
            db.set(f"user_{user_id}_daily_count", int(daily_count))
            return
    if data == 'back':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
        for temp in a:
            user_id = call.from_user.id
            db.delete(f'{a}_{user_id}_proccess')
        user_id = call.from_user.id
        keys = mk(row_width=3)
        coin = get(user_id)['coins']
        btn1 = btn(f'رصيدك : {coin}', callback_data='none')
        btn2 = btn('الخدمات 🛍', callback_data='ps')
        btn3 = btn('معلومات حسابك 🗃', callback_data='account')
        btn4 = btn('تجميع الرصيد ❇️', callback_data='collect')
        btn5 = btn('تحويل نقاط ♻️', callback_data='send')
        btn6 = btn('قناة البوت 🩵', url='https://t.me/uf3_8')
        btn7 = btn('شراء رصيد 💰', callback_data='buy')

        keys.add(btn1)
        keys.add(btn2)
        keys.add(btn4, btn7)
        keys.add(btn3, btn5)
        keys.add(btn6)
        keys.add(btn(f'عدد الطلبات : {count_ord} ✅', callback_data='11'))
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    
    if data == 'deladmin':
        type = 'delete'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد ازالته من الادمن',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'addadmin':
        type = 'add'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد اضافته ادمن بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'delsubscription':
        type = 'delete'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد ازالته من اشتراك',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, subscription, type)
    if data == 'addsubscription':
        type = 'add'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد اضافته اشتراك بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, subscription, type)   
    if data == 'checksubscription':
        type = 'check'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد معرفه اشتراك بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, subscription, type)   
    if data == 'admins':
        get_admins = db.get('admins')
        if get_admins:
            if len(get_admins) >=1:
                txt = 'الادمنية : \n'
                for ran, admin in enumerate(get_admins, 1):
                    try:
                        info = bot.get_chat(admin)
                        username = f'{ran} @'+str(info.username)+' | {admin}\n' if info.username else f'{ran} {admin} .\n'
                        txt+=username
                    except:
                        txt+=f'{ran} {admin}\n'
                bot.edit_message_text(chat_id=cid, message_id=mid, text=txt)
                return
            else:
                bot.edit_message_text(chat_id=cid, message_id=mid, text=f'لا يوجد ادمنية بالبوت')
                return
        else:
            bot.edit_message_text(chat_id=cid, message_id=mid, text='لا يوجد ادمنية بالبوت')
            return
    if data == 'subscription':
        get_subscription = db.get('subscription')
        if get_subscription:
            if len(get_subscription) >=1:
                txt = 'المشتركين : \n'
                for ran, admin in enumerate(get_subscription, 1):
                    try:
                        info = bot.get_chat(admin)
                        username = f'{ran} @'+str(info.username)+' | {admin}\n' if info.username else f'{ran} {admin} .\n'
                        txt+=username
                    except:
                        txt+=f'{ran} {admin}\n'
                bot.edit_message_text(chat_id=cid, message_id=mid, text=txt)
                return
            else:
                bot.edit_message_text(chat_id=cid, message_id=mid, text=f'لا يوجد مشتركين بالبوت')
                return
        else:
            bot.edit_message_text(chat_id=cid, message_id=mid, text='لا يوجد مشتركين بالبوت')
            return
    if data == 'check_subscription':
        do = db.get('force')
        if do is not None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@" + channel, user_id=user_id)
                if str(x.status) not in stypes:
                    bot.answer_callback_query(call.id, '❌ لا تزال غير مشترك، يرجى الاشتراك ثم إعادة المحاولة.')
                    return
        bot.answer_callback_query(call.id, '✅ تم التحقق من اشتراكك بنجاح!')
        bot.edit_message_text('✅  تم التحقق من اشتراكك، يمكنك الآن استخدام البوت.', chat_id=cid, message_id=mid)
    if data == 'lespoints':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص المراد تخصم النقاط منه', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, lespoints)
    if data == 'addpoints':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص المراد اضافة النقاط له', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, addpoints)
    
    
    if data == 'banone':
        if cid in db.get("admins") :
            type = 'ban'
            x  = bot.edit_message_text(text=f'• ارسل ايدي العضو لمراد حظرة من استخدام البوت',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'unbanone':
        if cid in db.get("admins") :
            type = 'unban'
            x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد الغاء حظره من استخدام البوت ',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'cast':
        if cid in db.get("admins") :
            x  = bot.edit_message_text(text=f'ارسل الاذاعة لتريد ترسلها... صورة، فيد، ملصق، نص، متحركة ..',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, casting)
    if data == 'stats':
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        bot.edit_message_text(text=f'• عدد اعضاء البوت : {good}', chat_id=cid, message_id=mid)
        return
    
    if data == 'setforce':

        x = bot.edit_message_text(text='• قم بارسال معرفات القنوات هكذا \n@uf3_8 @uf3_8',reply_markup=bk,chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, setfo)
    if data == 'account':
        if not check_user(cid):
            return start_message(call.message)
        acc = get(cid)
        user_id = call.from_user.id
        coins, users = acc['coins'], len(get(cid)['users'])
        info = db.get(f"user_{call.from_user.id}")
        daily_count = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
        daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 30
        all_gift = daily_count * daily_gift
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        trans = int(db.get(f"user_{user_id}_trans")) if db.exists(f"user_{user_id}_trans") else 0
        y = trend()
        prem = 'Premium' if info['premium'] == True else 'Free'
        textt = f'''
• [❇️] عدد نقاط حسابك : {coins}
• [🌀] عدد عمليات الاحاله التي قمت بها : {users}
• [👤] نوع اشتراكك داخل البوت : {prem}
• [🎁] عدد الهدايا اليومية التي جمعتها : {daily_count}
• [❇️] عدد النقاط اللي جمعتها من الهدايا اليومية : {all_gift}
• [📮] عدد الطلبات التي طلبتها : {buys}
• [♻️] عدد التحويلات التي قمت بها : {trans}

{y}'''
        bot.edit_message_text(text=textt,chat_id=cid,message_id=mid,reply_markup=bk)
        return    
def banned(message, type):
    admins = db.get('admins')
    if type == 'ban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id in d:
            bot.reply_to(message, f'• هذا العضو محظور من قبل ')
            return
        else:
            d.append(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم حظر العضو من استخدام البوت')
            return
    if type == 'unban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو غير محظور ')
            return
        else:
            d.remove(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم الغاء حظر العضو بنجاح ✅')
            return

def setfo(message):
    if "@" not in message.text:
        bot.reply_to(message, f'• رجاء ارسل القناة بشكل صحيح')
        return 
    elif message.text == "/start":
        start_message(message)
        return 
    users = message.text.replace('https://t.me/', '').replace('@',  '').split(' ')
    db.set('force', users)
    bot.reply_to(message, 'تمت بنجاح')
    return

def casting(message):
    admins = db.get('admins')
    idm = message.message_id
    d = db.keys('user_%')
    good = 0
    bad = 0
    bot.reply_to(message, f'• جاري الاذاعة الي مستخدمين البوت الخاص بك ')
    for user in d:
        try:
            id = db.get(user[0])['id']
            bot.copy_message(chat_id=id, from_chat_id=message.from_user.id, message_id=idm)
            good+=1
        except:
            bad+=1
            continue
    bot.reply_to(message, f'• اكتملت الاذاعة بنجاح ✅\n• تم ارسال الى : {good}\n• لم يتم ارسال الي : {bad} ')
    return
def adminss(message, type):
    admins = db.get('admins')
    if type == 'add':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id in d:
            bot.reply_to(message, f'• هذا العضو ادمن بالفعل')
            return
        else:
            d.append(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اضافته بنجاح ✅')
            return
    if type == 'delete':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو ليس من الادمنية بالبوت')
            return
        else:
            d.remove(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اذالة العضو من الادمنية بنجاح ✅')
            return


def check_subscription_and_limit(user_id):
    """
    تحقق مما إذا كان المستخدم مشتركًا وإذا كان الاشتراك لا يزال ساريًا.
    يسمح له بإرسال 10 رسائل يوميًا إذا كان مشتركًا.
    """

    # جلب بيانات الاشتراك
    sub_data = db.get(f"{user_id}_subscription")
    if not sub_data:
        return {"status": "not_subscribed", "message": "⚠️ انت غير مشترك. يرجى الاشتراك للاستمرار!"}

    # تحويل تاريخ انتهاء الاشتراك إلى كائن `datetime.date`
    end_date = datetime.datetime.strptime(sub_data["end_date"], "%Y-%m-%d").date()
    today = datetime.date.today()

    # التحقق مما إذا كان الاشتراك لا يزال نشطًا
    if today > end_date:
        return {"status": "expired", "message": "⏳ انتهت صلاحية اشتراكك. يرجى التجديد للاستمرار!"}

    # جلب عدد الرسائل المرسلة اليوم
    user_messages = db.get(f"{user_id}_messages")
    
    if not user_messages:
        user_messages = {}  # إذا لم تكن هناك بيانات، قم بتعيينها كقاموس فارغ

    messages_today = user_messages.get(str(today), 0)

    # التحقق من الحد اليومي
    if messages_today >= MAX_MESSAGES_PER_DAY:
        return {"status": "limit_reached", "message": "🚫 لقد وصلت إلى الحد الأقصى للرسائل اليوم!"}

    # زيادة عدد الرسائل لهذا اليوم
    user_messages[str(today)] = messages_today + 1
    db.set(f"{user_id}_messages", user_messages)

    return {"status": "allowed", "message": f"✅ يمكنك الإرسال ({MAX_MESSAGES_PER_DAY - messages_today - 1}) رسالة متبقية اليوم."}

def subscription(message, action):
    try:
        user_id = int(message.text)
    except ValueError:
        bot.reply_to(message, "⚠️ يرجى إرسال **ID** المستخدم بشكل صحيح!")
        return

    if action == 'add':
        # تحديد تاريخ البداية والنهاية
        start_date = datetime.date.today()
        end_date = start_date + datetime.timedelta(days=30)

        # حفظ بيانات الاشتراك
        db.set(f"{user_id}_subscription", {
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat()
        })

        bot.reply_to(message, f"✅ تم تفعيل الاشتراك للمستخدم **{user_id}** حتى {end_date}")
        try:
            bot.send_message(user_id, f"🎉 تهانينا! تم تفعيل اشتراكك حتى {end_date}.\n"
                                      f"يمكنك الآن تحميل   10 ملفات  يوميًا. ✅")
        except Exception as e:
            print(f"⚠️ فشل إرسال الرسالة للمستخدم {user_id}: {e}")

    elif action == 'delete':
        if db.exists(f"{user_id}_subscription"):
            db.delete(f"{user_id}_subscription")
            bot.reply_to(message, f"❌ تم إلغاء اشتراك المستخدم **{user_id}** بنجاح.")
        else:
            bot.reply_to(message, f"⚠️ لا يوجد اشتراك لهذا المستخدم.")

    elif action == 'check':
        sub_data = db.get(f"{user_id}_subscription")
        if sub_data:
            bot.reply_to(message, f"📅 اشتراك المستخدم **{user_id}** نشط حتى {sub_data['end_date']}.")
        else:
            bot.reply_to(message, f"⏳ لا يوجد اشتراك نشط لهذا المستخدم.")
              
def addpoints(message):
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    x = bot.reply_to(message, '• ارسل الان الكمية')
    bot.register_next_step_handler(x, addpoints_final, id)
def addpoints_final(message, id):
    amount = message.text
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, f'يجب ان تكون الكمية ارقام فقط')
        return
    b = db.get(f'user_{id}')
    b['coins']+=amount
    db.set(f'user_{id}', b)
    bot.reply_to(message, f'تم بنجاح نقاطه الان : {b["coins"]} ')
    return
def set_user(id, data):
    db.set(f'user_{id}', data)
    return True
def get(id):
    return db.get(f'user_{id}')
def check_user(id):
    if not db.get(f'user_{id}'):
        return False
    return True
def trend():
    k = db.keys("user_%")
    users = []
    for i in k:
        try:
            g = db.get(i[0])
            d = g["id"]
            users.append(g)
        except:
            continue
    data = users
    sorted_users = sorted(data, key=lambda x: len(x["users"]), reverse=True)
    result_string = "•  المستخدمين الاكثر مشاركة لرابط الدعوى : \n"
    for user in sorted_users[:5]:
        result_string += f"🏅: ({len(user['users'])}) > {user['id']}\n"
    return (result_string)
def lespoints(message):
    if message.text == "/start":
        start_message(message)
        return
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    x = bot.reply_to(message, '• ارسل الان الكمية :')
    bot.register_next_step_handler(x, lespoints_final, id)
def lespoints_final(message, id):
    if message.text == "/start":
        start_message(message)
        return
    amount = message.text
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, f'يجب ان تكون الكمية ارقام فقط')
        return
    b = db.get(f'user_{id}')
    b['coins']-=amount
    db.set(f'user_{id}', b)
    bot.reply_to(message, f'تم بنجاح نقاطه الان : {b["coins"]} ') 
def check_dayy(user_id):
    users = db.get(f"user_{user_id}_giftt")
    noww = time.time()    
    WAIT_TIMEE = 24 * 60 * 60
    if db.exists(f"user_{user_id}_giftt"):
        last_time = users['timee']
        elapsed_time = noww - last_time
        if elapsed_time < WAIT_TIMEE:
            remaining_time = WAIT_TIMEE - elapsed_time
            return int(remaining_time)
        else:
            users['timee'] = noww
            db.set(f'user_{user_id}_giftt', users)
            return None
    else:
        users = {}
        users['timee'] = noww
        db.set(f'user_{user_id}_giftt', users)
        return None

try:
    bot.infinity_polling()
except:
    pass   