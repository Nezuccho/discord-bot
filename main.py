import discord
from discord.ext import commands
import logging

# อ่าน Token
file = open("token.txt","r")
token = file.read()
file.close()
#-------------- Note CTRL + K + C เพื่อ comment selection

#logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/',intents=intents) #กำหนด Prefix

@bot.event
async def on_ready() : #เมื่อระบบพร้อมใช้งาน
    print("Bot Started!") #แสดงผลใน CMD
    print(f'We have logged in as {bot.user}')
    
@bot.event
async def on_message(message) : #ดักรอข้อความใน Chat
    if message.author == bot.user:
        return
    
    await bot.process_commands(message) 
    
#     if message.content.startswith('/hello'):
#         await message.channel.send(f'อ่า สวัสดี ยินดีที่ได้รู้จักนะ! {message.author.display_name}!')
        
#     if message.content.startswith('/ping') : #เมื่อข้อความในตัวแรกมีคำว่า ping
#        await message.channel.send('Pong... ฉันควรตอบอย่างงี้ใช่ไหมนะ...?') #ข้อความที่ต้องการตอบกลับ

@bot.command() # ใส่เพื่อประกาศ command
async def ping(ctx):
    await ctx.send('Pong... ฉันควรตอบอย่างงี้ใช่ไหมนะ...?')
    
@bot.command()
async def hello(ctx):
    await ctx.send(f'อ่า สวัสดี ยินดีที่ได้รู้จักนะ! {ctx.author.display_name}!')

@bot.command()
async def echo(ctx,*,message): # ส่งข้อความตามที่ส่งไป
    await ctx.send(message)

@bot.command()
async def clear(ctx,limit = 1): # ลบข้อความ
    await ctx.channel.purge(limit=limit)

@bot.command()
async def add(ctx,a:float,b:float):
    await ctx.send(a + b)
       
bot.run(token, log_handler=handler, log_level=logging.DEBUG) #รันบอท (โดยนำ TOKEN จากบอทที่เราสร้างไว้นำมาวาง)

