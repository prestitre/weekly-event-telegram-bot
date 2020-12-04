from urllib.request import Request, urlopen
from datetime import datetime, date, time, timedelta
from bot import telegram_chatbot
import configparser as cfg
import asyncio

bot = telegram_chatbot("config.cfg")
config = "config.cfg"


def getData(url):
    req = Request(url, headers={"User-Agent":"Mozilla/5.0"})
    data = urlopen(req).read().decode("utf-8")
    data = data.split("\n")
    weekNumber = date.today().isocalendar()[1]
    yearNumber = date.today().year
    data = makeData(data, weekNumber, yearNumber)
    return data

def makeData(data, wNumber, yNumber):
    outer = []
    for i in range(len(data)):
        if data[i].strip() == "BEGIN:VEVENT":
            j = 0
            inner = []
            while(data[i+j].strip() != "END:VEVENT"):
                cutOut = len(data[i+j])-1
                if data[i+j][:4] == "URL:":
                    inner.append(makeURL(data[i+j], cutOut))
                elif data[i+j][:8] == "SUMMARY:":
                    inner.append(makeTitle(data[i+j], cutOut))
                elif data[i+j][:8] == "DTSTART:":
                    dt = makeDate(data[i+j][8:cutOut])
                    if wNumber == dt.isocalendar()[1] and yNumber == dt.year:
                        inner.append(dt)
                j += 1
            if len(inner) == 3:
                outer.append(inner)
    return sorted(outer)

def makeURL(data, cutOut):
    return data[4:cutOut]
    
def makeTitle(data, cutOut):
    return data[8:cutOut]

def makeDate(data):
    date = datetime(int(data[:4]), int(data[4:6]), int(data[6:8]), int(data[9:11]), int(data[11:13]))
    return date

# format(e_s(i[1]), e_s(i[2]), e_s(i[0]))
def makeMsg(data):
    week = data[0][0].isocalendar()[1]
    days = [0,0,0,0,0,0,0]
    msg = e_s("*- Add your opening line here -*").format(week)
    timediff_hours = timedelta(hours=int(get_timedelta_from_config(config)))
    for i in data:
        if i[0].weekday() == 0:
            if days[i[0].weekday()] == 0:
                msg = msg + "\n\n*MON:*\n"
            msg = msg + "[{}]({}) {:%H:%M}\n".format(e_s(i[1]), e_s(i[2]), (i[0] + timediff_hours))
        if i[0].weekday() == 1:
            if days[i[0].weekday()] == 0:
                msg = msg + "\n*TUES:*\n"
            msg = msg + "[{}]({}) {:%H:%M}\n".format(e_s(i[1]), e_s(i[2]), (i[0] + timediff_hours))
        if i[0].weekday() == 2:
            if days[i[0].weekday()] == 0:
                msg = msg + "\n*WED:*\n"
            msg = msg + "[{}]({}) {:%H:%M}\n".format(e_s(i[1]), e_s(i[2]), (i[0] + timediff_hours))
        if i[0].weekday() == 3:
            if days[i[0].weekday()] == 0:
                msg = msg + "\n*THURS:*\n"
            msg = msg + "[{}]({}) {:%H:%M}\n".format(e_s(i[1]), e_s(i[2]), (i[0] + timediff_hours))
        if i[0].weekday() == 4:
            if days[i[0].weekday()] == 0:
                msg = msg + "\n*FRI:*\n"
            msg = msg + "[{}]({}) {:%H:%M}\n".format(e_s(i[1]), e_s(i[2]), (i[0] + timediff_hours))
        if i[0].weekday() == 5:
            if days[i[0].weekday()] == 0:
                msg = msg + "\n*SAT:*\n"
            msg = msg + "[{}]({}) {:%H:%M}\n".format(e_s(i[1]), e_s(i[2]), (i[0] + timediff_hours))
        if i[0].weekday() == 6:
            if days[i[0].weekday()] == 0:
                msg = msg + "\n*SUN:*\n"
            msg = msg + "[{}]({}) {:%H:%M}\n".format(e_s(i[1]), e_s(i[2]), (i[0] + timediff_hours))
        days[i[0].weekday()] += 1
    msg = msg + e_s("\n\n- Add something after your report -\n")
    return msg


def e_s(msg):
    """Return a string, with reserved characters escaped"""
    msg = msg.replace(".", "\\.")
    msg = msg.replace("=", "\\=")
    msg = msg.replace("-", "\\-")
    msg = msg.replace("(", "\\(")
    msg = msg.replace(")", "\\)")
    msg = msg.replace("]", "\\]")
    msg = msg.replace("!", "\\!")
    return msg


def get_recip_from_config(config, language):
    parser = cfg.ConfigParser()
    parser.read(config)
    return parser.get("magic", "message_recipient")

def get_timedelta_from_config(config):
    parser = cfg.ConfigParser()
    parser.read(config)
    return parser.get("magic", "time_diff_from_source")


def main():
    """Main program flow. Runs functions to gather data, make message and print it, as well as send it."""
    data = getData(bot.url)
    """Test if there is data coming back from your request"""
    if len(data) > 0:
        message = makeMsg(data)
        bot.send_message(message, get_recip_from_config(config))

if __name__ == "__main__":
    main()
