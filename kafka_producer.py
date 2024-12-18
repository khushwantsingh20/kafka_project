# from kafka import KafkaProducer
# import json
# import time

# # Initialize Kafka Producer
# producer = KafkaProducer(
#     bootstrap_servers='localhost:9092',  # Kafka broker address
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize messages as JSON
# )

# # List of sample messages
# messages = [
#     {"id": 1, "name": "Alice", "action": "login"},
#     {"id": 2, "name": "Bob", "action": "logout"},
#     {"id": 3, "name": "Charlie", "action": "update"},
#     {"id": 4, "name": "Diana", "action": "login"}
# ]

# # Send messages to Kafka topic
# print("Producing messages to Kafka topic 'test-topic'...")
# for message in messages:
#     producer.send('test-topic', value=message)
#     print(f"Sent: {message}")
#     time.sleep(1)  # Simulate real-time delay

# # Close the producer
# producer.close()
# print("Producer finished.")


#example 2nd
from kafka import KafkaProducer
import json
import time

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize messages as JSON
)

# Simulate different data to send to Kafka topic
data = [
    {"event": "user_login", "user": "Alice", "timestamp": "2024-12-17T12:00:00"},
    {"event": "user_logout", "user": "Bob", "timestamp": "2024-12-17T12:05:00"},
    {"event": "user_update", "user": "Charlie", "timestamp": "2024-12-17T12:10:00"},
    {"event": "user_login", "user": "Diana", "timestamp": "2024-12-17T12:15:00"}
]

# Send messages to Kafka topic
print("Sending messages to Kafka topic 'file-topic'...")
for entry in data:
    producer.send('file-topic', value=entry)
    print(f"Sent: {entry}")
    time.sleep(2)  # Simulate a delay for real-time data production

# Close the producer
producer.close()
print("Producer finished.")
