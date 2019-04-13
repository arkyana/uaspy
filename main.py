from core.baseapp import BaseApp


class App(BaseApp):
    def __init__(self) :
        BaseApp.__init__(self)

    def on_playing(self):
        self.check_collision(self.player, self.enemies)

if __name__ == "__main__":
    theApp = App()
    theApp.run()