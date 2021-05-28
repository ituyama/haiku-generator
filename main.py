
import MeCab
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, request, redirect, url_for, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show_img', methods=['GET', 'POST'])
def show_img():



    upper = request.form.get('upper')
    middle = request.form.get('middle')
    under = request.form.get('under')
    name = request.form.get('name')
    kami =list(upper)
    naka =list(middle)
    simo =list(under)
    name =list(name)
    haik = Image.open("static/img/backs.png")
    kami = '\n'.join(kami)
    naka = '\n'.join(naka)
    simo = '\n'.join(simo)
    name= '\n'.join(name)
    draw = ImageDraw.Draw(haik)
    font = ImageFont.truetype('font/kana.ttf', 80)
    fontname = ImageFont.truetype('font/kana.ttf', 50)
 
   
 



    draw.multiline_text((400, 50), kami, fill=(0, 0, 0), font=font ) 
    draw.multiline_text((270, 120), naka, fill=(0, 0, 0), font=font ) 
    draw.multiline_text((170, 430), simo, fill=(0, 0, 0), font=font ) 
    draw.multiline_text((60, 530), name, fill=(0, 0, 0), font=fontname ) 
    
    a ="static/img/"
    b =".png"
    c =[a,upper,middle,under,b]
    c = ''.join(c)
    haik.save(c)
    return render_template("index.html", img_url=c , )

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
