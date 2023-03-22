import 'dart:math';

void main(){
  print(distanceBetweenTwoPoints(1, 2, 4, 6));
}

double circumferenceOfCircle(double radius){
  return 2 * pi * radius;
}

double areaOfCircle(double radius){
  return pi * pow(radius, 2);
}

double gradient(double x1, double y1, double x2, double y2){
  return (y2 -  y1) / (x2 - x1);
}

double distanceBetweenTwoPoints(double x1, double y1, double x2, double y2){
  return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}