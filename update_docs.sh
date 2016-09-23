#!/bin/bash

user=$1
if [ x$user = x ]; then
    echo 'Pouzitie: ./update_docs.sh nazov_uzivatela'
    exit 1 
fi


rsync -rlzvD -e "ssh" --rsync-path="sudo rsync" --delete-excluded --delete-after \
	--filter "P web/" \
	--filter "P logs/" \
	--filter "P logs/*" \
	--exclude "update_docs.sh" \
	--exclude 'web/' \
	--exclude '.git' \
	--exclude '.gitignore' \
	./ \
	$user@planck.qnd.sk:/opt/docs


