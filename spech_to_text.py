import asyncio
#import time
import websockets
import os
from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'zero_ru.cd_cont_4000'),
    lm=False,
    jsgf=os.path.join(model_path, 'calc2.jsgf'),
    dic=os.path.join(model_path, 'vocabular.dict')
)
print("initialized")

def readValues():
    '''do stuff that returns the values for database'''
    pass


def inserdata(val):
    '''insert values into mysql'''
    pass

async def ph(websocket, path):
    # while True:
    #     message = 'update111111111111' 
    #     # here we receive message that the data
    #     # has been added and need to message the
    #     # browser to update
    print('socket executed')
    #     
    while True:
        for phrase in speech:
            print(phrase)
            await websocket.send(str(phrase))

    # await asyncio.wait([websocket.send(phrase) for phrase in speech])


async def main():  # maybe use this to get/write to the database etc
    while True:  # instead of the loop at bottom
        print('main executed')
        await asyncio.sleep(20)


start_server = websockets.serve(ph, '0.0.0.0', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_forever()
