from dataclasses import dataclass, field
from typing import Optional
import struct

time_dict = {
    "day" : [12, 0],
    "dawn" : [8, 0],
    "night" : [24, 0],
    "dusk" : [20, 0],
}

@dataclass
class RequestSetTime:

    packet: int = 20
    empty: int = 0
    hour: int = field(default=None)
    minutes: int = field(default=None)

    def __post_init__(self):
        if self.hour is None or self.minutes is None:
            raise ValueError("hour and minutes must be provided")

    async def to_bytes(self):
        return (struct.pack('<I', self.packet) + 
                struct.pack('<I', self.empty) + 
                struct.pack('<I', self.hour) + 
                struct.pack('<I', self.minutes))

    @classmethod
    async def toClass(cls, hour, minutes):
        return cls(hour=hour, minutes=minutes)
    
    # we use the sentence array as an agruement here, you can pass anything into the ToClass(hour, minutes)
    @classmethod
    async def settime(cls, sentence_array = list):
        time = [0, 0]
        
        if sentence_array[1].lower() in time_dict:
            time = time_dict[sentence_array[1].lower()]
        else: 
            clock_time = sentence_array[1].split(":")
            if len(clock_time) == 1:
                clock_time.append(0)
            time = [clock_time[0], clock_time[1]]
        
        instance = await RequestSetTime.toClass(cls, time[0], time[1])
        print(f"Setting time to {time[0]}:{time[1]}")    
        return await instance.to_bytes()