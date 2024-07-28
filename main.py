import discord
from datetime import datetime, timedelta, timezone
import re
from keep_alive import keep_alive
from pygrowup import Calculator
from dateutil.relativedelta import relativedelta
from utils import *
from syrups import *
from immunization import *
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import json
import asyncio
from threading import Thread
from aiogram import Bot
import pytz

async def send_tel_message(msg):
    bot = Bot(token="6352219140:AAFfaT2n1VbpqZUhSc3GUYiX67nBRLEQiZ4")
    await bot.send_message(chat_id="@SRS_update", text=msg)

def update_telegram(msg):
    asyncio.run(send_tel_message(msg))

async def send_discord_message(content):
  user_ids = [704597807214100530,769965673161424897,1153012994834444449] #Rutvik,Navi,Ni
  for user_id in user_ids:
    user = await client.fetch_user(user_id)
  
    if user:
      await user.send(content)
    else:
      print(f"No user found for ID {user_id}")

def check_job_status(index):
  d = None
  with open("job_schedule.json","r") as f:
    d = json.load(f)
  if not d[index][1]:
    update_telegram(f"SRS Could not updated.")
    asyncio.run_coroutine_threadsafe(send_discord_message(f"SRS Could not updated."), client.loop)
scheduler = BackgroundScheduler(timezone='Asia/Kolkata')
scheduler.start()

d = None
with open("job_schedule.json","r") as f:
  d = json.load(f)
scheduler.remove_all_jobs()
scheduler.add_job(lambda:check_job_status(0), 'cron', hour=int(d[0][0]), minute=5)
scheduler.add_job(lambda:check_job_status(1), 'cron', hour=int(d[1][0]), minute=5)
if not scheduler.running:
  scheduler.start()


def cleanup():
  scheduler.shutdown()
  print("Cleaning up...")
    
atexit.register(cleanup)

invite_link = "https://discord.com/api/oauth2/authorize?client_id=1147098933340946502&permissions=8&scope=bot"
token = 'MTE0NzA5ODkzMzM0MDk0NjUwMg.GB_UtE.qwxFVIlSfZscDqIRzxzgpqfKWx88tHjGV_is-c'

class Channels:
  paedia_dose_calculator = "paedia_dose_calculator"
  paedia_growth_calculators = "paedia_growth_calculators"
  rabies = "rabies"
  iron_sucrose = "iron_sucrose"
  abbreviation = "abbreviation"
  treatment_charts = "treatment_charts"
  calculators = "calculators"
  immunization = "immunization"


async def delete_messages(channel, spare_prefixes=[]):
    messages_to_delete = []
    messages_to_delete_individually = []

    # Store current time
    now = datetime.now(timezone.utc)

    async for message in channel.history(limit=None):
        if (not message.pinned) and (not any(
            message.content.startswith(prefix) for prefix in spare_prefixes)):
            # Check if message is less than 14 days old
            if (now - message.created_at).days < 14:
                messages_to_delete.append(message)
            else:
                messages_to_delete_individually.append(message)

    message_chunks = [
        messages_to_delete[i:i + 100]
        for i in range(0, len(messages_to_delete), 100)
    ]

    for chunk in message_chunks:
        try:
            await channel.delete_messages(chunk)
        except Exception as e:
            print(f"Failed to bulk delete messages due to {e}")
            messages_to_delete_individually.extend(chunk)

    for message in messages_to_delete_individually:
        try:
            await message.delete()
        except discord.Forbidden:
            print(f"Do not have permission to delete message {message.id}")
        except discord.HTTPException as e:
            print(f"Failed to delete message {message.id} due to {e}")

pinned_charts = None
async def find_chart(message, download=False, *args):
  global pinned_charts
  chart_name = [arg.upper() for arg in args]
  if pinned_charts == None:
    pinned_charts = await message.channel.pins()
  for pin in pinned_charts:
    if all(word in pin.content.upper() for word in chart_name):
      if pin.attachments:
        if download:
          await message.reply(pin.attachments[0].url)
        else:
          guild_id = message.guild.id
          channel_id = message.channel.id
          message_id = pin.id
          message_url = f"https://discord.com/channels/{guild_id}/{channel_id}/{message_id}"
          await message.reply(message_url)
        return
  await message.reply(
      f"Sorry, I couldn't find the treatment chart for {' '.join(chart_name)}."
  )

