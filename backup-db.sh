#!/bin/bash
# backups the application db

REMOTE_DB="/var/www/ruggerfest/htdocs/rf/ruggerfest_production.db"
SERVER="scrapeny.com"
BACKUP="production.$(date +%Y-%m-%d).db"

echo "BACKUP: $BACKUP"

CMD="scp $SERVER:$REMOTE_DB $BACKUP"
echo "executing $CMD"
$CMD
