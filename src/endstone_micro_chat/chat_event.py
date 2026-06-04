from endstone.event import event_handler, PlayerChatEvent
from endstone.plugin import Plugin

from .utils import replace_color_code



class ChatEvent:
    def __init__(self, plugin: Plugin) -> None:
        self._plugin = plugin

    @event_handler
    def on_player_chat(self,event: PlayerChatEvent)-> None:
        event.cancel()
        # local
        msg_player = event.player

        message = event.message
        self._plugin.logger.info(str(message))

        #global
        if message.startswith(self._plugin.config.get("player_global_message_default_prefix"," ")) or self._plugin.config.get("use_local_chat", False)=="false":
            message = message.replace(self._plugin.config.get("player_global_message_default_prefix",""),"",1)

            output = self._plugin.config.get("global_chat_prefix"," ")
            for line in output:
                line = replace_color_code(line.replace("%player%",msg_player.name))
                line = line.replace("%message%",message)
                self._plugin.server.broadcast_message(line)
            #end the function and don`t do many computations
            return


        players = set(self._plugin.server.online_players)
        #self._plugin.logger.info(str(players))
        config_prefix = self._plugin.config.get("local_chat_prefix", " ")
        output = []
        for line in config_prefix:
            line = replace_color_code(line.replace("%player%", msg_player.name))
            line = line.replace("%message%", message)
            output.append(line)


        for player in players:
            if msg_player.location.distance(player.location)<= int(self._plugin.config.get("player_chat_radius")):
                for line in output:
                    player.send_message(line)
