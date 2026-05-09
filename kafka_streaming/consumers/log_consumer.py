from kafka_streaming.services.kafka_service import KafkaService

class LogConsumer:
    def __init__(self, topic):
        kafka_service = KafkaService(bootstrap_servers="localhost:9092")
        self.consumer = kafka_service.create_consumer(topic)

    def consume_logs(self):
        print("waiting for logs....\n")
        for message in self.consumer:
            print(f"Received: {message.value}")
