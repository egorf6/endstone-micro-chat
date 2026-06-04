# Endstone Micro Chat (early beta!)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Endstone](https://img.shields.io/badge/Endstone-Plugin-green.svg)](https://github.com/Endstone/Endstone)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Small Endstone plugin for managing chat in small Bedrock servers

## Features:
- 💬 Local chat 
- 🌍 Global chat
- 👥 Player Join Message
- supporting multiline messages
- autoreplacing '&' char to § , usable for color printing

<img width="609" height="69" alt="joinmsg1" src="https://github.com/user-attachments/assets/4c6156c9-fb06-4be6-a7dc-2aa65dd84193" />
<img width="450" height="69" alt="chats1" src="https://github.com/user-attachments/assets/ce7fc5ff-d739-46c2-89c1-a747f377787a" />


## Items configurable in config.toml:
| key | description | 
|---------|------------------|
| `player_join_message` | configurable multiline join message  |
| `use_local_chat` | if false, using global by default(write "true" or "false") | 
| `global_chat_prefix` | multiline prefix for global message | 
| `local_chat_prefix` | multiline prefix for global message | 
| `player_chat_radius` | radius where players can hear your local message |
| `player_global_message_default_prefix` | char or word in message which can used for writing in global chat (this prefix deletes from message)  |
