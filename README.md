# TOTK-UltraCam-Console
This repo is an API for UltraCam 2.5 and 3.0+. Hugely work in progress currently.

## How to Setup
1. Download TOTK UltraCam Beyond (V 2.5+) or UltraCam Calamity (V 3.0+) or Latest [TOTK Optimizer Version](https://github.com/MaxLastBreath/TOTK-mods).
2. (MANDATORY) On Legacy based Emulators Navigate to **Settings System -> Network -> Network Interface -> Loopback or Ethernet/Wifi.**
3. (MANDATORY) On Ryujinx Navigate to **Settings -> Network -> Network Interface -> Loopback or Ethernet/Wifi.**
4. On Switch
  - Open CMD on Windows and type ipconfig
  - find and copy your **IPv4 IP (192.168.x.x)** - (This is your Router's IP) 
  - Paste the Copied IP Into : **UltraCam/romfs/maxlastbreath.ini** or **!!!TOTKOptimizer/romfs/maxlastbreath.ini** -> **[Console] IP = 127.0.0.1**
5. Run the console, it should open a Command Prompt.
6. Open the game, it should now say **"UltraCam Version X.X Connected!"**
7. You can also **press T** in game to **reconnect** the console if needed or **connect** it in the first place!

## Representing Structures in C++ (B represents byte(s))
| Struct         | Packet        | Value         | Value          | Value          |
| -------------  | ------------- | ------------- | -------------  | -------------  |
| RequestBool    | Int           | Int (4B)      | NULL           | NULL           |
| RequestFloat   | Int           | float (4B)    | NULL           | NULL           |
| RequestInt     | Int           | Int (4B)      | NULL           | NULL           |
| RequestVectorF | Int           | EMPTY (4B)    | Floats (4-12 B)| NULL           |
| RequestVectorI | Int           | EMPTY (4B)    | Ints (4-12 B)  | NULL           |
| RequestSetTime | Int           | EMPTY (4B)    | Int (4B)       | Int (4B)       |
| RequestActor   | Int           | Int (4B)      | STRING (??? B) | EMPTY (4B)     |
| RequestResponse| Int           | NULL          | NULL           | NULL           |

## Table representing command structure.

| Commands      | packet        | struct          | Version         |
| ------------- | ------------- | -------------   | -------------   |
| spawn         | 1             | RequestActor    | UltraCam 2.5+   |
| tp            | 10            | RequestVector3F | UltraCam 2.5+   |
| cords         | 11            | RequestResponse | UltraCam 2.5+   |
| settime       | 20            | RequestSetTime  | UltraCam 2.5+   |
| timespeed     | 21            | RequestFloat    | UltraCam 2.5+   |
| gettime       | 24            | RequestBool     | UltraCam 2.5+   |
| changeweather | 25            | RequestBool     | UltraCam 2.5+   |
| pause         | 23            | RequestBool     | UltraCam 2.5+   |
| godmode       | 10            | RequestBool     | UltraCam 2.5+   |
| kill          | 31            | RequestResponse | UltraCam 2.5+   |
| heal          | 30            | RequestResponse | UltraCam 2.5+   |
| fps           | 40            | RequestFloat    | UltraCam 2.5+   |
| fov           | 41            | RequestFloat    | UltraCam 2.5+   |
| gamespeed     | 42            | RequestFloat    | UltraCam 2.5+   |
| shadow        | 43            | RequestInt      | UltraCam 2.5+   |
| resolution    | 44            | RequestVector3F | UltraCam 2.5+   |
| freecam       | 50            | RequestResponse | UltraCam 2.5+   |
| hideui        | 51            | RequestResponse | UltraCam 2.5+   |
| idleanimation | 53            | RequestResponse | UltraCam 2.5+   |
| savesequence  | 60            | RequestResponse | UltraCam 2.5+   |
| loadsequence  | 61            | NONE (HANDLED)  | UltraCam 2.5+   |
| deletesequence| 62            | RequestResponse | UltraCam 2.5+   |
| benchmark     | 63            | RequestResponse | UltraCam 2.5+   |
| firstperson   | 52            | RequestResponse | UltraCam 3.0+   |
| killall       | 110           | RequestResponse | UltraCam 3.0+   |
| healall       | 111           | RequestResponse | UltraCam 3.0+   |