async def calculate_growth(msg, *args):
  commands = ["hfa", "wfh", "wfa", "bmifa", "hcfa"]
  indicators = {
      "hfa": "lhfa",
      "wfh": "wfl",
      "wfa": "wfa",
      "bmifa": "bmifa",
      "hcfa": "hcfa"
  }
  calculator = Calculator(adjust_height_data=False,
                          adjust_weight_scores=False,
                          include_cdc=False,
                          logger_name='pygrowup')
  calculator2 = Calculator(adjust_height_data=False,
                           adjust_weight_scores=False,
                           include_cdc=True,
                           logger_name='pygrowup')

  # Parse the arguments
  command = args[0].replace("$", "")

  if command == "medians":
    # Convert age to months
    age_str = args[1]
    age_in_months = None
    if "yr" in age_str:
      age_in_years = float(age_str.replace("yr", ""))
      age_in_months = age_in_years * 12
    elif "mo" in age_str:
      age_in_months = float(age_str.replace("mo", ""))
    else:
      await msg.reply(
          "Invalid age format. Please use 'yr' for years and 'mo' for months")
      return

    # Check that age is within valid range
    if age_in_months > 240:  # 20 years * 12 months/year
      await msg.reply("Invalid age. Only valid for ages up to 20 years.")
      return
    # Parse sex
    sex = args[2]
    if sex.upper() not in ['M', 'F']:
      await msg.reply("Invalid sex. Please use 'M' for male and 'F' for female"
                      )
      return

    expected = []
    for indicator in ["lhfa", "wfa", "bmifa", "hcfa"]:
      if age_in_months > 60:
        if indicator in ["lhfa", "wfa"]:
          expected.append(
              f"{calculator2.expected_measurement(indicator, age_in_months, sex):.2f}"
          )
        else:
          expected.append("No data available")
      else:
        expected.append(
            f"{calculator.expected_measurement(indicator, age_in_months, sex):.2f}"
        )

    await msg.reply(", ".join([
        f"{i[0]}: {expected[index]}{i[1] if expected[index]!='No data available' else ''} "
        for index, i in enumerate([('Height',
                                    'cm'), ('Weight',
                                            'kg'), ('BMI',
                                                    'kg/m²'), ('HC', 'cm')])
    ]))
    return

  if command not in commands:
    await msg.reply(
        "Invalid command. Please choose from 'hfa', 'wfh', 'wfa', 'bmifa', 'hcfa'"
    )
    return

  # Convert command to indicator
  indicator = indicators[command]

  # Remove units from measurement and convert to float
  measurement = float(extract_number(args[1]))

  # Convert age to months
  age_str = args[2]
  age_in_months = None
  if "yr" in age_str:
    age_in_years = float(age_str.replace("yr", ""))
    age_in_months = age_in_years * 12
  elif "mo" in age_str:
    age_in_months = float(age_str.replace("mo", ""))
  else:
    await msg.reply(
        "Invalid age format. Please use 'yr' for years and 'mo' for months")
    return
  # Check that age is within valid range
  if age_in_months > 240:  # 20 years * 12 months/year
    await msg.reply("Invalid age. Only valid for ages up to 20 years.")
    return

  # Parse sex
  sex = args[3]
  if sex.upper() not in ['M', 'F']:
    await msg.reply("Invalid sex. Please use 'M' for male and 'F' for female")
    return

  # Calculate z-score and expected measurement using appropriate calculator
  z_score, expected = None, None
  if indicator in ['wfl', 'bmifa']:
    # For weight-for-length/height and BMI-for-age, we also need height
    if len(args) < 5:
      await msg.reply(
          "Height is required for this calculation. Please provide height in cm."
      )
      return
    height = float(extract_number(args[4]))
    if age_in_months <= 60:
      z_score = calculator.zscore_for_measurement(indicator, measurement,
                                                  age_in_months, sex, height)
      expected = calculator.expected_measurement(indicator, age_in_months, sex,
                                                 height)
    else:
      await msg.reply("No data available for children older than 60 months.")
      return
  else:
    if age_in_months <= 60:
      z_score = calculator.zscore_for_measurement(indicator, measurement,
                                                  age_in_months, sex)
      expected = calculator.expected_measurement(indicator, age_in_months, sex)
    elif indicator in ["lhfa", "wfa"]:
      z_score = calculator2.zscore_for_measurement(indicator, measurement,
                                                   age_in_months, sex)
      expected = calculator2.expected_measurement(indicator, age_in_months,
                                                  sex)
    else:
      await msg.reply("No data available for children older than 60 months.")
      return

  units = {
      "hfa": "cm",
      "wfh": "kg",
      "wfa": "kg",
      "bmifa": "kg/m²",
      "hcfa": "cm"
  }
  full_words = {
      "hfa": "Height",
      "wfh": "Weight",
      "wfa": "Weight",
      "bmifa": "BMI",
      "hcfa": "Head Circumference"
  }

  # Check nutrition status based on z-score
  if -2 < z_score <= 1:
    nutrition_status = "Normal nutrition status"
  elif -3 < z_score <= -2:
    nutrition_status = "Moderate undernutrition"
  elif z_score <= -3:
    nutrition_status = "Severe undernutrition"
  elif 1 < z_score <= 2:
    nutrition_status = "Possible risk of overweight"
  elif 2 < z_score <= 3:
    nutrition_status = "Overweight"
  elif z_score > 3:
    nutrition_status = "Obesity"
  else:
    nutrition_status = "Data out of normal range"

  await msg.reply(
      f"z-score : {z_score:.2f}, Median(Expected) {full_words[command]} : {expected:.2f}{units[command]}\nNutrition Status: {nutrition_status}"
  )

