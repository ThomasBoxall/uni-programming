import java.io.* ;
import java.util.* ;

public class GetAttributes {

    public static void main(String [] args) throws Exception {
    
        File dum = new File("C:/Users/thoma/git/uni-programming/01-L5/M30233-OSINT/2023-11-23-os-lab/tweedle-dum.txt");

        System.out.println("Is a directory?: " + dum.isDirectory()) ;
        System.out.println("Is an ordinary file?: " + dum.isFile()) ;
        System.out.println("Length: " + dum.length()) ;
        System.out.println("Last modified: " + new Date(dum.lastModified())) ;
        System.out.println("Can be read by this process?: " + dum.canRead()) ;
        System.out.println("Can be written by this process?: " + dum.canWrite()) ;
        System.out.println("Is a hidden file?: " + dum.isHidden()) ;
    }
}
