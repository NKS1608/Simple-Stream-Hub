from player import app, render_template


@app.route('/dash/<id>')
def dash(id):
    url_dash = 'video/dash/'+id+'/stream.mpd'
    return render_template('player.html', video_url=url_dash,mime='application/dash+xml')

@app.route('/hls/<id>')
def hls(id):
    url_hls = 'video/hls/'+id+'/master.m3u8'
    return render_template('player.html', video_url=url_hls,mime='application/x-mpegURL')

@app.route('/livedash/<id>')
def livedash(id):
    url_livedash = 'video/livedash/'+id+'.mpd'
    return render_template('player.html', video_url=url_livedash,mime='application/dash+xml')

@app.route('/livehls/<id>')
def livehls(id):
    url_livehls = 'video/livehls/'+id+'.m3u8'
    return render_template('player.html', video_url=url_livehls,mime='application/x-mpegURL')

@app.route('/mp4/<id>')
def mp4(id):
    return render_template('mp4.html', name=id)
