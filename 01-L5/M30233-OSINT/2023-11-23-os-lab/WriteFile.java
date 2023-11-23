import java.io.* ;
  public class WriteFile {
      public static void main(String [] args) throws Exception {
          FileOutputStream out = new FileOutputStream("C:/Users/thoma/git/uni-programming/01-L5/M30233-OSINT/2023-11-23-os-lab/tweedle-dee-slightly-more-different.txt");
          String text = "Shoes and ships and sealing wax." ;
          byte buffer [] = text.getBytes();
          out.write(buffer) ;
          out.close() ;
      }
  }
