# StackAPIでデータ取得
プログラミング言語って何使えばわからない・・・今から勉強するなら何を勉強すればいいの？  
そんな自分のためにプログラミング言語の推移を解析してみる．
  
### 使うもの
* Python3
* パッケージ
    * StackAPI
    * datatime
    * pandas
    * sklearn
    * matplotlib

## StackAPI
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
他にも色々な条件でfetchできる．詳細は参考を参照．
今回は質問についたタグから，どの質問が多くされているのか，その時に共起しているタグは何があるのかを調べる．  

## pandas
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


## sklearn
scikit-learnはデータサイエンス系のツールキットパッケージで，基本的な機械学習の手法を網羅している．さらに発展問題をしたい人は専用のパッケージを入れたり，自作する必要がある．一般的な手法を試すだけならsklearnで十分でだろう．

#### 準備
sklearnとmatplotlibをインストールする．
```bash:
$ pip install sklearn matplotlib
```


# 参考
公式サイト
https://stackapi.readthedocs.io/en/latest/user/install.html
詳細ドキュメント
https://buildmedia.readthedocs.org/media/pdf/stackapi/stable/stackapi.pdf
