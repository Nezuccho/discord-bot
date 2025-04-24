import discord
from discord.ext import commands
import logging
import random
import time
import os # สำหรับ env
from dotenv import load_dotenv

# อ่าน Token
load_dotenv() # load ตัวแปรจาก env
token = os.getenv("Discord_token") # access env value

#-------------- Note: CTRL + K + C เพื่อ comment selection

#logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')


intents = discord.Intents.default()
intents.message_content = True

activity = discord.CustomActivity(name="คงจะทำเสร็จในสักวันล่ะมั้งนะ....") # set activity status ใต้ชื่อ
bot = commands.Bot(command_prefix='/',intents=intents,activity=activity) #กำหนด Prefix

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

# command
@bot.command() # ใส่เพื่อประกาศ command
async def ping(ctx):
    await ctx.send('Pong... ฉันควรตอบอย่างงี้ใช่ไหมนะ...?')
    
@bot.command()
async def hello(ctx):
    await ctx.send(f'อ่า สวัสดี ยินดีที่ได้รู้จักนะ! {ctx.author.mention}!')

@bot.command()
async def echo(ctx,*,message): # ส่งข้อความตามที่ส่งไป
    await ctx.send(message)

@bot.command()
async def clear(ctx,limit = 3): # ลบข้อความ
    await ctx.channel.purge(limit=limit)

@bot.command()
async def add(ctx,a:float,b:float): # บวกเลขเฉยๆ
    await ctx.send(a + b)

@bot.command()
async def dice(ctx,amount:int = 1): # ทอยเต๋า 6 หน้า ระบุจำนวนลูกเต๋าได้
    dice_list = []
    await ctx.send("ทอยเต๋า! :game_die:")
    if amount > 1:
        for i in range(amount):
            dice = random.randint(1,6)
            dice_list.append(dice)
            await ctx.send(f'ลูกเต๋าที่ {i+1} ด้านที่ออก: {dice}')
        time.sleep(1)
        await ctx.send(f'รวม: {sum(dice_list)}')
    else:
        dice = random.randint(1,6)
        time.sleep(1)
        await ctx.send(f'ด้านที่ออก: {dice}')
           
bot.run(token, log_handler=handler, log_level=logging.DEBUG) #รันบอท (โดยนำ TOKEN จากบอทที่เราสร้างไว้นำมาวาง)

