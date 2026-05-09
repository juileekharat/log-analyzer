from kafka_streaming.consumers.log_consumer import LogConsumer

consumer = LogConsumer(topic="application-logs")
consumer.consume_logs()


