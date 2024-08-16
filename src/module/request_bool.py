from dataclasses import dataclass
import struct

bool_dict = {
    "true": 1,
    "on": 1,
    "false": 0,
    "off": 0
}

@dataclass
class RequestBool:
    packet: int
    value: bool

    async def to_bytes(self):
        return struct.pack('<I', self.packet) + struct.pack('<f', self.value)

    @classmethod
    async def from_sentence(cls, sentence_array, packet):
        is_Enabled = 2
        if len(sentence_array) < 2:
            return struct.pack('<I', packet) + struct.pack('<I', is_Enabled)
        
        value = sentence_array[1].lower()
        if value.lower() in bool_dict:
            is_Enabled = bool_dict[value]    

        instance = cls(value=is_Enabled, packet=packet)
        return await instance.to_bytes()