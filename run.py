import App 
app = App.app()

if __name__ == '__main__':
    app.run (host='0.0.0.0', threaded=True ,port=8000 , debug =True )