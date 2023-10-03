class Stack{
  List data = [];
  int MAX_SIZE = 10;
  int top = -1;

  Stack();

  void push(var newValueToAdd){
    if(top <= MAX_SIZE - 1){
      data.add(newValueToAdd);
      top++;
      print("success pushing");
    } else{
      print("stack full");
    }
  }

  void pop(){
    if(top >= 0){
      data.removeAt(top);
      top--;
      print("success popping");
    }else{
      print("stack empty");
    }
  }

  peek(){
    print("peek: ${data[top]}");
    return data[top];
  }

  void length(){
    print("length: ${top+1}");
  }

  void display(){
    print(data);
  }
}

void main(){
  Stack s = Stack();

  s.push(1);
  s.push(2);
  s.push(3);
  s.display();

  s.peek();
  s.length();

  s.pop();
  s.display();
  s.pop();
  s.pop();
  s.display();
}