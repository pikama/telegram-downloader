from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterVideo, InputMessagesFilterVoice, InputMessagesFilterDocument, InputMessagesFilterMusic, InputMessagesFilterRoundVideo, InputMessagesFilterGif, InputMessagesFilterPhotoVideo
import sys

class messageFilter():
	filter_list = [None, InputMessagesFilterPhotos, InputMessagesFilterVideo, InputMessagesFilterPhotoVideo, InputMessagesFilterVoice, InputMessagesFilterRoundVideo, InputMessagesFilterMusic, InputMessagesFilterGif, InputMessagesFilterDocument]
	print_text = '0: all \n1: photo \n2: video \n3: photo/video \n4: voice \n5: round video \n6: audio \n7: gif \n8: other document'

sys.modules[__name__] = messageFilter
