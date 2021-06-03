from events.line_bot_api import *


def area_event(event):
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/0HQpf1p.jpg',
                    title='樂齡創客練工場',
                    text='周一至周五:08:30-16:30',
                    actions=[
                        PostbackAction(
                            label='詳細資訊',
                            text='詳細資訊',
                            data='action=step2-1&service=詳細資訊'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/e3vDx9i.png',
                    title='健康管理樂活實作中心',
                    text='周一至周五:08:30-16:30',
                    actions=[
                        PostbackAction(
                            label='詳細資訊',
                            text='詳細資訊',
                            data='action=step2-2&service=詳細資訊'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/CX6M5x3.png',
                    title='樂活俱樂部',
                    text='周一至周五:08:30-16:30',
                    actions=[
                        PostbackAction(
                            label='詳細資訊',
                            text='詳細資訊',
                            data='action=step2-3&service=詳細資訊'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/CP3X4na.jpg',
                    title='療癒花園',
                    text='周一至周五:08:30-16:30',
                    actions=[
                        PostbackAction(
                            label='詳細資訊',
                            text='詳細資訊',
                            data='action=step2-4&service=詳細資訊'
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[TextSendMessage(text='園區裡共分成四個場域\n可以點選下方選擇您想了解的內容'),
                  carousel_template_message]
    )


# 樂齡創客練工場
def area_maker_event(event):
    maker_img = 'https://i.imgur.com/Wjg6wlx.png'
    maker_text = '藉由創新研發、長照實作及專題實作課程'
    maker_text1 = '技優生與長者青銀共創，共同研發高齡創新輔具及多媒體大腦活化遊戲或教具'

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[TextSendMessage(text=maker_text),
                  TextSendMessage(text=maker_text1),
                  ImageSendMessage(original_content_url=maker_img, preview_image_url=maker_img)]
    )


# 健康管理樂活實作中心
def area_health_event(event):
    health_img = 'https://i.imgur.com/wT4TEij.jpg'
    health_text = '設置銀髮整合性評估及運動、健康等'
    health_text1 = '促進相關之軟硬體儀器設備，中間空地可作為多用途活動空間。'

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[TextSendMessage(text=health_text),
                  TextSendMessage(text=health_text1),
                  ImageSendMessage(original_content_url=health_img, preview_image_url=health_img)]
    )


# 樂活俱樂部
def area_club_event(event):
    club_img = 'https://i.imgur.com/VQwB3KX.jpg'
    club_text = '配置適合長者的油壓器材'
    club_text1 = '技優生藉由實作或實習課程規劃及引導樂齡大學'
    club_text2 = '瑞智日托站或社區長者進行阻力運動訓練或治療性活動。'

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[TextSendMessage(text=club_text),
                  TextSendMessage(text=club_text1),
                  TextSendMessage(text=club_text2),
                  ImageSendMessage(original_content_url=club_img, preview_image_url=club_img)]
    )


# 療癒花園
def area_garden_event(event):
    garden_img = 'https://i.imgur.com/CP3X4na.jpg'
    garden_text = '配合學程開設課程'
    garden_text2 = '提供學生進行園藝療法實作及實習場域'
    garden_text3 = '作為長者及樂齡大學學員進行社交活動及園藝治療'

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[TextSendMessage(text=garden_text),
                  TextSendMessage(text=garden_text2),
                  TextSendMessage(text=garden_text3),
                  ImageSendMessage(original_content_url=garden_img, preview_image_url=garden_img)]
    )
