from endstone.plugin import Plugin

from . import login_event
from . import chat_event


class MicroChat(Plugin):

    api_version = "0.11"
    def on_load(self) ->None:
     pass

    def on_enable(self) -> None:
        self.save_default_config()
        self.register_events(login_event.LoginEvent(self))
        self.register_events(chat_event.ChatEvent(self))
        if self.config.get("auto_broadcast","false") == "true":
            self.logger.info("auto broadcast started")
            self.server.scheduler.run_task(self,lambda :chat_event.ChatEvent.schedule_broadcast_message(self),delay=360,period = self.config.get("broadcast_time",)*20)

    #def on_disable(self) -> None:
    #    pass

