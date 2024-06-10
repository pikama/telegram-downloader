import sys
from telethon.tl.types import DocumentAttributeSticker, DocumentAttributeAudio, DocumentAttributeAnimated

def getMessageType(message): 

    def checkSticker(attributes):
        for attr in attributes:
            if isinstance(attr, DocumentAttributeSticker):
                return True
        return False 

    def checkGif(attributes):
        for attr in attributes:
            if isinstance(attr, DocumentAttributeAnimated):
                return True
        return False     

    def checkAudio(attributes):
        for attr in attributes:
            if isinstance(attr, DocumentAttributeAudio):
                return True
        return False 

    chat_media_tag = None
    if message.media is not None:
        msg_media_detail = message.media
        if hasattr(msg_media_detail, 'photo'):
            chat_media_tag = '(secret photo)' if msg_media_detail.ttl_seconds is not None else '(photo)' 
        elif hasattr(msg_media_detail, 'document'):
            if bool(msg_media_detail.video):
                chat_media_tag = '(secret video)' if msg_media_detail.ttl_seconds is not None else '(video)'
            elif bool(msg_media_detail.voice):
                chat_media_tag = '(secret voice)' if msg_media_detail.ttl_seconds is not None else '(voice)'
            elif bool(msg_media_detail.round):
                chat_media_tag = '(round video)'
            else:
                chat_media_atts = message.media.document.attributes
                if checkSticker(chat_media_atts):
                    chat_media_tag = '(sticker)'
                elif checkAudio(chat_media_atts):
                    chat_media_tag = '(audio)'
                elif checkGif(chat_media_atts):
                    chat_media_tag = '(gif)'
                else:         
                    chat_media_tag = '(document)'
        else:
            chat_media_tag = '(other)'
    return chat_media_tag

sys.modules[__name__] = getMessageType
