void main(){
  print(greet("Dave"));
  print(greet("a"));
  
  print(countdown());
  
  print(canYouVote(17));
  print(canYouVote(18));
  
  waitToVote(14);

  // No discount
  print(ferryDiscount(26, false)); // 10.0
  // Senior discount only
  print(ferryDiscount(65, false)); // 6.67
  // Senior citizen and armed forces discount
  print(ferryDiscount(67, true)); // 6.0
}

String greet(String name) {
  String output = 'Hello $name.';

  // if name's length (number of characters) was more than 10
  if (name.length > 10) {
    output += '\nThat is a long name';
  } else if (name.length <=3 ){
    output += "\nYour full name cannot be less than 3 characters!";
  }
  return output;
}


String countdown() {
  String output = '';
  int count = 10;

  while (count >= 0) {
    output += '$count, ';
    count--;
  }

  output += '... Liftoff! 🚀';
  return output;
}

bool canYouVote(int age){
  if (age>=18){
    return true;
  } else{
    return false;
  }
}

void waitToVote(int age){
  while (!canYouVote(age)){
    print("You are $age, wait till next year...");
    age++;
  }
  print("Now that you are $age, you can vote.");
}

double ferryDiscount(int age, bool armedForces){
  double cost = 10.0;
  if (age <= 14){
    cost = 0.75 * cost;
  } else if (age >= 65 && !armedForces){
    cost = 0.666 * cost;
  } else if (age > 65 && armedForces){
    cost = 0.6 * cost;
  } else if (armedForces){
    cost = 0.8 * cost;
  }

  return cost;
}