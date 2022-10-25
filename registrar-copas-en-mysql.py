import brawlstats
import mysql.connector
import requests
import logging as log

def bot_send_text(bot_message):    
    bot_token = '1744210955:AAHgEC8e24vuP2LNyrdT5c-AdoLd7AXtM7E'
    bot_chatID = '70429625'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response

log.basicConfig(handlers=[
								log.FileHandler(filename="/home/wecher/Git/BrawlStars_DB/logs/registrar-copas-en-mysql.log", 
												encoding='utf-8',
												mode='a+')
							],
                    format='%(asctime)s, %(levelname)-8s, [%(filename)s:%(funcName)s:%(lineno)s], %(message)s',
                    datefmt='%Y-%m-%d, %H:%M:%S, %A', 
					level=log.INFO)

# Token Brawl Stars
client = ''
try:
	client = brawlstats.Client('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjIyNmYyOTc2LTBhYzgtNDE0MC05NTMyLTdhMmQzY2ZlY2ZlNCIsImlhdCI6MTY2NTI2MzE1OCwic3ViIjoiZGV2ZWxvcGVyL2ZlNGU4OWJiLTI5ZjMtMjFiOC05YzBmLTc2MzhhNGMxNmMzNiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTUyLjE2OS40Ny4xNjIiXSwidHlwZSI6ImNsaWVudCJ9XX0.gzk2ZKillueFmsvShvEiNjqR3zkj2p09Fqsw7ufqJ_ruJpkMtDeZ7XVQD3ybg2Gs5cSoBZEax7wB5kidyd9XrQ')
except: # catch all exceptions
	msg = "Error making request to BrawlStars"
	log.critical(msg)
	bot_send_text(msg)
	exit(1)
	
club = client.get_club('2GVC0QRPY')
members = club.get_members()



mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="matute",
	database='brawlstars'
)
cursor = mydb.cursor()
sentencia_sql = 'INSERT INTO jugadores VALUES (CURDATE(), CURTIME(), \"%s\", %i)'
for member in members:
	cursor.execute(sentencia_sql % (member.tag, member.trophies))


mydb.commit()
cursor.close()
mydb.close()

log.info('Successful registration')
