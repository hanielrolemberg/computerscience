#!/bin/bash
if [ "$1" == "" ]
then 
echo "create a script to discover active hosts using ping"
echo "example:$0 10.0.0"
else
for host in {1..254};do
ping -c1 $1.$host | grep "64 bytes" | cut -d " " -f 4 | sed 's/.$//'
done
fi