async def long_msg_send(msg,long_message):

  while len(long_message) > 0:
      # Subtract 6 for the triple backticks at the start and end
      if len(long_message) > 1994:  
          # Find the last newline character within the limit
          split_index = long_message[:1994].rfind('\n')
          to_send = long_message[:split_index]
          long_message = long_message[split_index:]
      else:
          to_send = long_message
          long_message = ""

      # Wrap the message segment in triple backticks and send it
      await msg.reply(f"```{to_send}```")

def processFlag(args,flag):
  details = False

  if flag in args:
    args.remove(flag)
    details = True

  return args, details

async def eval_immunization(msg, *arg):
    arg,isD = processFlag(list(arg),"-d")
    command = arg[0].replace("$", "")
    if command == "immunization":
      await long_msg_send(msg,format_schedule(immunization_schedule,isD))

    if command == "synonyms":
      await msg.reply(f"```{ format_synonyms(synonyms) }```")

    if command == "age":
      if len(arg)<2:
        await msg.reply("Enter Appropriate Age And/Or Vaccine Name")      
      reply = get_vaccine_schedule_by_age_and_vaccine(age=arg[1],vaccine_name=arg[2] if len(arg)>2 else None)
      if reply==None or reply=={}:
        await msg.reply("Enter Appropriate Age And/Or Vaccine Name")
      else:
        await long_msg_send(msg,format_schedule(reply,isD))

    if command == "vaccine":
      if len(arg)<2:
        await msg.reply("Enter Appropriate Age And/Or Vaccine Name")      
      reply = get_vaccine_schedule_by_age_and_vaccine(age=arg[2] if len(arg)>2 else None,vaccine_name=arg[1])
      if reply==None or reply=={}:
        await msg.reply("Enter Appropriate Age And/Or Vaccine Name")
      else:
        await long_msg_send(msg,format_schedule(reply,isD))


