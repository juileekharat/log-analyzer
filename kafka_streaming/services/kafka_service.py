from kafka import KafkaProducer
from kafka import KafkaConsumer
import json

class KafkaService:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers

    def create_producer(self):
        return KafkaProducer(
            bootstrap_servers = self.bootstrap_servers,
            value_serializer = lambda v: json.dumps(v).encode("utf-8")
        )
    
    def create_consumer(self, topic):
        return KafkaConsumer(
            topic,
            bootstrap_servers = self.bootstrap_servers,
            auto_offset_reset="earliest",
            value_deserializer= lambda m: json.loads(m.decode("utf-8"))
        )