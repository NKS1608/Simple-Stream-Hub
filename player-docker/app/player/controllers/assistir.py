from player import app, render_template, request
import base58

@app.route('/assistir')
def assistir():
    b58str = request.args.get('id')
    url = base58.b58decode(b58str.encode('utf-8')).decode('utf-8')
    return render_template('assistir.html', link=url, title='Video-On-Demand')

@app.route('/ao-vivo')
def aovivo():
    return render_template('assistir.html', link='livehls/stream', title='Ao Vivo')