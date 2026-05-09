from kafka_streaming.services.kafka_service import KafkaService
from kafka_streaming.models.log_message import LogMessage

class LogProducer:
    def __init__(self):
        kafka_service = KafkaService(bootstrap_servers="localhost:9092")
        self.producer = kafka_service.create_producer()

    def send_log(self, topic, log_message: LogMessage):
        self.producer.send(topic, value=log_message.__dict__)
        self.producer.flush()
        print(f"Sent: {log_message}")