import 'dart:math';

void main(){
  print(roundToDP(distanceBetweenTwoPoints(1, 2, 4, 6), 2));
}

double roundToDP(double number, int dp){
  number = number * pow(10, dp);
  number = number.roundToDouble();
  number = number / pow(10, dp);
  return number;
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