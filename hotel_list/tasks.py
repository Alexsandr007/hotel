from hotel.celery import app
from .service import send, sending
from .views import *

@app.task
def send_message(name, message, email, name_room = None):
	if name_room == None:
		name1 = 'name: '+name
		text = name1 + '\n'+ message
		send(email, text)
	else:
		name1 = 'name: ' + name
		text = name1 + '\n' + message + '\n' + 'Аренда: '+ name_room
		sending(email, text)