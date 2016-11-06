import java.util.Scanner;

public class flTest {

    public static void main(String args[]) {
        
//Singel line comment

/*
    Multi line comment
*/

        int    i = 0;
        double d = 0.0;
        float  f = 0.0;
        String s = "A string!"    

        while(i < 100) {
            outerLoop:
            for(int j = 0; j< i; j++) {
                break outerLoop;
            }

        

        }

    }

}

//Extends
public class Stuff extends MoreStuff {
    
    public Stuff(void) {  
    }

    private jee(int i) {
        return 1;
    }
 
}
interface myInterface {
    
}

//Implements
public class evenMoreStuff implements myInterface {
    public evenMoreStuff(void) {
    
    }
}


