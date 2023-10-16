void main(){

  List<int> fib = [1,1];
  print("==RECURSION==");
  recursion(fib, 13);
  print("Dalin's example: ${dalinRecursiveExample(7)}");
  print("==ITERATIVE==");
  iterative(fib, 13);
}

void recursion(List<int> fib, int fibToGetTo){
  
  int currentMaxFibIndex = fib.length - 1;

  if(fib[currentMaxFibIndex] == fibToGetTo){
    print("Number $fibToGetTo in ${fib} at position ${currentMaxFibIndex+1}");
  }else if(fib[currentMaxFibIndex] > fibToGetTo){
    print("Number $fibToGetTo NOT FOUND in $fib. Got to position ${currentMaxFibIndex+1}");
  } else{
    int nextFibbo = fib[currentMaxFibIndex] + fib[currentMaxFibIndex - 1];
    fib.add(nextFibbo);
    recursion(fib, fibToGetTo);
  }
}

int dalinRecursiveExample(int n){
  if (n == 1 || n == 2){ return 1; }
  else{ return dalinRecursiveExample(n-1) + dalinRecursiveExample(n-2); }
}

void iterative(List<int> fib, int fibToGetTo){
  int currentMaxFibIndex = fib.length - 1;
  while(fib[currentMaxFibIndex] <= fibToGetTo){
    int nextFibbo = fib[currentMaxFibIndex] + fib[currentMaxFibIndex - 1];
    fib.add(nextFibbo);
    currentMaxFibIndex = fib.length - 1;
  }
  currentMaxFibIndex--;
  if(fib[currentMaxFibIndex] == fibToGetTo){
    print("Number $fibToGetTo in ${fib} at position ${currentMaxFibIndex+1}");
  }else if(fib[currentMaxFibIndex] > fibToGetTo){
    print("Number $fibToGetTo NOT FOUND in $fib. Got to position ${currentMaxFibIndex+1}");
  }
}