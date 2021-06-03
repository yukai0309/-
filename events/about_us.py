from events.line_bot_api import *


def about_us_event(event):
    profile_name = line_bot_api.get_profile(event.source.user_id).display_name

    about_us_text1 = '歡迎來賓 {name} (๑•᎑•๑)\n我是長照小幫手，主要是宣傳'.format(name=profile_name)
    about_us_text2 = '位於慈濟科技大學的\n智社區服務據點的資訊'
    about_us_text3 = '希望透過我詳細的介紹\n讓您可以更加清楚呦(๑•᎑•๑)'
    about_us_img = 'https://i.imgur.com/iHlzwEF.jpg'
    line_bot_api.reply_message(
        event.reply_token,
        messages=[TextSendMessage(text=about_us_text1),
                  TextSendMessage(text=about_us_text2),
                  TextSendMessage(text=about_us_text3),
                  ImageSendMessage(original_content_url=about_us_img, preview_image_url=about_us_img),
                  StickerSendMessage(package_id=11539, sticker_id=52114110)])
