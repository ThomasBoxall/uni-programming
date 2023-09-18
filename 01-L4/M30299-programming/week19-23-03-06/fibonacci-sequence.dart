import 'dart:io';

void main(){

    print("Enter the number of fibonacci numbers to generate");
    int? fibCount = int.parse(stdin.readLineSync()!);

    var fib = <int>[0];
    for(var i =0; i < fibCount-1; i++){
        int nextVal;
        if (fib.length == 1){
            nextVal = fib[i]+1;
        }else{
            nextVal = fib[i] + fib[i-1];
        }
        fib.add(nextVal);
        // print(nextVal);
    }   
    print(fib);
    print(fib.length);
}