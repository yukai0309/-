from events.line_bot_api import *
from urllib.parse import parse_qsl
from developers.models import service
import datetime


# 圖選項
def appointment_event(event):
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/7OXIQcQ.png',
                    title='瑞智憶學苑',
                    text='周一至周五:08:30-16:30',
                    actions=[
                        PostbackAction(
                            label='詳細資訊',
                            text='詳細資訊',
                            data='action=step1-3-1&service=詳細資訊'
                        ),
                        PostbackAction(
                            label='預約參觀',
                            text='瑞智憶學苑',
                            data='action=step1-1&service=瑞智憶學苑'
                        ),
                        PostbackAction(
                            label='取消預約',
                            text='取消預約',
                            data='action=step1-2&service=取消預約'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/NE749E3.jpg',
                    title='好young心坊',
                    text='周一至周五:08:30-16:30',
                    actions=[
                        PostbackAction(
                            label='課程內容',
                            text='課程內容介紹',
                            data='action=step1-4&service=課程內容介紹'
                        ),
                        PostbackAction(
                            label='預約參觀',
                            text='好young心坊',
                            data='action=step1-1&service=好young心坊'
                        ),
                        PostbackAction(
                            label='取消預約',
                            text='取消預約',
                            data='action=step1-2&service=取消預約'
                        ),
                    ]
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[TextSendMessage(text='主要招生的有兩個學苑，想了解更多資訊，點選下方更進一步了解'),
                  carousel_template_message]
    )


# 選擇日期
def appointment_datetime_event(event):
    data = dict(parse_qsl(event.postback.data))

    now = datetime.datetime.now()
    min_date = now + datetime.timedelta(days=3)
    max_date = now + datetime.timedelta(days=9)

    image_carousel_template_message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/LoPvhkh.jpg',
                    action=DatetimePickerAction(
                        label="選擇日期",
                        data='action=step3&service={}'.format(data.get('service')),
                        mode="datetime",
                        initial=min_date.strftime('%Y-%m-%dT00:00'),
                        min=min_date.strftime('%Y-%m-%dT00:00'),
                        max=max_date.strftime('%Y-%m-%dT23:59')
                    )
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[image_carousel_template_message]
    )


# 已完成預約
# 服務, 時間, 使用者名稱, id
def appointment_completed_event(event):
    appointment_service = dict(parse_qsl(event.postback.data)).get('service')
    appointment_datetime = datetime.datetime.strptime(event.postback.params.get('datetime'), '%Y-%m-%dT%H:%M')
    profile_name = line_bot_api.get_profile(event.source.user_id).display_name
    user_id = event.source.user_id

    # 存入資料庫
    appointment = service.objects.create(user_id=user_id, service=appointment_service, datetime=appointment_datetime)
    appointment.save()

    appointment_service_text = '謝謝 {name}~ 您已經預約 {service}囉~'.format(name=profile_name, service=appointment_service)
    appointment_datetime_text = appointment_datetime.strftime('您預約的日期是 %Y-%m-%d\n時間為 %H:%M')
    appointment_text = '不要忘記囉!歡迎您的到來~'

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[TextSendMessage(text=appointment_service_text),
                  TextSendMessage(text=appointment_datetime_text),
                  TextSendMessage(text=appointment_text)]
    )


# 取消預約
def appointment_cancelappointment_event(event):
    user_id = event.source.user_id
    appointment = service.objects.filter(user_id=user_id).exists()
    appointment_datetime_text = appointment.appointment_datetime.strftime('您預約的日期是 %Y-%m-%d\n時間為 %H:%M')

    confirm_template_message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='您想要取消預約嗎?',
            actions=[
                MessageAction(
                    label='是的',
                    text='@cancel'
                ),
                MessageAction(
                    label='沒有',
                    text='@no'
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[TextSendMessage(text=appointment_datetime_text),
                  confirm_template_message]
    )


def appointment_cancel_event(event):
    # 先抓取使用者Line id
    user_id = event.source.user_id
    appointment = service.objects.filter(user_id=user_id).exists()
    # 刪除此使用者
    if appointment:
        appointment.delete()

        line_bot_api.reply_message(
            reply_token=event.reply_token,
            messages=[TextSendMessage(text='您的預約已經取消囉，歡迎再次預約')]
        )


# 瑞智憶學苑詳細資訊
def appointment_introduction131_event(event):
    appointment_introduction_text1 = '瑞智憶學苑'
    appointment_introduction_text2 = '內部空間安裝無障礙雙層扶手維護長者安全，提供社區失智長者服務及學生實作及實習的場域。'
    appointment_introduction_text3 = '除此此外!!我們還有憶起愛、柑仔店'

    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/FtfV0X2.png',
                    title='憶起愛、柑仔店',
                    text='服務、貢獻、成就感',
                    actions=[
                        PostbackAction(
                            label='了解更多',
                            text='了解更多',
                            data='action=step1-3-2&service=了解更多'
                        )
                    ]
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[TextSendMessage(text=appointment_introduction_text1),
                  TextSendMessage(text=appointment_introduction_text2),
                  TextSendMessage(text=appointment_introduction_text3),
                  carousel_template_message]
    )


