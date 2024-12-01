import asyncio
import socket
import struct
import logging
import configparser
from keyframes import *
from aioconsole import ainput
from module.master_modules import * 

# teleport_dict = {
#     "kakariko" : [1797.0, 222.0, 1083.0],
# }

log_file = "UltraCam_Console.log"
SequenceName = "Default"
prevcommand = "help"

logging.basicConfig(filename=log_file,
                    format="{message}",
                    style='{',
                    datefmt="%H:%M:%S",
                    level=logging.DEBUG)

if log_file is not None:
    logging.getLogger().addHandler(logging.StreamHandler())

config = configparser.ConfigParser()

config.read("console.ini")

if config.has_section("Console"):
    host = config.get("Console", "IP")
    port = config.get("Console", "port")
else:
    host = "127.0.0.1"
    port = "5555"

amount = 5


## ~~~ COMMAND DICT ~~~
##
## ENTRY : COMMAND NAME
## LIST 1 : PACKET
## LIST 2 : DESCRIPTION
## LIST 3 : FUNCTION
## LIST 4 : TYPE
##
## EXAMPLE ON HOW TO USE : 
## "spawn" : [packet(1), "Spawns stuff.", COMMAND(RequestActor.from_sentence), "TYPE"]
## TYPES : graphics, utility cheats
## NOT ALL COMMANDS WORK ON 2.5 ATM.
## CHECK MODULE FOLDER TO SEE HOW THE STRUCTS WORK!
##
## ~~~~~~~~~~~~~~~~~~~~

command_dict = {
    "spawn": [1, 'Spawns anything : Type "spawn random" for a random Enemy.', RequestActor.from_sentence, "utility"],
    "tp": [10, "Teleports player.", RequestVector3F.from_sentence , "utility"],
    "cords": [11, "Prints Player Cordinates.", RequestResponse.from_sentence, "utility"],
    "settime": [-1, "Sets current day time.", RequestSetTime.settime, "graphics"],
    "timespeed": [21, "Sets the speed of time of day.", RequestFloat.from_sentence, "graphics"],
    "gettime": [24, "Pauses the game but let's the freecam still move", RequestBool.from_sentence, "utility"],
    "changeweather": [25, "Changes the weather, currently random.", RequestBool.from_sentence, "graphics"],
    "pause": [23, "Pauses the game but let's the freecam still move", RequestBool.from_sentence, "utility"],
    "godmode": [32, "Makes the player Invincible.", RequestBool.from_sentence, "cheats"],
    "kill": [31, "Kills the player.", RequestBool.from_sentence, "cheats"],
    "killall": [110, "Kills All Enemies.", RequestBool.from_sentence, "cheats"], # Doesn't work on 2.5
    "heal": [30, "Heals the player.", RequestInt.from_sentence, "cheats"],
    "healall": [111, "Heals All Enemies.", RequestBool.from_sentence, "cheats"], # Doesn't work on 2.5
    "healthregen": [33, "Heals the player out of combat every 1 second.", RequestResponse.from_sentence, "gameplay"],
    "fps": [40, "Let's you adjust FPS cap", RequestFloat.from_sentence, "graphics"],
    "fov": [41, "Let's you adjust the FOV", RequestFloat.from_sentence, "graphics"],
    "gamespeed": [42, "Changes the game speed", RequestFloat.from_sentence, "cheats"],
    "shadow": [43, "Adjust shadow quality", RequestInt.from_sentence, "graphics"],
    "resolution": [44, "Adjust the resolution quality", RequestVector3F.from_sentence, "graphics"],
    "freecam": [50, "Toggles Freecam.", RequestResponse.from_sentence, "utility"],
    "hideui": [51, "Toggles UI.", RequestResponse.from_sentence, "graphics"],
    "firstperson": [52, "Toggles First Person.", RequestResponse.from_sentence, "graphics"],
    "idleanimation": [53, "Toggles the last Player Animation from the selfie camera.", RequestResponse.from_sentence, "utility"],
    "savesequence": [60, "Save current sequence, command $NAME.", RequestResponse.from_sentence, "utility"],
    "loadsequence": [61, "Load sequence, command $NAME", 0, "utility"], # a bit more complex.
    "deletesequence": [62, "Removes current sequence in game.", RequestResponse.from_sentence, "utility"],
    "benchmark": [63, "Play Benchmark.", RequestResponse.from_sentence, "graphics"], # temporarily use request string, until we can request different benchmarks (TODO:).
}

clients = []

# just server logic pps.
async def handle_client(reader, writer):

    # this is where we check if we receive a keyframe.
    async def receive_data():
        global SequenceName
        while True:
            try:
                data = await reader.readline()
                msg = data.decode()
                if not msg:
                    logging.warning("Assuming Disconnect.")
                    break
                if (msg.startswith("KEYFRAME")):
                    await SaveSequence(SequenceName, f"{msg}".strip())
                else:
                    logging.info(f"{msg}".strip())
                #print("TEST", msg, flush=True)
            except asyncio.TimeoutError:
                continue
    
    async def process_input(writer):
        global SequenceName, prevcommand

        while True:
            data = await RequestActor.from_sentence(["spawn", "random"], 1)
            writer.write(data)
            await writer.drain()
            await asyncio.sleep(5)
    try:
        await asyncio.gather(receive_data(), process_input(writer))
    except ConnectionResetError:
        writer.close()
        print("LOST CONNECTION.")

async def main():
    server = await asyncio.start_server(handle_client, host, port)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())