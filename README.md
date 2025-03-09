<p align="center">
  <img src="https://i.ibb.co/LdqH8ChB/tmpycnd0ygf.jpg" alt="Stelleron-FileStore">

Telegram Bot to store Posts and Documents and it can Access by Special Links.
I Guess This Will Be Usefull For Many People.....😇. 

### Features
- Fully customisable.
- Customisable welcome & Forcesub messages.
- Start Pic, Force Pic
- More than one Posts in One Link.
- 4 ForceSub Channels.

### Setup

- Add the bot to Database Channel with all permission
- Add bot to 4 ForceSub channels as Admin with Invite Users via Link Permission if you enabled ForceSub 

##
### Installation
#### Deploy on Heroku
**Before You Deploy On Heroku, You Should Fork The Repo And Make changes in {procfile - (web to worker)} . In app.json {Size - (free to eco)}.**<br>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)</br>


#### Deploy on Koyeb

The fastest way to deploy the application is to click the **Deploy to Koyeb** button below.


[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/TitanXBots/FileStore-Bot&branch=koyeb&name=filesharingbot)


### 𝑨𝒅𝒎𝒊𝒏 𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔

```
/start - start the bot or get posts

/batch - create link for more than one posts

/genlink - create link for one post

/users - view bot statistics

/broadcast - broadcast any messages to bot users

/stats - checking your bot uptime
```

### Variables
* `API_HASH` Your API Hash from my.telegram.org
* `APP_ID` Your API ID from my.telegram.org
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `DATABASE_URL` Your mongo db url
* `DATABASE_NAME` Your mongo db session name
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_PIC` Optional: URL or file path of the image to be sent as the start message 
* `START_MESSAGE` Optional: start
