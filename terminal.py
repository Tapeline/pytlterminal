class Terminal:
    command_handlers = {}

    def __init__(self, prefix):
        self.prefix = prefix
        self.running = True

    def cmd(self, command):
        def decorator_use_unit(func):
            self.command_handlers[command] = func

            def wrapper_use_unit(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper_use_unit

        return decorator_use_unit

    def run(self):
        while self.running:
            command = input(f"{self.prefix}>")
            without_args = command.split()[0]
            if without_args in self.command_handlers.keys():
                self.command_handlers[command](command)
            else:
                self.err(f"[{self.prefix}] {without_args} is not defined!")

    def info(self, msg):
        print(f"(i) {msg}")

    def warn(self, msg):
        print(f"(!) {msg}")

    def err(self, msg):
        print(f"(X) {msg}")

    def out(self, msg):
        print(f"{msg}")
