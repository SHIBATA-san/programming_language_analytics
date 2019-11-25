# StackAPIでデータセット作成
StackAPIを使ってデータを取得，月ごとに集計する予定（だった）．  
急に全部を作るのは難しそうなので，各機能を個別に実装してあとでくっつける．  
* 01_stackapi.py: StackAPIから特定の期間，タグで検索できた結果を取得する
* 02_monthly.py: 期間を指定するためのデータを作る
* 03_pandas.py: pandasで特定の期間内のタグ件数を集計する
* 04_languages.py: 検索したいタグ一覧を作る
あとはくっつけてデータセットを作ることができる．

### 使うもの
* Python3
* パッケージ
    * StackAPI
    * datatime
    * pandas

# StackAPI
プログラマに聞き込みをするのは現実できではないので、プログラマが集うコミュニティからデータを収集する．
今回は海外で最大の質問サイトStackOverflowからデータを持ってくる．  
最近はスクレイピング（scraping，HTML形式で直接ダウンロードする方法）はサーバに余計な負荷をかけるため敬遠されている．ここではAPI（application platform interface）を通してStackOverflowの質問データをダウンロードする．

#### 準備
StackAPIをインストールする．
```bash:
$ pip install stackapi
```

#### 使用例
StackAPI型のオブジェクトにパラメータを設定し，fetchするとJSON形式でデータを返してくれる．
```python:
from stackapi import StackAPI
from datetime import datetime

SITE = StackAPI('stackoverflow')
questions = SITE.fetch('questions', fromdate=datetime(2018,1,1,0,0), todate=datetime(2018,2,1,0,0), min=20, tagged='python', sort='votes')
print(questions)
```
他にも色々な条件でfetchできる．詳細は参考文献を見て欲しい．


# pandas
pandasはPythonでデータセットを扱う際によく使われるパッケージ．
いろんなところでよく使われているので慣れておくと良い．

#### 準備
pandasをインストールする．
```bash:
$ pip install stackapi
```

### 使用例
pandasはSeries型とDataframe型があり、専らDataframe型オブジェクトをdfという名前で作って操作する．
```python:
import pandas as pd

data = [['tag1', 'tag2'],['tag1', 'tag3'],['tag1']]

df = pd.DataFrame()
for tags in data:
    tmp_df = pd.DataFrame([tags], columns=tags)
    #df = pd.merge(df, tmp_df, how='outer', on='python')  # merge: 二つのdfをくっつけるが，初回に共通のカラム（列）がないとエラーになる
    df = df.append(tmp_df, ignore_index=True, sort=False) # 追加という形で対応
#print(df)
df2 = pd.DataFrame(df.count()).T
```
この例では，空っぽのdfを準備，各データについているタグを列の頭（columns）と値に入れている．  
後々，月ごとのデータで集計する予定なので，最後にdf.count()で集計し，転置（行と列の入れ替え）を行なっている．  




# 参考
公式サイト
https://stackapi.readthedocs.io/en/latest/user/install.html
詳細ドキュメント
https://buildmedia.readthedocs.org/media/pdf/stackapi/stable/stackapi.pdf
