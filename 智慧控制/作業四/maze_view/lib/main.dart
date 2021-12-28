import 'dart:math';

import 'package:flutter/material.dart';

void main(List<String> args) {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'walk the maze',
      home: Maze(),
    );
  }
}

class Maze extends StatefulWidget {
  Maze({Key? key}) : super(key: key);

  @override
  _MazeState createState() => _MazeState();
}

class _MazeState extends State<Maze> {
  List<List<int>> maze = [
    [-1, -1, -1, -1, -1, -1],
    [-1, 0, 0, 100, 0, -1],
    [-1, -1, 0, -1, 0, -1],
    [-1, 0, 0, 0, 0, -1],
    [-1, 0, -1, -1, 0, -1],
    [-1, 0, -1, 0, 0, -1],
    [-1, 0, -1, 0, -1, -1],
    [-1, 0, 0, 0, 0, -1],
    [-1, -1, -1, -1, -1, -1],
  ];
  @override
  Widget build(BuildContext context) {
    double _w = MediaQuery.of(context).size.width;
    double _h = MediaQuery.of(context).size.height;
    return Scaffold(
      body: Container(
          alignment: Alignment.center,
          child: Container(
            width: _h / 9 * 6,
            child: Stack(
              children: [
                GridView.count(
                  crossAxisSpacing: 2,
                  mainAxisSpacing: 2,
                  crossAxisCount: 6,
                  children: List.generate(54, (index) {
                    int box = maze[index ~/ 6][index % 6];
                    return Container(
                      color: box == -1
                          ? Colors.black87
                          : box == 100
                              ? Colors.green[400]
                              : Colors.grey[350],
                    );
                  }),
                ),
                Positioned(
                  top: _h / 9 * 2 + _h / 36,
                  left: _h / 9 * 2 + _h / 36,
                  child: Container(
                    width: _h / 18,
                    height: _h / 18,
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(10),
                    ),
                  ),
                ),
              ],
            ),
          )),
    );
  }

  walk() {
    List<List<List<double>>> Q = List.filled(9, List.filled(6, List.filled(4, 0.0)));
    int epoc = 5; //回合數
    int step = 1000; //步數
    double beta = 0.9; //學習率
    double gamma = 0.9; //獎勵因子
    List start=[7,1];
    for(int round=0;round<epoc;round++){
      for(int i=0;i<step;i++){
        int x=start[0];
        int y=start[1];
        int action=0;
        while(maze[x][y]!=0){
          action=Q[x][y].indexOf(getMaxNum(Q[x][y]));
          if(action==0){
            x=x-1;
          }else if(action==1){
            y=y-1;
          }else if(action==2){
            x=x+1;
          }else if(action==3){
            y=y+1;
          }
        }
        Q[x][y][action]=Q[x][y][action]+beta*(gamma*maze[x][y]-Q[x][y][action]);
      }
    }
  }
double  getMaxNum(numList<List<double>>){
    double max=0;
    for(double num in numList){
      if(num>max){
        max=num;
      }
    }
    return max;
  }
}
