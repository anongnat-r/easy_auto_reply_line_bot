
import json
from random import randint
from pythainlp import word_tokenize
from flask import Flask, request, abort
from argparse import ArgumentParser
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = '087de6c99fc50017802808a0a8c84e3e'
channel_access_token = '1Epm1mCMcOi/TD5zF6vt7Ti1b0GK1gUQ4T8RaJdPRr/f97Xhz8j9KniHkF+5havAk73P8scdo0vmohex+RdpVvUD8VGpUlF2n2lyGwYphMKgh2dcP4C8KCqH95PhKWAHH3SF2ltPk4+uVElCwCUNJwdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

@app.route('/webhook', methods=['POST'])
def callback():
    json_line = request.get_json(force=False,cache=False)
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    no_event = len(decoded['events'])
    for i in range(no_event):
        event = decoded['events'][i]
        event_handle(event)
    return '',200

def event_handle(event):
    print(event)
    try:
        userId = event['source']['userId']
    except:
        print('error cannot get userId')
        return ''

    try:
        rtoken = event['replyToken']
    except:
        print('error cannot get rtoken')
        return ''
    food_list = ['กระดูกอ่อนตุ๋นไชเท้ายาจีน',
             'เกาเหลาลูกชิ้นหมู',
             'แกงจืดไข่น้ำ',
             'แกงจืดเต้าหู้ไข่สาหร่าย',
             'แกงจืดแตงกวาสอดไส้',
             'แกงจืดมะระยัดไส้หมูสับ',
             'แกงจืดหมูม้วนสาหร่าย',
             'แกงจืดลูกรอก',
             'ต้มเลือดหมู',
             'ต้มจับฉ่าย',
             'ไก่ตุ๋นฟักมะนาวดอง/เห็ดหอม',
             'ซี่โครงหมูตุ๋นเยื่อไผ่',
             'มะระตุ๋นยาจีนกระดูกหมู',
             'แกงเลียงกุ้งสด',
             'แกงส้มชะอมทอดกุ้ง',
             'ต้มข่าไก่/ปลาสลิด',
             'ต้มโคล้งปลาดุกย่าง/ปลากรอบ',
             'ต้มแซบกระดูกหมูอ่อน',
             'ต้มส้มปลาทับทิม',
             'ต้มยำกุ้ง/รวมมิตร',
             'ต้มยำโป๊ะแตก',
             'แกงกระหรี่ไก่',
             'แกงคั่วสับปะรด',
             'แกงเขียวหวานปลากราย/ไก่',
             'แกงเทโพหมู',
             'แกงไตปลา',
             'แกงป่าขาหมู',
             'แกงเผ็ดเป็ดย่าง',
             'แกงเหลืองปลาขนมจีนน้ำยาปลาช่อน',
             'ฉู่ฉี่ปลา',
             'แกงไก่หน่อไม้ดอง',
             'แกงเผ็ดปลาหมึกสอดไส้',
             'แกงเผ็ดกระดูกหมู',
             'พะแนงหมู/ไก่/กุ้ง',
             'มัสมั่นหมู/ไก่',
             'น้ำตกหมู',
             'ปลาหมึกนึ่งมะนาว',
             'พล่ากุ้ง',
             'ยำก้านคะน้ากุ้งสด',
             'ยำคอหมูย่าง',
             'ไก่ย่าง',
             'ยำถั่วพลูกุ้ง',
             'ยำทะเลรวมมิตร',
             'ยำปลาดุกฟู',
             'ยำปลาทู',
             'ยำตะไคร้',
             'ยำมะเขือยาวเผา',
             'ยำวุ้นเส้นกุ้ง/ไก่/ปลาหมึก',
             'ยำหมูยอ',
             'ยำกุนเชียง',
             'ยำเห็ดหูหนูขาว',
             'ลาบหมู/ไก่/ปลาช่อน',
             'หมู/ไก่มะนาว']
    text = event['message']['text']
    proc = word_tokenize(text, engine='newmm')
    matching = [s for s in proc if ('กิน' in s) or (
        'อาหาร' in s) or ('อะไร' in s)]
    if len(matching) != 0:
        i = randint(0, len(food_list)-1)
        line_bot_api.reply_message(
            rtoken, TextSendMessage(text=food_list[i]))
    else:
        line_bot_api.reply_message(rtoken, TextSendMessage(
            text='ต้องการสุ่มอาหารหรือเปล่า หากต้องการสุ่ม พิมพ์ กินอะไรดี'))
    # line_bot_api.reply_message(rtoken, TextSendMessage(text='Hello World!'))

if __name__ == '__main__':
    app.run(debug=True)
