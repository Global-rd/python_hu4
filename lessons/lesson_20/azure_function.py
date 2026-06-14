import azure.functions as func
import logging
import os
from telegram import Telegram

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="f_pythonhu4")
def f_pythonhu4(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    telegram = Telegram(bot_token=os.environ.get("TELEGRAM_BOT_TOKEN"),
                        chat_id=os.environ.get("TELEGRAM_CHAT_ID"))
    
    telegram.send_telegram_message("This is a test message from the class!")

    challenge = req.params.get('challenge')

    if challenge:
        return func.HttpResponse(challenge, status_code=200)
    
    return func.HttpResponse("all good!", status_code=200)