async def eval_calculators(msg, *arg):
  command = arg[0].replace("$", "") 
  if command == "bmi":
    height = extract_number(arg[1])
    if height == None:
      await msg.reply("Enter valid height in cm.")
    weight = extract_number(arg[2])
    if weight == None:
      await msg.reply("Enter valid weight in kg.")
    bmi = weight / ((height / 100)**2)
    bmi_status = ''
    if bmi < 18.5:
      bmi_status = 'underweight'
    elif 18.5 <= bmi < 25:
      bmi_status = 'within the normal weight range'
    elif 25 <= bmi < 30:
      bmi_status = 'overweight'
    else:
      bmi_status = 'obese'
    await msg.reply(f"BMI: {bmi:.2f} kg/m2, Status: {bmi_status}")

  elif command == "edd":
    lmp_date_str = arg[1]
    try:
      lmp_date = datetime.strptime(lmp_date_str, '%d/%m/%Y') # Parse the date as day/month/year
      edd_date_naegele = lmp_date + relativedelta(months=9) # add 9 months
      edd_date_naegele = edd_date_naegele + timedelta(days=7) # add 7 days
      edd_date_280 = lmp_date + timedelta(days=280) # add 280 days
      await msg.reply(f"Estimated Due Date (EDD)\nbased on 280 days: {edd_date_280.strftime('%d/%m/%Y')}\nbased on naegele's: {edd_date_naegele.strftime('%d/%m/%Y')}")
    except ValueError:
      await msg.reply("Enter valid date in format DD/MM/YYYY.")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
abbr = abbr()


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


