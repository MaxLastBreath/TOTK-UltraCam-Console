from dataclasses import dataclass
import struct
import random

ActorList = ["Actor_1", "Actor_2"]

@dataclass
class RequestActor:
    packet: int
    amount: int
    actor: str

    async def to_bytes(self):
        return struct.pack('<I', self.packet) + struct.pack('<I', self.amount) + struct.pack(f'!{len(self.actor)}s', self.actor.encode()) + struct.pack('<I', 0)

    @classmethod
    async def from_sentence(cls, sentence_array, packet):

        if sentence_array[1] == "random" or sentence_array[1] == "r":
            instance = cls(packet=packet, amount=1, actor=random.choice(ActorList))
            return await instance.to_bytes()
        elif len(sentence_array) < 2:
            instance = cls(packet=packet, amount=1, actor=sentence_array[1])
            return await instance.to_bytes()
        else:
            instance = cls(packet=packet, amount=int(sentence_array[1]), actor=sentence_array[2])
            return await instance.to_bytes()