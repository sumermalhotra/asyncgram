from src.asyncgram import Asyncgram

client = Asyncgram()

client.start()

for msg in [
    'Hello world',
    'My name is Codeman',
    'My birthday was yesterday',
]:
    client.put(msg)

client.stop()