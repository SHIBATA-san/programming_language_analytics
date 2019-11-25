from stackapi import StackAPI
from datetime import datetime

SITE = StackAPI('stackoverflow')

SITE.page_size = 10
SITE.max_pages = 10

# コメント検索
# comments = SITE.fetch('comments')

# 質問検索
questions = SITE.fetch('questions', fromdate=datetime(2018,1,1,0,0), todate=datetime(2018,2,1,0,0), min=20, tagged='python', sort='votes')


for date in questions['items']:
    print(date[u'tags'])