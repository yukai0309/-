from events.line_bot_api import *

# host = 'lineqna.azurewebsites.net'
# endpoint_key = 'e3170c7c-48ff-4340-bca4-5772e60ba3e3'
# kb = '94c69f04-ec64-4c6c-99a1-f7f94e82bde6'
# method = '/qnamaker/knowledgebases/' + kb + '/generateAnswer'


def location_event(event):
    location_text = '洽詢專線'
    location_text2 = '長期照護研究所 03-8572158\n分機 2259 方小姐'
    location_text3 = '地點'
    location_text4 = '花蓮市建國路二段880號 (慈濟科技大學)'

    line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(text=location_text),
         TextSendMessage(text=location_text2),
         TextSendMessage(text=location_text3),
         TextSendMessage(text=location_text4),
         LocationSendMessage(title='我的所在位置', address='花蓮縣慈濟科技大學', latitude=23.9967593, longitude=121.5625648)])

