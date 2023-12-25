from turtle import *  # タートルグラフィックスの利用
from random import *  # 乱数の利用

t = Turtle() # カメの命名
t.shape('turtle') # カメの形にする
t.shapesize(1.1) # カメの大きさ指定
#t.speed(5) # カメの描画速度の指定
colormode(255) # RGBで色の指定
bgcolor('black') # 背景色の設定

star_n = int(input("いくつのお星様を描きますか?")) # 変数star_n : ターミナル上で入力された数字→描く星の数

for i in range(star_n):
    # 変数star_n : 星の1辺の大きさ:10~50までのランダムな値で指定
    star_size = randint(10, 50)
    # 変数tur_x_pos : カメのx座標:-200~200までのランダムな値で指定
    tur_x_pos = randint(-200, 200)
    # 変数tur_y_pos : カメのy座標を-150~150までのランダムな値で指定
    tur_y_pos = randint(-150, 150)
    red = randint(0, 255) # 変数red : Redの値0～255をランダムの値で指定
    green = randint(0, 255) # 変数green : Greenの値0～255をランダムの値で指定
    blue = randint(0, 255) # 変数blue : Blueの値0～255をランダムの値で指定
    t.pencolor(red, green, blue) # 描画色を上記変数で指定する
    tur_speed = randint(0,10) # 変数tur_speed : 描画速度の値0~10をランダムの値で指定
    t.speed(tur_speed) # 描画速度をtur_speedで指定
    """
    以下for文 : 星1つを描く処理
    """
    for i in range(5):
        
        t.pendown() # ペンを下ろす
        t.forward(star_size)    # star_sizeの値分だけ前へ進む
        t.right(180 - (180 / 5))# 星の外角は以下のrightの引数内の式で求め、右に移動
    t.penup() # ペンを上げる
    t.goto(tur_x_pos, tur_y_pos) # 指定したx座標,y座標にカメを移動させる
done() # 画面を表示し続ける
