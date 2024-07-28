from flask import Flask, request
from threading import Thread
import asyncio
import json

app = Flask('')
client = None
scheduler = None

@app.route('/')
def home():
  return "I'm alive"


@app.route('/send_message', methods=['POST'])
def send_message():
  type = request.form['type']
  if(type=="re_schedule"):
    d = [(i,False) for i in request.form['content'].split(',')]
    with open("job_schedule.json","w") as f:
      json.dump(d,f)
    scheduler.remove_all_jobs()
    scheduler.add_job(lambda: check_job_status(0), 'cron', hour=int(d[0][0]), minute=5)
    scheduler.add_job(lambda: check_job_status(1), 'cron', hour=int(d[1][0]), minute=5)
    if not scheduler.running:
        scheduler.start()
  if(type=="job_status"):
    content = request.form['content']
    num = request.form['num']
    print(num,content)
    d = None
    with open("job_schedule.json","r") as f:
      d = json.load(f)
    with open("job_schedule.json","w") as f:
      d[int(num)][1] = False if int(content)==0 else True
      json.dump(d,f)
  return 'Message sent to Discord', 200


async def send_discord_message(content):
  user_ids = [704597807214100530,769965673161424897,1153012994834444449] #Rutvik,Navi,Ni
  for user_id in user_ids:
    user = await client.fetch_user(user_id)

    if user:
      await user.send(content)
    else:
      print(f"No user found for ID {user_id}")


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive(c,s):
  global client,scheduler
  client = c
  scheduler = s
  t = Thread(target=run)
  t.start()
