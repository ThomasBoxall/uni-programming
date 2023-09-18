import 'dart:math';

void main(){
  // print(roundTo2DP(44.556));
  double radius = 5;
  print("Radius: ${radius.toInt()}");
  print("Circumference: ${getCircumference(radius)}");
  print("Area: ${getArea(radius)}");
  print("Rounded Area: ${roundTo2DP(getArea(radius))}");
  print("Rounded Circumference: ${roundTo2DP(getCircumference(radius))}");
}

// Tools
double numToDouble(num inputVal){
  return inputVal.toDouble();
}

String intToString(int inputVal){
  return inputVal.toString();
}

String doubleToString(double inputVal){
  return inputVal.toString();
}

double roundTo2DP(double inputVal){
  double roundedVal = inputVal * 100;
  double finishedVal = roundedVal.round().toDouble();
  return finishedVal / 100;
}

// Equations
double getCircumference(double radius){
  return 2 * pi * radius;
}

num squared(num value){
  return value * value;
}

double getArea(num radius){
  return pi * squared(radius);
}