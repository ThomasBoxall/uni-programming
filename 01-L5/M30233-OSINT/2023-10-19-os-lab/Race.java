public class Race {

    public static void main(String args []) throws Exception { 
        MyThread.count = 0;
        MyThread thread1 = new MyThread();
        MyThread thread2 = new MyThread();
        thread1.start() ; thread2.start();

        thread2.join() ; thread1.join();

        System.out.println("MyThread.count = " + MyThread.count);
    }
}

class MyThread extends Thread { 
    static volatile int count;
    String name;


    public void run() {

        for(int i = 0 ; i < 100000000 ; i++) { 
            increment();
        }
    }

    synchronized static void increment() { 
        int x = count;
        count = x + 1 ;
    }
}
