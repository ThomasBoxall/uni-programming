import java.io.* ;
public class ReadFile {
      public static void main(String [] args) throws Exception {      
          FileInputStream in = new FileInputStream("C:/Users/thoma/git/uni-programming/01-L5/M30233-OSINT/2023-11-23-os-lab/tweedle-dum.txt");
          byte buffer [] = new byte [100] ;
          int numBytesRead = in.read(buffer) ;
        //   System.out.println(new String(buffer)) ;
        while(numBytesRead > 0) {
            System.out.print(new String(buffer, 0, numBytesRead)) ; 
            numBytesRead = in.read(buffer) ;
        }
            
      }
  }
