#!/usr/bin/expect -f
spawn ssh yiprogra@yi-programmer.com
set timeout 60
expect "yiprogra@yi-programmer.com *"
send "/home2/yiprogra/articles/crontab_run.sh\r"
set timeout 120
expect "yiprogra@yi-programmer.com *"
send "exit\r"
expect eof
