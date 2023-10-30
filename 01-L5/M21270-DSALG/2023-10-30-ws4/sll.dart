// class Node{
//   int data;
//   Node next;

//   Node(){
//     data = 0;
//     next = null;
//   }

//   Node(int data){
//     data = data;
//   }
// }

// class SinglyLinkedList{
//   Node? head;

//   SinglyLinkedList();

//   void insert(int data){
//     print(data);
//     Node newNode = Node(data);
//     if(head == null){
//       head = newNode;
//     } else{
//       Node? current = head;
//         while(current!.next != null){
//           current = current.next;
//         }
//         current.next = newNode;
//     }
//   }

//   void traverse(){
//     if(head == null){
//       print("empty");
//     } else{
//       Node? current = head;
//       print(current);
//         while(current!.next != null){
//           current = current.next;
//           print(current);
//         }
//     }
//   }
// }

// void main(){
//   SinglyLinkedList sll = SinglyLinkedList();
//   // sll.traverse();
//   sll.insert(1);
//   sll.traverse();
//   // sll.insert(4);
//   // sll.traverse();
// }

class Node {
  int data;
  Node? next;

  Node(this.data, [this.next]);

  @override
  String toString() {
    return "Data: $data | Next: ${next != null ? next!.data : 'null'}";
  }
}

class SinglyLinkedList {
  Node? head;

  SinglyLinkedList([int? initialData]) {
    if (initialData != null) {
      head = Node(initialData);
    }
  }

  void insert(int data) {
    Node newNode = Node(data);
    if (head == null) {
      head = newNode;
    } else {
      Node? current = head;
      while (current!.next != null) {
        current = current.next;
      }
      current.next = newNode;
    }
  }

  void traverse() {
    print("--TRAVERSE--");
    if (head == null) {
      print("empty");
    } else {
      Node? current = head;
      while (current != null) {
        print(current);
        current = current.next;
      }
    }
  }

  bool search(int toFind){
    Node? current = head;
    while (current != null){
      if(current.data == toFind){
        return true;
      }
      current = current.next;
    }
    return false;
  }

  void delete(int toDelete){
    if(head != null){
      return;
    }
    if(head!.data == toDelete){
      head = head!.next;
      return;
    }
    Node? current = head!.next;
    print(current);
    while(current != null){
      print("z");
      if(current.next!.data == toDelete){
        print("a");
        current.next = current.next!.next;
        return;
      }
      current = current.next;
    }
  }
}

void main() {
  SinglyLinkedList emptyList = SinglyLinkedList();
  print("Empty List:");
  emptyList.traverse();

  SinglyLinkedList listWithInitialNode = SinglyLinkedList(1);
  print("\nList with Initial Node:");
  listWithInitialNode.traverse();

  listWithInitialNode.insert(2);
  listWithInitialNode.insert(3);
  listWithInitialNode.insert(6);
  listWithInitialNode.insert(8);
  listWithInitialNode.insert(10);
  listWithInitialNode.insert(9);
  print("\nList after Inserts:");
  listWithInitialNode.traverse();
  print(listWithInitialNode.search(6));
  print(listWithInitialNode.search(3));
  listWithInitialNode.traverse();
  listWithInitialNode.delete(10);
  listWithInitialNode.traverse();
}
