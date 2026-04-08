from dataclasses import dataclass
import struct
import random

@dataclass
class RequestJson:
    packet: int
    size: int
    json: str

    async def to_bytes(self):
        return struct.pack('<I', self.packet) + struct.pack('<I', self.size) + struct.pack(f'!{len(self.json)}s', self.json.encode()) + struct.pack('<I', 0)

    @classmethod
    async def from_sentence(cls, sentence_array, packet):
        full_string = " ".join(sentence_array[1:])

        instance = cls(packet=packet, size=len(sentence_array[1]), json=full_string)
        return await instance.to_bytes()