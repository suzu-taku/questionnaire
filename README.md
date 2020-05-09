# 画像中の重要領域に関するアンケート

## 準備

このプログラムはpython3で動きます．

まず，以下のコマンドでこのリポジトリをダウンロードしてください．

```
$ git clone https://github.com/suzu-taku/questionnaire.git
```

次に，"questionnaire"に移動して以下のコマンドでパッケージ（OpenCV, matplotlib）をインストールしてください．

```
$ cd questionnaire

$ pip install -r requirements.txt
```

## 実行

準備ができたら，"main.py"を実行してください．

```
$ python main.py
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
2: The        red mask is rather important
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

アンケートを再開する際に再び"main.py"を実行してください．

すると，中断した画像の最初から再開することができます．

## 提出

アンケートを最後まで実行すると，以下の文字列が出力されプログラムが終了します．

```
You answered all images.

Thank you very much for your cooperation!
```

これが表示されたら，生成された"result.txt"を[ここ](https://www.dropbox.com/request/dqUKYzZdGBerNj2a7zgu)に送信してください．
