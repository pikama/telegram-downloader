# telegram-downloader
A tool for save media from telegram.
The following type of chat / message can be allowed:
- public/private chat
- a group/channel tuned on 'restrict saving content' function
- self destructing photo/video/voice

# Installation (Windows)
`pip install -r requirements.txt`

# Usage
`py telegram-downloader.py`

- Login if this is your first time using
- Enter username / Select from your chat list
- Select the type of message (select 0 (means all type) if it's a self-destructing photo/video/voice)
- Enter the number of messages you want to display. It start counting from the latest message.
- Enter the message no. of the file you want to download
- Set whether you need to send the file back to 'saved message'
- Wait for the media download to complete
