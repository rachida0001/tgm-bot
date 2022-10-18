import hikari
import lightbulb
import os
from dotenv import load_dotenv

load_dotenv()

bot = lightbulb.BotApp(
    token=os.getenv('TOKEN'),
    intents=hikari.Intents.ALL_UNPRIVILEGED)
)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 

cred = credentials.Certificate({
    "type": os.getenv("FIREBASE_TYPE"),
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY"),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
    "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER"),
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_CERT_URL")
})
firebase_admin.initialize_app(cred, {'databaseURL': os.getenv('dbUrl')})


ref = db.reference('/')
ref = db.reference('subjects')

@bot.command
@lightbulb.option('suggestion', 'write a suggestion', type=str)
@lightbulb.command('suggest', 'suggest a TGM subject')
@lightbulb.implements(lightbulb.SlashCommand)
async def suggestion(ctx):
    ref.push({
    'title' : ctx.options.suggestion,
    'status' : 'PENDING',
    'resources' : []
    })
    await ctx.respond("Your suggestion is in th db")

bot.run()