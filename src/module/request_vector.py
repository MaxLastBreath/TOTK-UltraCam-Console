from dataclasses import dataclass
import struct

@dataclass
class RequestVector3F:
    packet: int
    vec: list

    async def to_bytes(self): # byte 4-8 needs to be 0 or smth else..
        data = (struct.pack('<i', self.packet) + struct.pack('<i', 0))

        for value in self.vec:
            data += struct.pack('<f', float(value))
        
        return data

    @classmethod
    async def from_sentence(cls, sentence_array, packet):
        sentence_array.pop(0)
        vector = []

        for args in sentence_array:
            vector.append(float(args))

        instance = cls(packet=packet, vec=vector)
        return await instance.to_bytes()
    
    @classmethod
    async def VEC3(cls, x, y, z, packet):
        vector = [x, y, z]

        instance = cls(packet=packet, vec=vector)
        return await instance.to_bytes()

    
@dataclass
class RequestVector3I:
    packet: int
    vec: list

    async def to_bytes(self): # byte 4-8 needs to be 0 or smth else..
        data = (struct.pack('<i', self.packet) + struct.pack('<i', 0))

        for value in self.vec:
            data += struct.pack('<i', int(value))
        
        return data

    @classmethod
    async def from_sentence(cls, sentence_array, packet):
        sentence_array.remove(0)
        vector = []
        for args in sentence_array:
            vector.append(int(args))

        instance = cls(packet=packet, vec=vector)
        return await instance.to_bytes()
    
    @classmethod
    async def VEC3(cls, x, y, z, packet):
        vector = [x, y, z]

        instance = cls(packet=packet, vec=vector)
        return await instance.to_bytes()

