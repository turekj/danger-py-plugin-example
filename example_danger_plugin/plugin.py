from danger_python.plugins import DangerPlugin


class ExampleDangerPlugin(DangerPlugin):
    def hello(self):
        self.message("Hello world!")
