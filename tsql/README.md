# SEDEからデータセット作成

Stack Exchange Data Explorer（以下SEDE）にアクセスし，T-SQLでクエリ（query，要求？）を投げる．  
T-SQLはMicrosoftとSybaseが拡張したSQL言語．
***

## 1. T-SQLを投げる画面まで移動
下記URLからSEDEにアクセスする．
https://data.stackexchange.com/

SEDEからアクセスできるコミュニティがいくつか出てくる．  
利用したいStackOverflowは多分ランクの一番上に来ているはず．それをクリック．StackOverflowのAll Queriesという画面になる．

StackOverflowのAll Queriesの画面右上にあるCompose Queriesをクリック．T-SQLを入れる画面が出てくる．

## 2. T-SQLでデータ取得
基本はselectに続いて，どのデータ，どの条件などを指定する．

| 宣言 | 意味 |
| :---: | :---: |
| SELECT select_list | 取得したいデータ |
| FROM table_source | どのテーブルから |
| WHERE search_condition | どんな条件の |
| GROUP BY group_by_expression | どのグループの |
| HAVING search_condition | どの値を持っている |
| ORDER BY order_expression [ ASC | DESC ] | ソート [昇順/降順] |



# 参考
https://data.stackexchange.com/stackoverflow/query/3978/most-popular-stackoverflow-tags-in-may-2010
