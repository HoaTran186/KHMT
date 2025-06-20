import telegram
async def send_telegram(photo_path="alert.png"):
    try:
        my_token = "6797803638:AAFSkRBKPabgUg2knQJI181hoypKBu9caWE"
        bot = telegram.Bot(token=my_token)
        await bot.send_photo(chat_id="7084199172", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiêm!")
        # bot.sendPhoto(chat_id="7084199172", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiêm!")
    except Exception as ex:
        print("Can not send message telegram ", ex)

    print("Send sucess")
    
