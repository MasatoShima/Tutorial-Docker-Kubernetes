#! /bin/bash
# """
# Name: contents_cloner.sh
# Description: sample shell from chapter 7.6
# Created by: Masato Shima
# Created on: 2020/01/03
# """

# 環境変数に CONTENTS_SOURCE_URL がない場合, 処理を終了
if [ -z "$CONTENTS_SOURCE_URL" ]; then
    exit 1
fi

# 初回起動時に git clone を行い, 必要なリソースを取得
git clone "$CONTENTS_SOURCE_URL" /data

# 以後, 定間隔で git pull を行い, contents を最新化する
cd /data/ || exit

while true
do
    date
    sleep 60
    git pull
done

# End
