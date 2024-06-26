from telethon import TelegramClient
from pathlib import Path
import asyncio, asyncstdlib
import yaml
import getMessageType, messageFilter

async def main():
    try:
        with open("config.yaml") as f:
            cfg = yaml.safe_load(f)
        api_id = cfg['api_id']
        api_hash = cfg['api_hash']
        default_chat_ID = cfg['default_chat_ID']
    except:
        print("config.yaml not found")
        exit()

    media_path = '.\\download\\'
    Path(media_path).mkdir(parents=True, exist_ok=True)
    message_filter_list = messageFilter.filter_list

    try:
        cli = TelegramClient('user', api_id, api_hash)
        print('ready to start...')
        await cli.start()
    except:
        print('please make sure your api_id and api_hash are valid')
        exit()

    # Select a chat by id / get from list
    chat_ID_input = input('Insert chat username/ID (type 0 as default / 1 get from list): ')
    if chat_ID_input == '0':
        chat_ID = default_chat_ID
    elif chat_ID_input == '1': # print all chat
        chat_list = []
        async for chat_dialog in cli.iter_dialogs(archived=False, ignore_migrated=True):
            chat_list.append({"id": chat_dialog.id, "title": chat_dialog.title})
        chat_list_ID = chatListHandler(chat_list)
        chat_ID = abs(int(chat_list_ID))
    elif chat_ID_input.isdigit():
        chat_ID = int(chat_ID_input)
    else:
        chat_ID = chat_ID_input

    print(f'Chat ({chat_ID}) has been selected')

    # Get message type and amount
    print(messageFilter.print_text)
    while True:
        msg_filter_input = input('Select message type: ')
        if msg_filter_input.isdigit() and int(msg_filter_input) + 1 <= len(message_filter_list):
            msg_filter = message_filter_list[int(msg_filter_input)]
            break
        else:
            print('Invalid input')
    last_msg_limit = input('Insert number of messages (from recent message): ')

    # Print Message
    try:
        msg_list = await printMsg(cli, chat_ID, int(last_msg_limit), msg_filter)
        if msg_list == []:
            print('No message found')
            exit()
    except Exception as e:
        print(e)
        print('User not found / You don\'t have permission to access')
        exit()

    # Select a message(file) to download / + send to saved message
    msg_ID_input = input('Select message id: ')
    msg_ID = msg_list[int(msg_ID_input)]
    send_back_input = input('Send back to saved messages(Y/N): ').upper()

    target_msg = await cli.get_messages(chat_ID, ids=msg_ID)  

    try:
        if target_msg.media.photo != None:
            await saveFile(cli, target_msg.media, media_path, 'photo', send_back_input)
    except AttributeError:
        try:
            if target_msg.media.document != None:
                if bool(target_msg.media.video) or bool(target_msg.media.round):
                    await saveFile(cli, target_msg.media, media_path, 'video', send_back_input)
                elif bool(target_msg.media.voice):
                    await saveFile(cli, target_msg.media, media_path, 'audio', send_back_input)
                else:
                    await saveFile(cli, target_msg.media, media_path, 'document', send_back_input)
        except AttributeError:
            print("not a media type")


async def printMsg(cli, chat_ID, last_msg_limit, msg_filter):
    msg_list = []
    all_msg = cli.iter_messages(chat_ID, limit=last_msg_limit, filter=msg_filter)
    async for idx, message in asyncstdlib.enumerate(all_msg):
        chat_media_tag = getMessageType(message)
        print(f"{idx}: {chat_media_tag or '(text only)'} {message.text}")
        msg_list.append(message.id)  
    return msg_list

async def saveFile(cli, file, media_path, file_type, send_back):
    print('Downloading', file_type, '...')
    file_name = await cli.download_media(file, media_path)
    print('Done downloading: ', file_name.replace(media_path, ''))
    if send_back == 'Y':
        print("Uploading...")
        await cli.send_file('me', open(file_name, 'rb'))
        print(file_type, 'was sent to your saved messages')
        await asyncio.sleep(0)

def chatListHandler(chat_list):
    chat_length = len(chat_list)
    no_of_page = 20
    curr_page = 0

    while True:
        curr_page_last = (curr_page + 1) * no_of_page if (curr_page + 1) * no_of_page < chat_length else chat_length
        for i in range(curr_page * no_of_page, curr_page_last):
            print(i, ':', chat_list[i]["title"])

        while True:
            chat_list_ID = input('Choose your chat (P for previous page / N for next page): ').upper()

            if chat_list_ID.isdigit():
                if int(chat_list_ID) < chat_length:
                    return chat_list[int(chat_list_ID)]["id"]
                else:
                    print('Invalid input')
            elif chat_list_ID == 'P':
                if curr_page != 0:
                    curr_page -= 1
                    break
                else:
                    print('Already to the first page')
            elif chat_list_ID == 'N':
                if (curr_page + 1) * no_of_page < chat_length:
                    curr_page += 1
                    break
                else:
                    print('No more chat can be display')
            else:
                print('Invalid input')
    return


if '__main__' == __name__:
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nbye bye')
