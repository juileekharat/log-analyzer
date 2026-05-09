from dataclasses import dataclass

@dataclass
class LogMessage:
    timestamp: str
    level: str
    message: str