import asyncio
import socket
import struct

host = '127.0.0.1'
port = 5555

async def receive_data(reader, writer):
    try:
        while True:
            # Receive the amount (integer)
            amount_data = await reader.read(4)
            amount = struct.unpack('!I', amount_data)[0]
            print(f"Received amount: {amount}")

            # Receive the string
            string_length_data = await reader.read(4)
            string_length = struct.unpack('!I', string_length_data)[0]

            string_data = await reader.read(string_length)
            received_string = string_data.decode('utf-8')
            print(f"Received string: {received_string}")

    except Exception as e:
        print(f"Error: {e}")

async def connect_and_receive():
    while True:
        try:
            reader, writer = await asyncio.open_connection(host, port)
            print(f"Connected to {host}:{port}")

            await receive_data(reader, writer)

        except ConnectionRefusedError:
            print("Connection refused. Retrying...")
            await asyncio.sleep(5)  # Wait for 5 seconds before retrying
        except Exception as e:
            print(f"Error: {e}")
            await asyncio.sleep(5)  # Wait for 5 seconds before retrying

async def main():
    await connect_and_receive()

if __name__ == "__main__":
    asyncio.run(main())
