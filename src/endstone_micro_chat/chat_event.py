from endstone.event import event_handler, PlayerChatEvent
from endstone.plugin import Plugin



class ChatEvent:
    def __init__(self, plugin: Plugin) -> None:
        self._plugin = plugin

    @event_handler
    def on_player_chat(self,event: PlayerChatEvent)-> None:
        event.cancel()
        message = event.message

        #global
        if message.startswith(self._plugin.config.get("player_global_message_default_prefix"," ")) or self._plugin.config.get("use_local_chat", False)=="false":
            message = message.replace(self._plugin.config.get("player_global_message_default_prefix",""),"")

            self._plugin.server.broadcast_message(self._plugin.config.get("global_chat_prefix"," ")+message)
            #end the function and don`t do many computations
            return

        #local
        msg_player = event.player

        players = set(self._plugin.server.online_players)
        #self._plugin.logger.info(str(players))

        for player in players:
            if msg_player.location.distance(player.location)<= int(self._plugin.config.get("player_chat_radius")):
                player.send_message(self._plugin.config.get("local_chat_prefix"," ")+message)
