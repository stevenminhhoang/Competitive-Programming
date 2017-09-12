import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
	    boolean open = true;
	    boolean end = false;
        String line;
        while(scanner.hasNextLine()) {
           line = scanner.nextLine();
           for(int i=0; i<line.length(); i++) {
               if(line.charAt(i) == '\u001a') {
                   end = true;
                   break;
               }
               if(line.charAt(i) == '\"') {
                   if(open == true) {
                       System.out.print("``");
                       open = false;
                       continue;
                   }
                   if(open == false) {
                       System.out.print("''");
                       end = true;
                       continue;
                   }
               }
               System.out.print(line.charAt(i));
           }
           System.out.print("\n");
        }

    }
}
