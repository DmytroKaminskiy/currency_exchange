def send_tel_message():
    import requests
    import os

    bot_api_key = os.environ['TELEGRAM_BOT_API_KEY']
    channel_name = '@CurrencyExchangeBotHillel'
    message = 'Hello @/?World'

    url = f'https://api.telegram.org/bot{bot_api_key}/sendMessage'

    params = {
        'chat_id': channel_name,
        'text': message,
    }

    return requests.get(url, params=params).json()

print(send_tel_message())
