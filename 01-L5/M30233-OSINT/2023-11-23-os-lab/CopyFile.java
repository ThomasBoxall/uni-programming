 import java.io.* ;

public class CopyFile {

    public static void main(String [] args) throws Exception {

        FileInputStream in = new FileInputStream("C:/Users/thoma/git/uni-programming/01-L5/M30233-OSINT/2023-11-23-os-lab/tweedle-dum.txt");

        FileOutputStream out = new FileOutputStream("C:/Users/thoma/git/uni-programming/01-L5/M30233-OSINT/2023-11-23-os-lab/tweedle-dee.txt");

        byte buffer [] = new byte [100] ;

        int numBytesRead = in.read(buffer) ;

        while(numBytesRead > 0) {
            out.write(buffer, 0, numBytesRead) ;
            numBytesRead = in.read(buffer) ;
        }

        out.close();
        in.close();
    }
}
