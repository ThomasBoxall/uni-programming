void main(){
  print(sayHello());
}

String sayHello({String name= "NAME"}){
  String retString = "Hello $name";
  return retString;
}