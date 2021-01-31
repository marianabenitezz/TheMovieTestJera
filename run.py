from app import manager


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    manager.run()