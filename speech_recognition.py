import websockets
import asyncio
import base64
import json
from configure import auth_key
import pyaudio

common_errors = {'dull': 'doll', 'dahl': 'doll', 'but': 'bought', 'vaccinely': 'facsimile', 'factsimile': 'facsimile'}

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()
 
# starts recording
stream = p.open(
   format=FORMAT,
   channels=CHANNELS,
   rate=RATE,
   input=True,
   frames_per_buffer=FRAMES_PER_BUFFER
)

URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"
 

async def send_receive():
	
	print(f'Connecting websocket to url ${URL}')

	async with websockets.connect(
		URL,
		extra_headers=(("Authorization", auth_key),),
		ping_interval=5,
		ping_timeout=20
	) as _ws:

		r = await asyncio.sleep(0.1)

		session_begins = await _ws.recv()

		print("Waiting for result...")


		async def send():
			loop = asyncio.get_running_loop()
			end_time = loop.time() + 5.0
			counter = 0
			while True:
				try:
					data = stream.read(FRAMES_PER_BUFFER)
					data = base64.b64encode(data).decode("utf-8")
					json_data = json.dumps({"audio_data":str(data)})
					r = await _ws.send(json_data)

				except websockets.exceptions.ConnectionClosedError as e:
					print(e)
					assert e.code == 4008
					break

				except Exception as e:
					print(e)
					assert False, "Not a websocket 4008 error"

				r = await asyncio.sleep(0.01)

				if (loop.time()) >= end_time:
					break


		async def receive():
			loop = asyncio.get_running_loop()
			end_time = loop.time() + 5.0
			while True:
				try:
					result_str = await _ws.recv()
					result = json.loads(result_str)['text']

					if json.loads(result_str)['message_type']=='FinalTranscript':
						result = result.split()[0].lower().replace('.', '')
						return result

				except websockets.exceptions.ConnectionClosedError as e:
					print(e)
					assert e.code == 4008
					break

				except Exception as e:
					print(e)
					assert False, "Not a websocket 4008 error"

				if (loop.time()) >= end_time:
					break
					
		send_result, receive_result = await asyncio.gather(send(), receive(), return_exceptions=True)
		r = await _ws.send(json.dumps({'terminate_session': 'true'}))
		return receive_result

def speech_result() -> str:
	result = asyncio.run(send_receive())
	if result in common_errors:
		result = common_errors[result]
	print()
	print(result)
	print()
	return result

if __name__ == '__main__':
	speech_result()