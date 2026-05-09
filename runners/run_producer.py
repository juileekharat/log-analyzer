from kafka_streaming.producers.log_producer import LogProducer
from kafka_streaming.models.log_message import LogMessage

producer = LogProducer()

log = LogMessage(
    timestamp="2026-05-09 10:00:00",
    level="ERROR",
    message="Database timeout"
)

producer.send_log(
    topic = "application-logs",
    log_message=log
)