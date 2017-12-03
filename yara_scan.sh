#!/bin/bash
#Bash script to do a crontab, make sure you have the correct rights
#Script en bash pour faire une tâche cron, assurez vous d'avoir les droits nécessaires.
echo "Started scan at" `date` >> yara_scan.log
python ./yarascan.py >> yara_scan.log
