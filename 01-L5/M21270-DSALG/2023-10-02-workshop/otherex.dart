import 'queue.dart';
import 'stack.dart';

void main(){
  ex3();
}

void ex3(){
  // reverse queue using a stack and put in another queue
  Queue inputQueue = Queue();
  String stringToConvert = "12345";
  for(int i=0; i<stringToConvert.length; i++){
    inputQueue.enqueue(stringToConvert[i]);
  }
  inputQueue.displayContents();
  
  Stack convStack = Stack();
  
  for(int i=0; i<stringToConvert.length; i++){
    convStack.push(inputQueue.peek());
    inputQueue.dequeue();
  }
  convStack.display();
  
  Queue outputQueue = Queue();
  
  while(convStack.top > -1){
    outputQueue.enqueue(convStack.peek());
    convStack.pop();
  }

  outputQueue.displayContents();

}