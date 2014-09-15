import web

urls = (
    '/', 'Index'
    )

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting = "Hello World"
        message = "Displaying foo"
        # return render.index(greeting = greeting)
        return render.foo(message = message)

if __name__ == "__main__":
    app.run()
