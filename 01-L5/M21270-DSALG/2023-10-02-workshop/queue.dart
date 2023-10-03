class Queue{
  int head = 0;
  int tail = -1;
  List data = [];
  int MAX_SIZE = 10;

  Queue();

  void enqueue(var newDataToAdd){
    if(tail < MAX_SIZE - 1){
      data.add(newDataToAdd);
      tail++;
      print("enqueue success");
    } else{
      print("queue too big, failed");
    }
    
  }

  void dequeue(){
    if(tail >= 0){
      // theres something in the queue so we can dequeue
      data[head] = null;
      head ++;
      print("dequeue success");
    }else{
      print("nothing in queue so can't dequeue");
    }
  }

  peek(){
    if(tail >= 0){
      print("Item at front: ${data[head]}");
      return data[head];
    }else{
      print("nothing to peek");
    }
  }

  int length(){
    print("Length: ${tail-head + 1}");
    return tail-head+1;
  }

  void displayContents(){
    print(data);
  }
}

class StaticHeadQueue extends Queue{
  StaticHeadQueue();

  void dequeue(){
    if(tail >= 0){
      // theres something in the queue so we can dequeue
      // data[head] = null;
      // head ++;
      
      int temp = head + 1;
      while(temp < tail){
        data[head] = data[temp];
        temp++;
      }
      data.removeAt(tail);
      tail--;
      print("dequeue success");
    }else{
      print("nothing in queue so can't dequeue");
    }
  }
}

class CircularQueue extends Queue{
  CircularQueue();

  void enqueue(var newDataToAdd){
    if(tail < MAX_SIZE - 1 || tail < head){
      // stick it on the tail
      data.add(newDataToAdd);
      tail++;
      print("enqueue success normal");
    } else if(tail == MAX_SIZE - 1 && head > 0){
      // tail can now be 0
      data[0] = newDataToAdd;
      tail = 0;
    } else if(tail == MAX_SIZE && head == 0){
      //full
      print("Full");
    }
  }
}



void main(){
  CircularQueue q = CircularQueue();
  q.enqueue("1");
  q.displayContents();
  q.enqueue("2");
  q.displayContents();
  q.enqueue("3");
  q.displayContents();
  q.enqueue("4");
  q.displayContents();
  q.enqueue("5");
  q.displayContents();
  q.enqueue("6");
  q.displayContents();
  q.enqueue("7");
  q.displayContents();
  q.enqueue("8");
  q.displayContents();
  q.enqueue("9");
  q.displayContents();
  q.enqueue("10");
  q.displayContents();
  q.dequeue();
  print(q.head);
  q.displayContents();
  q.enqueue("11");
  q.displayContents();
  q.enqueue("12");
  q.displayContents();
  q.enqueue("13");
  q.displayContents();

}