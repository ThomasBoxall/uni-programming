import java.util.concurrent.*; 

public class Deadlock2 {
    public static void main(String args []) throws Exception { 
        MyThreadA thread1 = new MyThreadA();
        MyThreadB thread2 = new MyThreadB();
        
        thread1.start() ; 
        thread2.start();

        thread2.join() ; 
        thread1.join();
    }
}

class MyThreadA extends Thread {

    static Semaphore semR = new Semaphore(1); 
    static Semaphore semS = new Semaphore(1); 
    void delay() {
        int delay = (int) (1000 * Math.random());
        try {
            Thread.sleep(delay);
        }
        catch(Exception e) {
        }
    }

    public void run() { 
        try {
            while(true) {
                delay() ;

                System.out.println("Thread A waiting for R"); 
                semR.acquire();
                System.out.println("Thread A acquired R");
delay();
                System.out.println("Thread A waiting for S"); 
                semS.acquire();
                System.out.println("Thread A acquired S"); 
                delay();
                semS.release();
                System.out.println("Thread A released S");

                semR.release();
                System.out.println("Thread A released R");
            }
        }
        catch(Exception e) {}
    }

}

class MyThreadB extends MyThreadA {
 
    public void run() { 
        try {
            while(true) {
                delay() ;

                System.out.println("Thread B waiting for S"); 
                semS.acquire();
                System.out.println("Thread B acquired S"); 
                delay();
          System.out.println("Thread B waiting for R");
semR.acquire();
                System.out.println("Thread B acquired R"); 
                delay();
                semR.release();
                System.out.println("Thread B released R");

                semS.release();
                System.out.println("Thread B released S");
            }
        }
        catch(Exception e) {}
    }

}
