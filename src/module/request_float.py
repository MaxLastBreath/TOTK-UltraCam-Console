from dataclasses import dataclass
import struct

@dataclass
class RequestFloat:
    packet: int
    value: float

    async def to_bytes(self):
        return struct.pack('<I', self.packet) + struct.pack('<f', self.value)

    @classmethod
    async def from_sentence(cls, sentence_array, packet):
        value = float(sentence_array[1].lower())
        instance = cls(value=value, packet=packet)
        return await instance.to_bytes()