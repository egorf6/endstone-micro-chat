# Endstone Micro Chat (early beta!)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Endstone](https://img.shields.io/badge/Endstone-Plugin-green.svg)](https://github.com/Endstone/Endstone)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Small Endstone plugin for managing chat in small Bedrock servers

## Features:
- 💬 Local chat   <img width="755" height="65" alt="image" src="https://github.com/user-attachments/assets/dd4a72e6-0743-4f4c-9568-63e9c8c31514" />
- 🌍 Global chat   <img width="760" height="66" alt="image" src="https://github.com/user-attachments/assets/01a63505-0a79-4ee7-86a6-d00168815c45" />
- 👥 Player Join Message   <img width="609" height="69" alt="joinmsg1" src="https://github.com/user-attachments/assets/4c6156c9-fb06-4be6-a7dc-2aa65dd84193" />
- Autobroadcasting with miltiline configuration <img width="344" height="33" alt="image" src="https://github.com/user-attachments/assets/4794f746-e933-40a4-ac96-c45ef8da8a58" />

- Supporting multiline messages
- Autoreplacing '&' char to § , usable for color printing






## Items configurable in config.toml:
| key | description | 
|---------|------------------|
| `player_join_message` | configurable multiline join message  |
| `use_local_chat` | if false, using global by default(write "true" or "false") | 
| `global_chat_prefix` | multiline prefix for global message | 
| `local_chat_prefix` | multiline prefix for global message | 
| `player_chat_radius` | radius where players can hear your local message |
| `player_global_message_default_prefix` | char or word in message which can used for writing in global chat (this prefix deletes from message)  |
| `auto_broadcast` | disabling or enabling broadcast scheduler(write "true" or "false") | 
| `broadcast_time` | delay for broadcasting loop (time in seconds) | 
| `broadcast_message` | multiline message of broadcast | 
