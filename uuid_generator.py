import uuid

uuid_number = input('how many uuids do you need?: ')

for i in range(int(uuid_number)):
    print(str(uuid.uuid4()))
