void main(){
  print(personalGreeting("Thomas"));
  print(formalName("Thomas", "Boxall"));
  print(gradeTest(5));
  print(nameToNumber("Sam"));
}

String personalGreeting(String name){
  return "Hey $name 👋";
}

String formalName(String firstName, String familyName){
  return "${firstName[0]}. $familyName";
}

String gradeTest(int mark){
  String grades = "FFFFCCBBAAA";
  return "${grades[mark]}";
}

int nameToNumber(String name){
  int numberTotal = 0;
  name = name.toLowerCase();
  for(int i=0; i < name.length; i++){
    numberTotal += name.codeUnitAt(i) - 96;
  }
  return numberTotal;
}