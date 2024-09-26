#!/bin/bash
ip="$1"
for port in {1..65535}; do
    nc -zv $ip $port 2>&1 | grep succeeded &
done
