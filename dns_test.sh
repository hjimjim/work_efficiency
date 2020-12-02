#!/bin/bash
echo "data now : $(date +%Y%m%d) "
echo "data now : $(date +%Y)년   $(date +%m)월 $(date +%d)일 " 
echo "$(date +%H) 시  $(date +%M) 분  $(date +%S) 초 입니다."

while true
do
	echo "$(date) |  $(nslookup www.google.com)" >> result_$(date +%Y%m%d).txt
	sleep 10
done
