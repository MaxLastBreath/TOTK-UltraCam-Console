import json
import os
import struct
import asyncio

keyframes_file = "keyframes.json"

if os.path.exists(keyframes_file):

    with open(keyframes_file, 'r') as file:
        json_data = json.load(file)

else:
    print("No keyframes.json")

async def LoadSequence(writer, name):
    with open(keyframes_file, 'r') as file:
        json_data = json.load(file)

    sequence = json_data[name]
    index = 0
    for keyFrame in sequence:
        data = (
            struct.pack('<I', 61) +  
            struct.pack('<I', index) +
            struct.pack('<f', float(sequence[keyFrame]["Pos:"][0])) + 
            struct.pack('<f', float(sequence[keyFrame]["Pos:"][1])) + 
            struct.pack('<f', float(sequence[keyFrame]["Pos:"][2])) + 
            struct.pack('<f', float(sequence[keyFrame]["Forward:"][0])) + 
            struct.pack('<f', float(sequence[keyFrame]["Forward:"][1])) + 
            struct.pack('<f', float(sequence[keyFrame]["Forward:"][2])) + 
            struct.pack('<f', float(sequence[keyFrame]["Up:"][0])) + 
            struct.pack('<f', float(sequence[keyFrame]["Up:"][1])) + 
            struct.pack('<f', float(sequence[keyFrame]["Up:"][2])) + 
            struct.pack('<f', float(sequence[keyFrame]["Fov:"])) + 
            struct.pack('<f', float(sequence[keyFrame]["Duration"])) 
            # struct.pack('<f', float(sequence[keyFrame]["Lerp"])) # currently unused.
        )
        index += 1
        writer.write(data)
        await writer.drain()
        await asyncio.sleep(0.1)

async def SaveSequence(name, text):
    with open(keyframes_file, 'r') as file:
        json_data = json.load(file)
    
    if name not in json_data:
        json_data[name] = {}
    
    array = text.split(" ")
    
    keyframe =  {
            array[2] : [array[3], array[4], array[5]],
            array[6] : [array[7], array[8], array[9]],
            array[10] : [array[11], array[12], array[13]],
            array[14] : array[15],
            array[16] : array[17],
            array[18] : array[19]
        }

    json_data[name][array[1]] = keyframe
    print(keyframe)

    with open(keyframes_file, 'w') as file:
        json.dump(json_data, file, indent=4)