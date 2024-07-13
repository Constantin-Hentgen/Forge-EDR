import logging

from core.utils import timer
from collectors.syslog_collector import SyslogCollector

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    collector = SyslogCollector()
    try:
        collector.start()
    except KeyboardInterrupt:
        collector.stop()
