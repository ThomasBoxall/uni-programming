import 'dart:math';

import '../week21-23-03-20/lect.dart';

class Point {
  int x;
  int y;

  Point(this.x, this.y);

  void move(int dX, int dY) {
    x = x + dX;
    y = y + dY;
  }

  int getX() => x;

  int getY() => y;

  @override
  String toString() {
    return 'Point{x: $x, y: $y}';
  }
}

class Circle {
  int radius;
  Point centre;

  Circle(this.radius, this.centre);

  Point getCentre() => centre;
  double getArea() => pi * pow(radius, 2);
  double getCircumference() => 2 * pi * radius;

  void scale(int factor){
    radius *= factor;
  }

  @override
  String toString() {
    return 'Circle{radius: $radius, centre: $centre}';
  }
}

class Rectangle {
  int width;
  int height;
  Point centre;

  Rectangle(this.width, this.height, this.centre);

  Point getCentre() => centre;
  int getArea() => width * height;
  int getPerimeter() => 2* width + 2* height;
  void scale(int factor){
    width *= factor;
    height *= factor;
  }

  @override
  String toString() {
    return 'Rectangle{width: $width, height: $height, centre: $centre}';
  }
}

class Question{
  String query;
  String answer;
  
  Question(this.query, this.answer);

  bool guess(String uAnswer){
    return uAnswer == this.answer;
  }

  @override
  String toString(){
    return query;
  }
}

class Exam{
  List<Question> questions;
  int score = 0;

  Exam(this.questions);
  
  int getScore() => score;

  void makeGuesses(List<String> guesses){
    for (int i=0; i< this.questions.length; i++){
      if(this.questions[i].guess(guesses[i])){
        this.score += 1;
      }
    }
  }

  bool checkPass(){
    return (score>40)? true: false;
  }

  @override
  String toString(){
    String retString = "";
    for(int i=0; i< this.questions.length; i++){
      retString = retString + this.questions[i].toString() + "\n";
    }
    return retString;
  }
}
void main(){
  // q1();
  // q2();
  // q3();
  // q4();
  q5();
}

double distanceBetweenTwoPoints(Point p1, Point p2){
  return roundTo2DP(sqrt((pow((p2.getX()-p1.getX()), 2)) + pow((p2.getY()-p1.getY()),2)));
}

void q1(){
  Point point1 = Point(-4, 5);
  Point point2 = Point(3, 2);
  print("The distance between $point1 and $point2 is ${distanceBetweenTwoPoints(point1, point2)}");
}

void q2(){
  Circle c = Circle(10, Point(0, 0));
  Rectangle r = Rectangle(10, 20, Point(0, 0));
  print("For $c, the area is ${c.getArea()} and the circumference is ${c.getCircumference()}");
  print("For $r, the area is ${r.getArea()} and the perimeter is ${r.getPerimeter()}");
}

void q3(){
  Circle c = Circle(10, Point(10, 10));
  Rectangle r = Rectangle(10, 20, Point(10, 10));
  print("Scaling the circle and rectangle by a factor of 2");
  c.scale(2);
  r.scale(2);
  print("They are now $c and $r");
}

void q4(){
  Question ques = Question("Whats 1+1", "2");
  print(ques);
  print(ques.guess("3"));
  print(ques.guess("2"));
}

void q5(){
  List<Question> trivia = [
    Question('How many red squares are there on a standard checkerboard?', '32'),
    Question('What does the Slavic word "vodka" translate to?', 'Little Water'),
  ];
  Exam exm = Exam(trivia);
  print(exm);
  exm.makeGuesses(["32","Little Water"]);
  print("${exm.getScore()}");
  print("${exm.checkPass()}");
}