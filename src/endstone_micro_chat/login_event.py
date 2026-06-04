from endstone.event import event_handler, PlayerJoinEvent
from endstone.plugin import Plugin

from .utils import replace_color_code



class LoginEvent:
    def __init__(self, plugin: Plugin) -> None:
        self._plugin = plugin


    @event_handler
    def on_player_join(self,event: PlayerJoinEvent)-> None:

        message = self._plugin.config.get("player_join_message","")
        for line in message:
            self._plugin.server.broadcast_message(replace_color_code(line).replace("%player%", event.player.name))

