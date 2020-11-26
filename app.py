from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from Blockchain import *
import datetime as datetime


obj = BlockChain()
app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  return render_template( './index.html' )

def messageRecived():
  print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  obj.add_block(Block(0,str(datetime.datetime.now()),str(json)))
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )
  for b in obj.chain:
      print("******************************")
      print(b)
      print("******************************")

if __name__ == '__main__':
  socketio.run( app, debug = True )