help_messages = {
    Channels.paedia_dose_calculator:
    'Here are the commands you can use:\n'
    '`$pcm weight concentration(125/5)`\n'
    '`$levocet age concentration(2.5/1)`\n'
    '`$ambroxol age concentration(15/5)`\n'
    '`$azithro weight severity(mild/severe) concentration(200/5)`\n'
    '`$mox weight severity(mild/severe) concentration(125/5)`\n'
    '`$moxclav weight concentration(200+28.5/5)`\n'
    '`$dom weight concentration(1/1)`\n'
    '`$ifa weight concentration(20/1)`\n'
    '`$zn age concentration(20/5)`\n'
    '`$dmr age concentration(13.5/5)`\n'
    '`$metro weight concentration(100/5)`\n'
    '`$salbu age concentration(2/5)`\n'
    'Example : $pcm 10kg 125/5\n'
    'Note: Use mox_conc + clav_conc / ml for moxclav\n'
    '`$clear`: Clear all messages except pinned.\n'
    '`$help`: Displays this help message.',
    Channels.rabies:
    'Here are the commands you can use:\n'
    '`$dates date(DD/MM/YYYY)`:if no date privided today is taken as 0 dose\n'
    '`$clear`: Clear all messages except pinned.\n'
    '`$help`: Displays this help message.',
    Channels.iron_sucrose:
    'Here are the commands you can use:\n'
    '`$pints weight Hb ANC(1/0) target_Hb(11) concentration(200/100) pint(100)`\n'
    '`$clear`: Clear all messages except pinned.\n'
    '`$help`: Displays this help message.',
    Channels.abbreviation:
    'Here are the commands you can use:\n'
    '`$find abbr`: Display Fullform of abbr.\n'
    '`$clear`: Clear all messages except pinned.\n'
    '`$help`: Displays this help message.',
    Channels.treatment_charts:
    'Here are the commands you can use:\n'
    '`$find query`: Find treatment chart of query.\n'
    '`$chart query`: Find and send treatment chart of query.\n'
    '`$clear`: Clear all messages except pinned and !chart.\n'
    '`$help`: Displays this help message.',
    Channels.paedia_growth_calculators:
    'Here are the commands you can use:\n'
    '`$hfa [height] [age] [sex]`: height-for-age.\n'
    '`$wfh [weight] [age] [sex] [height]`: weight-for-height.\n'
    '`$wfa [weight] [age] [sex]`: weight-for-age.\n'
    '`$bmifa [bmi] [age] [sex] [height]`: BMI-for-age.\n'
    '`$hcfa [head_circumference] [age] [sex] [height]`: head-circumference-for-age.\n'
    'Example: $wfa 5kg 3yr M 50cm\n'
    '`$medians [age] [sex]`: Median(Expected) Values\n'
    '`$clear`: Clear all messages except pinned.\n'
    '`$help`: Displays this help message.\n',
    Channels.calculators:
    'Here are the commands you can use:\n'
    '`$bmi [height] [weight]`: Body-Mass-Index.\n'
    '`$edd lmp_date(DD-MM-YYYY)`: Estimated Due Date.\n'
    '`$clear`: Clear all messages except pinned.\n'
    '`$help`: Displays this help message.\n',
    Channels.immunization:
    'Here are the commands you can use:\n'
    '`$immunization`: Entire Schedule\n'
    '\n'
    '`$age [age]`: Schedule Based On Age\n'
    '`$age 10wk` = at 10 week\n'
    '`$age 0` = at birth\n'
    '`$age -3wk` =  3week before birth (ANC)\n'
    '`$age <10mo` = before 10 month\n'
    '`$age <=10yr` = before with 10 year\n'
    '`$age >10day` = after 10 days\n'
    '`$age >=10wk` = after with 10wk\n'
    '`$age 2wk,10mo` = between 2 week to 10 month\n'
    '\n'
    '`$vaccine [vaccine]`: Schedule Based On Vaccine Name.\n'
    '`$vaccine penta`: all pentavalent.\n'
    '`$vaccine penta,2`: pentavalent-2.\n'
    '`$vaccine DPT,boost`: all DPT booster.\n'
    '`$vaccine DPT,boost,2`: DPT booster-2.\n'
    '\n'
    '`$vaccine [vaccine] [age]`: Schedule Based On Vaccine Name + Age.\n'
    '`$age [age] [vaccine]`: Schedule Based On Vaccine Name + Age.\n'    
    '`$synonyms`: Synonyms that can be used for vaccine names.\n'
    '`$[command] -d`: Use -d to get details of vaccines.\n Ex `$age <1yr -d` `$vaccine -d penta`\n'
    '\n'
    '`$clear`: Clear all messages except pinned.\n'
    '`$help`: Displays this help message.\n',
}

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # Make content and command keys case-insensitive
  commands = message.content.lower().split("\n")
  for content in commands:
    # Check for $help command
    if message.channel.name in help_messages and (content.startswith('$help') or content.startswith('r help')):
      await message.reply(help_messages[message.channel.name])
      continue

    # If the message is in a recognized channel and starts with $ or 'R '
    if message.channel.name in help_messages and (content.startswith('$') or content.startswith('r ')):
      # Replace 'r ' with '$'
      if content.startswith('r '):
        content = re.sub(r'^r\s', '$', content)

      if message.channel.name == Channels.paedia_dose_calculator:
        for command, func in command_dict.items():
          if content.startswith(command):
            args = content.split(' ')[1:]
            dose = func(*args)
            await message.reply(dose)
            break

      if message.channel.name == Channels.rabies and content.startswith(
          '$dates'):
        await message.reply(rabies_dates(*(content.split(' ')[1:])))

      if message.channel.name == Channels.iron_sucrose and content.startswith(
          '$pints'):
        await message.reply(iron_sucrose_pints(*(content.split(' ')[1:])))

      if message.channel.name == Channels.abbreviation and content.startswith(
          '$find'):
        await message.reply(abbr.find_abbreviation(*(content.split(' ')[1:])))

      if message.channel.name == Channels.treatment_charts and content.startswith(
          '$chart'):
        await find_chart(message, True, *(content.split(' ')[1:]))

      if message.channel.name == Channels.treatment_charts and content.startswith(
          '$find'):
        await find_chart(message, False, *(content.split(' ')[1:]))

      if message.channel.name == Channels.paedia_growth_calculators and any(
          content.startswith(f'${i}')
          for i in ["hfa", "wfh", "wfa", "bmifa", "hcfa", "medians"]):
        await calculate_growth(message, *(content.split(' ')))

      if message.channel.name == Channels.calculators and any(
          content.startswith(f'${i}') for i in ["bmi","edd"]):
        await eval_calculators(message, *(content.split(' ')))

      if message.channel.name == Channels.immunization and any(
          content.startswith(f'${i}') for i in ["immunization","synonyms","age","vaccine"]):
        await eval_immunization(message, *(content.split(' ')))

      if content.startswith('$clear'):
        if message.channel.name == Channels.treatment_charts:
          await delete_messages(message.channel, spare_prefixes=["!chart"])
        else:
          await delete_messages(message.channel)

keep_alive(client,scheduler)
client.run(token)