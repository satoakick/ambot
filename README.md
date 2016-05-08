# ambot

- 前提条件
 - [chainer-char-rnn](https://github.com/yusuketomoto/chainer-char-rnn)で学習データ(vocab.bin, **.chainermodel)を作成済

- ruby(ruboty)の設定  

```
cd ruby
bundle install --path vendor/bundle
bundle exec ruboty -l ambot.rb
```

- python(tornado)の設定
 - [chainer-char-rnn](https://github.com/yusuketomoto/chainer-char-rnn)で作った学習データ(vocab.bin, **.chainermodel)をambot/python/modelsに配置する
 - 以下を実行する
 ```
 cd python
 python app.py
 ```

- その他  
 - ruby/scraping/main_sample.rbは chainer-char-rnnに食わせるデータを作るための[nokogiri](http://www.nokogiri.org/)と[anemone](http://anemone.rubyforge.org/)を使ったサンプルソース
