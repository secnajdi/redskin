#Calling ready-made libraries and modules
import os
import openai
from aiogram import Bot , Dispatcher , executor , types
#Calling custom library and modules
from keep_alive import keep_alive
#Start code >>>
bot = Bot(token = "Your Token")
disp = Dispatcher(bot)
openai.api_key = "Your OpenAI API Key"
keep_alive()
@disp.message_handler(commands = ["start","help"])
async def welcome(message:types.Message):
    await message.reply("Hello")
@disp.message_handler()
async def gpt(message:types.Message):
    response = openai.completions.create(
    model ="text-davinci-003", 
    prompt=message.text,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0)
    await message.reply(response.choices[0].text)
if __name__ == "__main__":
    executor.start_polling(disp)
#End code
#...>>> Develpoer : Mohammad Javad Najdi
#...>>> gmail : secu.najdi@gmail.com
#...>>> Social media : Telegram : @J_najdi and instagram : najdires





