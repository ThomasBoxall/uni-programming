public class MyObjectTest 
{ public static void main(String args []) 
{ 
MyClass object1 = new MyClass() ;
// set a and b in object1
object1.a = 42;
object1.b = "my string value";
MyClass object2 = new MyClass();

// set a and b in object2
object2.a = 23;
object2.b = "my other string value";

// print fields:
System.out.println("Field a in object1 is: " + object1.a);
System.out.println("Field b in object1 is: " + object1.b);

System.out.println("Field a in object2 is: " + object2.a);
System.out.println("Field b in object2 is: " + object2.b);
}
}

class MyClass 
{ 
int a; 
String b;
}
