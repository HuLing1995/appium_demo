#!/bin/bash
devices=`adb devices | grep - | awk '{print $1}'`
for device in $devices; do
  { nohup adb -s $device shell monkey -p com.xueqiu.android -v -s 20 --throttle 300 --pct-touch 30 --pct-nav 40 200 &}
done
