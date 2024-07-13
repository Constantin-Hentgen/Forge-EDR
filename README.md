Welcome to Forge-XDR-Agent, an open-source Python project that represents my personal journey in developing an Extended Detection and Response (XDR) system. This project serves as a pedagogical tool, allowing me to explore and apply key concepts in cybersecurity engineering while building a functional XDR solution from scratch.

# Dev
## Build an image

```shell
Forge-XDR-Agent/                                    
docker buildx build -t forge-xdr-agent .
```

# Config
## Linux

```bash

echo "*.* @@127.0.0.1:5140" > /etc/rsyslog.d/forge-xdr
systemctl restart rsyslog

```