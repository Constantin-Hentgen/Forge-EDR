import socket
import logging


class SyslogCollector:
    def __init__(self, host="0.0.0.0", port=5140):
        self.host = host
        self.port = port
        self.sock = None
        self.logger = logging.getLogger("SyslogCollector")

    def start(self):
        self.logger.info("Starting Syslog Collector on %s:%d", self.host, self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        self.logger.info("Syslog Collector started and listening")

        while True:
            data, addr = self.sock.recvfrom(1024)
            self.logger.info("Received message from %s: %s", addr, data)
            self.process_message(data.decode("utf-8"))

    def process_message(self, message):
        self.logger.info("Processing message: %s", message)
        # Ajoutez ici la logique de traitement du message
        # Par exemple, vous pouvez enregistrer les messages dans une base de données
        # ou les transmettre à un autre service pour une analyse plus approfondie

        with open("app/logs/syslog_collector.log", "a") as log_file:
            log_file.write(f"{message}\n")
        pass

    def stop(self):
        self.logger.info("Stopping Syslog Collector")
        if self.sock:
            self.sock.close()
            self.sock = None
        self.logger.info("Syslog Collector stopped")
