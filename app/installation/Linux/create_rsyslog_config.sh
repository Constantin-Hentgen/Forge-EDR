#!/bin/bash

CONFIG_FILE="/etc/rsyslog.d/forge-xdr.conf"

echo "module(load=\"imudp\") # Chargement du module UDP
input(type=\"imudp\" port=\"5140\")

*.* @127.0.0.1:5140" | sudo tee "$CONFIG_FILE" > /dev/null

if [[ -f "$CONFIG_FILE" ]]; then
    echo "The rsyslog config file has been created successfuly $CONFIG_FILE"
else
    echo "Error : The rsyslog config file has not been created."
    exit 1
fi

# Redémarrer le service rsyslog
sudo systemctl restart rsyslog

# Vérifier si le redémarrage du service a réussi
if [[ $? -eq 0 ]]; then
    echo "The rsyslog service restarted successfuly."
else
    echo "Error : The rsyslog service could not restart."
    exit 1
fi
