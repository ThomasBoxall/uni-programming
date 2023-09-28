public class RandomNumberWithSleep {
    public static void main(String [] args) throws Exception{
        double random = Math.floor(Math.random() *(5000 - 1 + 1) + 1);
        System.out.println(random);
        Thread.sleep((long) random);
        System.out.println("done");
    }
}
