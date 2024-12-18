# from kafka import KafkaConsumer
# import json

# # Initialize Kafka Consumer
# consumer = KafkaConsumer(
#     'test-topic',  # Topic name
#     bootstrap_servers='localhost:9092',  # Kafka broker address
#     value_deserializer=lambda v: json.loads(v.decode('utf-8'))  # Deserialize JSON messages
# )

# print("Listening for messages on Kafka topic 'test-topic'...")

# # Poll messages from Kafka
# try:
#     for message in consumer:
#         print(f"Received: {message.value}")  # Print the message content
# except KeyboardInterrupt:
#     print("Consumer stopped.")
# finally:
#     consumer.close()


#2nd example
from kafka import KafkaConsumer
import json

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'file-topic',  # Kafka topic
    bootstrap_servers='localhost:9092',  # Kafka broker address
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))  # Deserialize JSON messages
)

# Open a file to write consumed messages
with open('output.txt', 'w') as file:
    print("Consuming messages from Kafka topic 'file-topic'...")

    # Poll messages from Kafka
    try:
        for message in consumer:
            print(f"Received: {message.value}")  # Print received message
            file.write(json.dumps(message.value) + "\n")  # Write to file
    except KeyboardInterrupt:
        print("Consumer stopped.")
    finally:
        consumer.close()
        print("Consumer finished.")
