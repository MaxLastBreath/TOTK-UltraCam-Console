# TOTK-UltraCam-Console
This repo is an API for UltraCam 2.5 and 3.0+. Hugely work in progress currently.

# representing Structures in C++ (4-8 B represents byte(s))
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
