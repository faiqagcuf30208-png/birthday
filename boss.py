import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

st.set_page_config(page_title="19 November | Happy Birthday Boss", page_icon="👑", layout="wide")
photo_path = Path(__file__).parent / "boss.jpg"
if not photo_path.exists():
    st.error("Keep boss.jpg in the same folder as boss.py.")
    st.stop()

photo = base64.b64encode(photo_path.read_bytes()).decode("utf-8")
photo_url = "data:image/jpeg;base64," + photo

st.markdown("""
<style>
header,footer,#MainMenu,[data-testid="stToolbar"]{visibility:hidden}
[data-testid="stAppViewContainer"],[data-testid="stMain"],.main{background:#070605!important}
.block-container{padding:0!important;max-width:100%!important}
iframe{border:0!important}
</style>
""", unsafe_allow_html=True)

page = r"""
<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;600&family=Playfair+Display:wght@500;600;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box}html,body{margin:0;background:#070605;color:#f8e8c4;font-family:'Playfair Display',Georgia,serif}
#intro{height:100vh;min-height:650px;position:relative;display:flex;align-items:center;justify-content:center;text-align:center;overflow:hidden}
.photo{
    position:absolute;
    inset:0;
    width:100%;
    height:100%;
    object-fit:cover;
    object-position:center 15%;
    filter:brightness(.63);
    animation:zoom 2s;
}
@media(max-width:600px){
    .photo{
        object-fit:contain;
        object-position:center center;
        background:#070605;
    }
}
@keyframes zoom{from{transform:scale(1.08)}to{transform:scale(1)}}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,transparent 20%,rgba(0,0,0,.18) 40%,rgba(0,0,0,.86))}
.hero{position:relative;z-index:2;width:95%;padding:20px 8px}
.date{font-size:clamp(16px,3vw,24px);letter-spacing:7px;color:#ffe4a1;opacity:0;animation:fade 1s 1.2s forwards}
.word{display:block;font-size:clamp(48px,11vw,108px);line-height:1.04;letter-spacing:2px;color:#ffe0a0;text-shadow:0 4px 24px #000,0 0 24px #c28b37;opacity:0;transform:translateY(22px)}
.happy{animation:rise 1s 2.3s forwards}.birthday{animation:rise 1s 3.5s forwards}.boss{animation:rise 1s 4.7s forwards;color:#fff4d8}
.crown{font-size:54px;opacity:0;animation:fade 1s 5.5s forwards}
@keyframes rise{to{opacity:1;transform:translateY(0)}}@keyframes fade{to{opacity:1}}
.goldbtn,button{border:1px solid #f5d58e;border-radius:40px;padding:14px 24px;margin:12px 7px;background:linear-gradient(135deg,#ffe8aa,#bd8426);color:#1b1207;font-weight:bold;letter-spacing:1px;cursor:pointer;box-shadow:0 0 22px #9d6b28}
.goldbtn{opacity:0;animation:fade 1s 6.2s forwards}
.page{display:none;min-height:100vh;padding:38px 14px;align-items:center;justify-content:center;text-align:center;background:radial-gradient(ellipse at top,#392710,#120d08 55%,#050505)}
.page.active{display:flex}.inner{width:min(850px,100%);padding:26px 18px;border:1px solid #b98d46;border-radius:24px;background:rgba(8,7,5,.76);box-shadow:0 0 32px #4b3214}
.kicker{color:#d8b66c;letter-spacing:3px;font-size:12px}h1{font-size:clamp(36px,8vw,68px);color:#f6d894}h2{color:#f4d58e;font-size:clamp(25px,5vw,40px)}
p{font-size:18px;line-height:1.8}.urdu{font-family:'Noto Nastaliq Urdu','Noto Naskh Arabic',serif;direction:rtl;line-height:2.5;font-size:clamp(19px,3.3vw,26px);color:#ffe7b2;margin:20px auto}
.roses{font-size:45px;margin:14px}.cake-scene{width:100%;display:flex;justify-content:center;align-items:center;padding:55px 0 28px}
.cake{position:relative;width:300px;height:245px;margin:0 auto}
.cake-shadow{position:absolute;bottom:4px;left:25px;width:250px;height:24px;border-radius:50%;background:rgba(0,0,0,.55);filter:blur(8px)}
.cake-bottom{position:absolute;bottom:18px;left:35px;width:230px;height:92px;border-radius:15px 15px 28px 28px;background:linear-gradient(90deg,#b87548,#ffe4bd 22%,#f5d6ad 76%,#a95d38);border:3px solid #d9aa5a;box-shadow:inset 0 -12px 0 rgba(122,55,26,.12)}
.cake-bottom:before{content:"";position:absolute;left:-3px;top:-17px;width:230px;height:35px;border-radius:50%;background:#fff0d9;border:3px solid #d9aa5a}
.cake-top{position:absolute;bottom:106px;left:67px;width:166px;height:62px;border-radius:14px 14px 18px 18px;background:linear-gradient(90deg,#b87548,#ffe4bd 25%,#f6d9b3 75%,#a95d38);border:3px solid #d9aa5a}
.cake-top:before{content:"";position:absolute;left:-3px;top:-15px;width:166px;height:30px;border-radius:50%;background:#fff0d9;border:3px solid #d9aa5a}
.cake-drip{position:absolute;z-index:2;top:26px;left:2px;width:222px;height:27px;border-radius:0 0 18px 18px;background:#6c321f;clip-path:polygon(0 0,100% 0,100% 55%,94% 100%,87% 55%,80% 100%,72% 55%,64% 100%,56% 55%,48% 100%,40% 55%,32% 100%,24% 55%,16% 100%,8% 55%,0 100%)}
.cake-plaque{position:absolute;z-index:4;left:50%;top:48px;transform:translateX(-50%);width:145px;padding:8px 3px;border-radius:9px;background:#fff0d9;border:2px solid #d5a04a;color:#5c2c1a;font-size:16px;font-weight:bold;letter-spacing:1px;box-shadow:0 3px 7px rgba(0,0,0,.18)}
.cake-pearl{position:absolute;z-index:4;bottom:23px;left:0;width:100%;text-align:center;color:#f8d88f;letter-spacing:8px;font-size:14px}
.candle{position:absolute;z-index:5;bottom:166px;width:13px;height:53px;border-radius:4px;background:repeating-linear-gradient(135deg,#fff3d1 0 7px,#d6a24d 7px 11px);box-shadow:0 2px 4px #321b0c}
.c1{left:92px}.c2{left:143px}.c3{left:194px}
.flame{position:absolute;top:-24px;left:0;width:14px;height:22px;border-radius:70% 0 70% 70%;transform:rotate(45deg);background:radial-gradient(circle at 65% 65%,#fff7b2 0 18%,#ffb52e 45%,#f36b20 75%);box-shadow:0 0 14px 5px rgba(255,164,38,.55);animation:flicker .45s infinite alternate}
@keyframes flicker{to{transform:rotate(45deg) scale(.78)}}.flame.off{display:none}
@media(max-width:420px){.cake{transform:scale(.9);transform-origin:center center;margin-top:30px;margin-bottom:10px}}
#fireworks{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
@media(max-width:600px){#intro{height:100svh;min-height:630px}.photo{object-position:center 20%}.date{letter-spacing:4px}.word{letter-spacing:0}.page{min-height:100svh;padding:25px 10px}p{font-size:16px}button{width:min(92%,320px);margin:8px auto}.cake{transform:scale(.9)}}

/* MOBILE: Each page fits on one screen */
@media (max-width: 600px) {
    html, body {
        width: 100%;
        height: 100%;
        overflow: hidden !important;
    }

    #intro {
        height: 100svh;
        min-height: 0;
        overflow: hidden;
    }

    .hero {
        width: 100%;
        padding: 12px;
    }

    .date {
        font-size: 16px;
        letter-spacing: 3px;
    }

    .word {
        font-size: clamp(42px, 12vw, 64px);
        line-height: 1.05;
    }

    .crown {
        font-size: 38px;
    }

    .page {
        height: 100svh;
        min-height: 0;
        padding: 10px;
        overflow: hidden;
    }

    .inner {
        width: 100%;
        max-height: calc(100svh - 20px);
        overflow: hidden;
        padding: 14px 10px;
        border-radius: 16px;
    }

    .inner h1 {
        font-size: clamp(27px, 8vw, 38px);
        margin: 10px 0;
    }

    .inner h2 {
        font-size: 24px;
        margin: 8px 0;
    }

    .inner p {
        font-size: 14px;
        line-height: 1.5;
        margin: 10px 0;
    }

    .urdu {
        font-size: 18px;
        line-height: 2.1;
        margin: 8px auto;
    }

    .roses {
        font-size: 30px;
        margin: 5px;
    }

    .cake-scene {
        padding: 12px 0;
    }

    .cake {
        transform: scale(.72);
        transform-origin: center center;
        margin: -25px auto;
    }

    button {
        width: 90%;
        max-width: 300px;
        padding: 11px 12px;
        margin: 6px auto;
        font-size: 12px;
    }

    .kicker {
        font-size: 10px;
        letter-spacing: 2px;
    }
}

</style></head><body>
<section id="intro"><img class="photo" src="__PHOTO__"><div class="shade"></div><div class="hero">
<div class="date">19 NOVEMBER</div><span class="word happy">HAPPY</span><span class="word birthday">BIRTHDAY</span><span class="word boss">BOSS</span><div class="crown">👑</div>
<button class="goldbtn" id="start">OPEN YOUR SPECIAL SURPRISE ✨</button></div></section>

<section class="page" id="poetry"><div class="inner">
<div class="kicker">A DUAA FROM THE HEART</div><div class="roses">🌹 ✨ 🌹</div><h2>HAPPY BIRTHDAY BOSS!</h2>
<div class="urdu">آپ کے نام ہو خوشیوں بھرا ہر ایک دن،<br>روشن رہے کامیابی سے آپ کا ہر اک سفر۔<br>ہر نئی صبح نئی امیدیں ساتھ لے کر آئے،<br>رب کرے آپ کا ہر خواب حقیقت بن جائے۔</div>
<p>May your life always be filled with happiness, respect and success.</p><button data-go="cakepage">A CAKE FOR THE BEST BOSS 🎂</button></div></section>

<section class="page" id="cakepage"><div class="inner">
<div class="kicker">MAKE A WISH</div><h2>For the BEST BOSS</h2>
<div class="cake-scene"><div class="cake">
<div class="cake-shadow"></div><div class="cake-bottom"><div class="cake-drip"></div><div class="cake-plaque">BEST BOSS</div><div class="cake-pearl">✦ • ✦ • ✦ • ✦</div></div>
<div class="cake-top"></div>
<div class="candle c1"><div class="flame"></div></div><div class="candle c2"><div class="flame"></div></div><div class="candle c3"><div class="flame"></div></div>
</div></div>
<p>A little birthday wish, made just for you. Blow out the candles!</p>
<button id="blow">🌬️ BLOW THE CANDLES</button><p id="after" style="display:none;color:#f6d894">May all your good wishes come true! ✨</p><button id="finish" style="display:none">ONE LAST WISH 💌</button></div></section>

<section class="page" id="last"><canvas id="fireworks"></canvas><div class="inner">
<div class="roses">🌹 🌹 🌹</div><div class="kicker">WITH RESPECT AND BEST WISHES</div><h1>HAPPY BIRTHDAY, BOSS!</h1>
<div class="urdu">زندگی کے ہر موڑ پر کامیابی آپ کے قدم چومے،<br>خوشیوں کی روشنی کبھی آپ کے آنگن سے کم نہ ہو۔<br>ہر آنے والا سال پہلے سے بڑھ کر خوبصورت ہو،<br>اور آپ کی محنت کا ہر خواب حقیقت بنے۔</div>
<p>Thank you for your guidance and support. Wishing you a wonderful year ahead!</p><h2>STAY BLESSED • STAY SUCCESSFUL</h2><button id="again">WATCH AGAIN ↻</button></div></section>

<script>
function go(id){document.querySelectorAll('.page').forEach(x=>x.classList.remove('active'));document.getElementById(id).classList.add('active');document.getElementById('intro').style.display='none';window.scrollTo(0,0)}
document.getElementById('start').addEventListener('click',()=>go('poetry'));
document.querySelectorAll('[data-go]').forEach(b=>b.addEventListener('click',()=>go(b.dataset.go)));
document.getElementById('blow').addEventListener('click',()=>{document.querySelectorAll('.flame').forEach(f=>f.classList.add('off'));document.getElementById('blow').style.display='none';document.getElementById('after').style.display='block';document.getElementById('finish').style.display='inline-block'});
let raf=null;
function fireworks(){const c=document.getElementById('fireworks'),x=c.getContext('2d');c.width=innerWidth;c.height=900;let a=[];function burst(){let X=Math.random()*c.width,Y=Math.random()*c.height*.55;for(let i=0;i<32;i++){let t=Math.random()*6.28,v=1+Math.random()*3;a.push({x:X,y:Y,vx:Math.cos(t)*v,vy:Math.sin(t)*v,l:60})}}function draw(){x.clearRect(0,0,c.width,c.height);if(Math.random()<.07)burst();a.forEach(p=>{p.x+=p.vx;p.y+=p.vy;p.vy+=.02;p.l--;x.globalAlpha=Math.max(0,p.l/60);x.fillStyle='#f6d894';x.beginPath();x.arc(p.x,p.y,2.5,0,7);x.fill()});x.globalAlpha=1;a=a.filter(p=>p.l>0);raf=requestAnimationFrame(draw)}draw()}
document.getElementById('finish').addEventListener('click',()=>{go('last');fireworks()});
document.getElementById('again').addEventListener('click',()=>{if(raf)cancelAnimationFrame(raf);document.querySelectorAll('.flame').forEach(f=>f.classList.remove('off'));document.getElementById('blow').style.display='inline-block';document.getElementById('after').style.display='none';document.getElementById('finish').style.display='none';document.getElementById('intro').style.display='flex';document.querySelectorAll('.page').forEach(x=>x.classList.remove('active'));window.scrollTo(0,0)});
</script></body></html>
"""
page = page.replace("__PHOTO__", photo_url)
components.html(page, height=750, scrolling=False)