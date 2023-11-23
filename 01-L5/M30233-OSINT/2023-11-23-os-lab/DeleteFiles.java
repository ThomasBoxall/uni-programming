import java.io.*;
    public class DeleteFiles {
    public static void main(String args []) throws Exception { 
        File dum = new File("C:/Users/thoma/git/uni-programming/01-L5/M30233-OSINT/2023-11-23-os-lab/tweedle-dum.txt");
        File dee = new File("tweedle-dee.txt"); 
        dum.delete();
        dee.delete();
    }
}
