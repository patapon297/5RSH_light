import web
import threading
from led import light


render = web.template.render('templates/')

urls = (
    '/', 'Index',
)

command = ""

t = threading.Thread(target=light, args=())
t.start()
t.task = "Off"

class Index:

    def GET(self):
        return render.index()

    def POST(self):
        command = web.input().keys()[0]

        print(command)
        t.task = command


    if __name__ == "__main__":
        web.app = web.application(urls, globals())
        web.app.run()
