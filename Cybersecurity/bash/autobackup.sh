#!/bin/bash
tar czf backup.tar.gz /etc /var/log
gpg --encrypt --recipient youremail@example.com backup.tar.gz
scp backup.tar.gz.gpg user@remote-server:/path/to/backup