# 瑞智憶學苑柑仔店
def appointment_orange_event(event):
    orange_img1 = 'https://i.imgur.com/27DXubO.png'
    orange_text1 = '每個月柑仔店會舉行二手物義賣'
    orange_text2 = '師生捧場，招呼介紹，樂做最佳店長'
    orange_text3 = '讓老人家體驗，清潔整理、包裝標價、增進計算能力'
    orange_text4 = '烘培課製作點心、販售義賣所得\n捐做慈濟教育志業基金，服務、貢獻、成就感'

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[TextSendMessage(text=orange_text1),
                  TextSendMessage(text=orange_text2),
                  TextSendMessage(text=orange_text3),
                  TextSendMessage(text=orange_text4),
                  ImageSendMessage(original_content_url=orange_img1, preview_image_url=orange_img1)]
    )


# 好young課程內容
def appointment_youngclassdetails_event(event):
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/WQPex1g.jpg',
                    title='咖啡烘培',
                    text='課程照片',
                    actions=[
                        PostbackAction(
                            label='觀看照片',
                            text='觀看照片',
                            data='action=step1-4-1&service=詳細資訊'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/69ShAyJ.jpg',
                    title='包裝設計',
                    text='課程照片',
                    actions=[
                        PostbackAction(
                            label='觀看照片',
                            text='觀看照片',
                            data='action=step1-4-2&service=詳細資訊'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/kJf1Zzp.jpg',
                    title='園藝療法',
                    text='課程照片',
                    actions=[
                        PostbackAction(
                            label='觀看照片',
                            text='觀看照片',
                            data='action=step1-4-3&service=觀看照片'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/3BigGyJ.jpg',
                    title='有氧增肌',
                    text='課程照片',
                    actions=[
                        PostbackAction(
                            label='觀看照片',
                            text='觀看照片',
                            data='action=step1-4-4&service=觀看照片'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/j7zOhuC.jpg',
                    title='運動舒包',
                    text='課程照片',
                    actions=[
                        PostbackAction(
                            label='觀看照片',
                            text='觀看照片',
                            data='action=step1-4-5&service=觀看照片'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/ll7R1C3.jpg',
                    title='腦力激盪',
                    text='課程照片',
                    actions=[
                        PostbackAction(
                            label='觀看照片',
                            text='觀看照片',
                            data='action=step1-4-6&service=觀看照片'
                        ),
                    ]
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[TextSendMessage(text='以下是好young心坊的六個課程照片'),
                  carousel_template_message]
    )


# 咖啡烘培
def appointment_coffee_event(event):
    coffee_img1 = 'https://i.imgur.com/FF2RSty.jpg'
    coffee_img2 = 'https://i.imgur.com/ud3bJFD.jpg'
    coffee_img3 = 'https://i.imgur.com/51MFBVj.jpg'
    coffee_img4 = 'https://i.imgur.com/WQPex1g.jpg'

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[ImageSendMessage(original_content_url=coffee_img1, preview_image_url=coffee_img1),
                  ImageSendMessage(original_content_url=coffee_img2, preview_image_url=coffee_img2),
                  ImageSendMessage(original_content_url=coffee_img3, preview_image_url=coffee_img3),
                  ImageSendMessage(original_content_url=coffee_img4, preview_image_url=coffee_img4),
                  ]
    )


# 包裝設計
def appointment_design_event(event):
    design_img1 = 'https://i.imgur.com/HNcrgFU.jpg'
    design_img2 = 'https://i.imgur.com/BKJlmCD.jpg'
    design_img3 = 'https://i.imgur.com/69ShAyJ.jpg'

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[ImageSendMessage(original_content_url=design_img1, preview_image_url=design_img1),
                  ImageSendMessage(original_content_url=design_img2, preview_image_url=design_img2),
                  ImageSendMessage(original_content_url=design_img3, preview_image_url=design_img3),
                  ]
    )


# 園藝療法
def appointment_gardening_event(event):
    gardening_img1 = 'https://i.imgur.com/kJf1Zzp.jpg'
    gardening_img2 = 'https://i.imgur.com/NnRKDMj.jpg'

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[ImageSendMessage(original_content_url=gardening_img1, preview_image_url=gardening_img1),
                  ImageSendMessage(original_content_url=gardening_img2, preview_image_url=gardening_img2),
                  ]
    )


# 有氧增肌
def appointment_aerobic_event(event):
    aerobic_img1 = 'https://i.imgur.com/NsnT5O5.jpg'
    aerobic_img2 = 'https://i.imgur.com/3BigGyJ.jpg'

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[ImageSendMessage(original_content_url=aerobic_img1, preview_image_url=aerobic_img1),
                  ImageSendMessage(original_content_url=aerobic_img2, preview_image_url=aerobic_img2),
                  ]
    )


# 運動舒包
def appointment_sports_event(event):
    sports_img1 = 'https://i.imgur.com/j7zOhuC.jpg'
    sports_img2 = 'https://i.imgur.com/0SHiig4.jpg'

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[ImageSendMessage(original_content_url=sports_img1, preview_image_url=sports_img1),
                  ImageSendMessage(original_content_url=sports_img2, preview_image_url=sports_img2),
                  ]
    )


# 腦力激盪
def appointment_brainpower_event(event):
    brainpower_img1 = 'https://i.imgur.com/ll7R1C3.jpg'

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[ImageSendMessage(original_content_url=brainpower_img1, preview_image_url=brainpower_img1),
                  ]
    )
