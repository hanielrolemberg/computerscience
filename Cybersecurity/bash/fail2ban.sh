#!/bin/bash
tail -f /var/log/auth.log | grep "Failed password" | while read line; do
    ip=$(echo $line | awk '{print $11}')
    iptables -A INPUT -s $ip -j DROP
    echo "Blocked $ip"
done