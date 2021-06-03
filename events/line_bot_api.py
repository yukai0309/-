from linebot import LineBotApi, WebhookParser, WebhookHandler
from linebot.models import PostbackEvent
from linebot.exceptions import InvalidSignatureError, LineBotApiError

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, CarouselTemplate, CarouselColumn,
    PostbackAction, MessageAction, URIAction, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, DatetimePickerAction, ConfirmTemplate
)

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

import http.client, json

line_bot_api = LineBotApi('8cDF9xyKifErJIMd1QzgLag14AXtPiu6+yux6zT6SRQ23ugAqklMpz+Kc+WgwVv/WinOPvYCOkPHfpbgW2LXQJiGxDhKQRQh+cZi3/VZdCVvz9wTwWot/3jsKk4onyH21JBJRqwo9g885e6J9E9bHAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('430ff05c7540edcb1e3e82e3c416897a')