from application import something

app = something()
app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True)

