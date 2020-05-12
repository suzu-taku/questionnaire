# 画像中の重要領域に関するアンケート

English version is [***HERE***](README_English.md)

## 目的

動画像は情報伝達手段として広く用いられていますが，容量が大きいということが問題となっています．

現在主流の符号化手法は一様圧縮ですが，これは高圧縮時に重要領域が欠損する場合があります．

また，画像中の重要領域の品質を維持したまま圧縮することができれば効率が良いと考えられます．

そこで，画像中の重要領域はどこかを定義するために本アンケートを実施します．

## 準備

SSHでは画像が表示されない場合があるので，ローカルでの実行を推奨します．

このプログラムはpython3で動きます．

まず，以下のコマンドでこのリポジトリをダウンロードしてください．

```
$ git clone https://github.com/suzu-taku/questionnaire.git
```

次に，"questionnaire"に移動して以下のコマンドでパッケージ（OpenCV, matplotlib, numpy）をインストールしてください．

（すでに入っている人はインストールする必要はありませんが，matplotlibは3.0.0以上が望ましいです．）

```
$ cd questionnaire
$ pip install -r requirements.txt
```

## 実行

準備ができたら，コマンドライン引数に問題番号を指定して"main.py"を実行してください．

```
$ python main.py 問題番号
```

実行すると，まず以下の画面および文字列が出力されます．

![](demo/demo_image_1.jpg)

```
This is the picture No.001 / 060 with all masks.
Please push the enter button.
```

左がオリジナル画像，右が対象となる全ての領域の輪郭を各色で囲んだ画像です．

この画像は"now_image_1.jpg"として保存されるので，画像が表示されなかった場合はそちらを参照してください．

画像を確認したら，エンターキーを押してください．

次に，以下のような画像および文字列が出力されます．

![](demo/demo_image_2.jpg)

```
------------------------------------------
image   1 /  60,     mask   1 /   3
------------------------------------------
1: The        red mask is very   important
2: The        red mask is        important
3: The        red mask is not so important
4: The        red mask is not    important
------------------------------------------
Your answer >>
```

左がオリジナル画像，右が現在対象となっている領域の輪郭を囲んだ画像です．

この画像は"now_image_2.jpg"として保存されるので，画像が表示されなかった場合はそちらを参照してください．

ここで，

領域が重要であったら 1

領域がどちらかといえば重要であったら 2

領域がどちらかといえば重要でなかったら 3

領域が重要でなかったら 4

を入力してください．

## 中断

アンケートを中断する際にはYour answerに"exit"と入力するかプログラムを終了してください．

```
Your answer >> exit
```

アンケートを再開する際に再び問題番号を指定して"main.py"を実行してください．

すると，中断した画像の最初から再開することができます．

## 提出

アンケートを最後まで実行すると，以下の文字列が出力されプログラムが終了します．

```
You checked all images.
Thank you very much for your cooperation!
```

これが表示されたら，生成された"result_ID.txt"を[***ここ***](https://www.dropbox.com/request/dqUKYzZdGBerNj2a7zgu)に送信してください．
