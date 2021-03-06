#!/bin/bash
# sync the application with the remote server

LOCAL_DIR="rf/"
REMOTE_DIR="/var/www/ruggerfest/htdocs/rf/"
#REMOTE_DIR="tmp/rf/"
RSYNC="rsync"
EXCLUDES="*.pyc *.db *_*.db .*"
SERVER="scrapeny.com"
TMPFILE=sync-excludes.$$

for i in $EXCLUDES; do
    echo $i >> $TMPFILE
done

CMD="$RSYNC -avz -e ssh --delete --exclude-from=$TMPFILE $LOCAL_DIR $SERVER:$REMOTE_DIR"
echo "executing $CMD"
$CMD

echo "fixing remote permissions"
ssh $SERVER "(cd $REMOTE_DIR; find . -type f -exec chmod 775 {} \;)"
ssh $SERVER "(cd $REMOTE_DIR; find . -type d -exec chmod 775 {} \;)"

rm $TMPFILE
