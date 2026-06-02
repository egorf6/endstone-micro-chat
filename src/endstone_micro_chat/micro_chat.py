from endstone.plugin import Plugin

from . import login_event
from . import chat_event


class MicroChat(Plugin):

    api_version = "0.11"
    def on_load(self):
        pass

    def on_enable(self) -> None:
        self.save_default_config()
        self.register_events(login_event.LoginEvent(self))
        self.register_events(chat_event.ChatEvent(self))

    def on_disable(self) -> None:
        self.logger.info("on_disable is called!")

