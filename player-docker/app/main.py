from player import app

if __name__ == '__main__':
    app.run()

def create_app(host='0.0.0.0', port=80):
   return app
