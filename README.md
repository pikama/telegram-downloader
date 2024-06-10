# telegram-downloader
A tool for save media from Telegram.
The following type of chat / message can be allowed:
- public/private chat
- a group/channel tuned on 'restrict saving content' function
- self destructing photo/video/voice

# Configuration
Getting your own API keys:
1. Visit https://my.telegram.org/apps and login with your Telegram account
2. Create a new application
3. Paste 'api_id' and 'api_hash' in 'telegram-downloader.py'

# Installation (Windows)
`pip install -r requirements.txt`

# Usage
`py telegram-downloader.py`

0. Login if this is your first time using
1. Enter username / Select from your chat list
2. Select the type of message (select 0 (means all type) if it's a self-destructing photo/video/voice)
3. Enter the number of messages you want to display. It start counting from the latest message.
4. Enter the message no. of the file you want to download
5. Set whether you need to send the file back to 'saved message'
6. Wait for the media download to complete
