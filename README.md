# TOTK-UltraCam-Console
This repo is an API for UltraCam 2.5 and 3.0+. Hugely work in progress currently.



## Table representing command structure.

| Commands      | packet        | struct          |
| ------------- | ------------- | -------------   |
| spawn         | 1             | RequestActor    |
| tp            | 10            | RequestVector3F |
| cords         | 11            | RequestResponse |
| settime       | 20            | RequestSetTime  |
| timespeed     | 21            | RequestFloat    |
| gettime       | 24            | RequestBool     |
| changeweather | 25            | RequestBool     |
| pause         | 23            | RequestBool     |
| godmode       | 10            | RequestBool     |
| kill          | 31            | RequestResponse |
| heal          | 30            | RequestResponse |
| killall       | 110           | RequestResponse |
| healall       | 111           | RequestResponse |
| fps           | 40            | RequestFloat    |
| fov           | 41            | RequestFloat    |
| gamespeed     | 42            | RequestFloat    |
| shadow        | 43            | RequestInt      |
| resolution    | 44            | RequestVector3F |
| freecam       | 50            | RequestResponse |
| hideui        | 51            | RequestResponse |
| firstperson   | 52            | RequestResponse |
| idleanimation | 53            | RequestResponse |
| savesequence  | 60            | RequestResponse |
| loadsequence  | 61            | NONE (HANDLED)  |
| deletesequence| 62            | RequestResponse |
| benchmark     | 63            | RequestResponse |

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