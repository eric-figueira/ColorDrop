# ColorDrop

## What is it
ColorDrop is a multiplayer game made in python (pygame), it consists in a game with minimum of 2 players and maximum of 8 in which they are in a board where many squares appear and disappear, if you step in the right color, you live, otherwise, you fall into the void!
 
![image](https://user-images.githubusercontent.com/113946578/216772227-7fd4f18d-959e-4671-9edc-82119a74e1db.png)

---

## Learning
The game was developed using knowledges aquired during the second semester of an IT course on COTUCA. The game has:
- Multiple matches -- There is no problem if the maximum amount of players was reached, the server will create a new match in which new players can join
- Syncronized movement and actions between players in the same match
- Use of sockets and object oriented programming
- Threads and timers

## How to play it
In order to play the game, the server must be running. Firstly, go to the file named "config.txt" and change the "server-ip" to the server's ip
Furthermore, you must have pygame installed, to do so, you can use:
```
pip install pygame
```
The controllers are pretty simple, you can move your player (in gold) by using the arrow keys in your keyboard

![image](https://user-images.githubusercontent.com/113946578/216772811-b8376294-3f32-4013-8d89-86ffe38c37cf.png)
![image](https://user-images.githubusercontent.com/113946578/216772826-b72942e7-41e8-4949-a00c-834136a47a04.png)

