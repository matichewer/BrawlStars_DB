from time import sleep
from datetime import datetime
import brawlstats
import mysql.connector
import requests

import logging
from logging.config import fileConfig
from pathlib import Path

def getTime():
	now = datetime.now()
	fecha = now.strftime('%Y-%m-%d')
	hora = now.strftime('%H:%M:%S')
	return (fecha, hora)

def bot_send_text(bot_message):    
    bot_token = '1744210955:AAHgEC8e24vuP2LNyrdT5c-AdoLd7AXtM7E'
    bot_chatID = '70429625'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response

def getMembers():
	client = ''
	try:
		client = brawlstats.Client('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFlMTQ5ZTZlLTZmMDctNDc5NS1iNzQyLTI0NDUxZGRjMDNlMCIsImlhdCI6MTY3MTM5MzY4Niwic3ViIjoiZGV2ZWxvcGVyL2ZlNGU4OWJiLTI5ZjMtMjFiOC05YzBmLTc2MzhhNGMxNmMzNiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTg2LjEyNy4xNzkuMzAiXSwidHlwZSI6ImNsaWVudCJ9XX0.keovNgqp3emXUg9RJaj0z_RR9Q1uOoPjpDEPQyuZ6y4YsCB_ZF5uUJTZEBsKNGis5N7oERjAE_GB9khrLoq6rg')
	except: # catch all exceptions
		msg = "Error making request to BrawlStars"
		log.error(msg)
		bot_send_text(msg)
		exit(1)		
	club = client.get_club('2GVC0QRPY')
	members = club.get_members()
	return members



fileConfig('logs/config.ini', defaults={ 'file-name': Path(__file__).stem })
log = logging.getLogger()

members = getMembers()
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="matute",
	database='brawlstars'
)

(fecha, hora) = getTime()
cursor = mydb.cursor()
sentencia_sql = 'INSERT INTO jugadores VALUES (\"%s\", \"%s\", \"%s\", %i)'
for member in members:
	cursor.execute(sentencia_sql % (fecha, hora, member.tag, member.trophies))


mydb.commit()
cursor.close()
mydb.close()

log.info('Successful registration')
