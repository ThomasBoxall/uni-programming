void main(){
  // print(multipleThreeFive(1000));
  // print(evenFib(4000000));
  print(largestPrimeFactor(13195));
}

int multipleThreeFive(int maxNumb){
  int sum = 0;

  for (int i = 0; i < maxNumb; i++){
    if (isMult(3, i) || isMult(5, i)){
      sum += i;
    }
  }
  return sum;
}

bool isMult(int factor, int val){
  if (val % factor == 0){
    return true;
  } else{
    return false;
  }
}


int evenFib(int maxNumb){
  int sum = 0;
  int current = 1;
  int prev = 1;
  while (current < maxNumb){
    int temp = prev;
    prev = current;
    current = prev + temp;
    if(current % 2 == 0){
      sum += current;
    }
  }
  return sum;
}

int largestPrimeFactor(int target){
  int currentLPF = 1;
  for (int i = 0; i < target; i++){
    if (isMult(target, i)){
      print(i);
      currentLPF = i;
    }
  }
  return currentLPF;
}

bool isPrime(int value){
  for (int x = 0; x < value; x++){
    if (x % 2 == 0){
      return false;
    }
  }
  return true;
}