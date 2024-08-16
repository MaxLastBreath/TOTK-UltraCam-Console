from dataclasses import dataclass
import struct

@dataclass
class RequestResponse:
    packet: int

    async def to_bytes(self):
        return struct.pack('<I', self.packet)
    
    @classmethod
    async def request(cls, packet):
        instance = cls(packet=packet)
        return await instance.to_bytes()

    @classmethod
    async def from_sentence(cls, sentence_array, packet):
        instance = cls(packet=packet)
        return await instance.to_bytes()