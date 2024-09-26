#!/bin/bash
echo "qual a sua idade?"
read idade
if ["$idade" -ge "18"]
then 
echo "voce pode dirigir"
else
echo "você nao pode dirigir"
fi
