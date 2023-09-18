import 'dart:ffi';
import 'dart:math';

void main(){
  print(bondGreeting("James", "Bond"));
  print(sing(4));
  print(circumferenceOfCircle(4));
  print(areaOfCircle(3));
  print(distanceBetweenTwoPoints(1, 2, 4, 6));
  singASong(2, sing, 4);

  List<Function> emailValidationFunctions = [emailStartUP, emailContainsAt, emailContainsDomain];
  print(isValidUPEmail("up2108121@myport.ac.uk", emailValidationFunctions));
}

String bondGreeting(String first, String last){
  return "My name is $last, $first $last!";
}

String sing(int numb) => "dum " * numb;

double circumferenceOfCircle(double radius) => 2 * pi * radius;

double areaOfCircle(double radius) => pi * (pow(radius, 2));

double distanceBetweenTwoPoints(double x1, double y1, double x2, double y2) => sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

void singASong(int lines, String Function(int) printALine, int repeatPerLine){
  for(int i=0; i<lines; i++){
    print(printALine(repeatPerLine));
  }
}

bool emailStartUP(String email) => email.startsWith("up");
bool emailContainsAt(String email) => email.contains("@");
bool emailContainsDomain(String email) => email.contains("myport.ac.uk");

bool isValidUPEmail(String email, List<Function> validationFunctions){
  for (int i=0; i<validationFunctions.length; i++){
    if (validationFunctions[i](email) == false){
      print(i);
      return false;
    }
  }
  return true;
}