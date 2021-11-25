package case_study;
import java.io.*; 
import java.net.*; 
import java.util.Scanner; 
  
//Client class
public class Client {
    public static void main(String[] args) throws IOException  
    { 
        try
        { 
            
            Scanner scn = new Scanner(System.in); 
              
            // getting localhost ip 
            InetAddress ip = InetAddress.getByName("localhost"); 
      
            // establish the connection with server port 8080 
            Socket s = new Socket(ip,8080 ); 
      
            // obtaining input and out streams 
            DataInputStream dis = new DataInputStream(s.getInputStream()); 
            DataOutputStream dos = new DataOutputStream(s.getOutputStream()); 
      
            // the following loop performs the exchange of 
            // information between client and client handler 
            while (true)  
            { 
                System.out.println(dis.readUTF()); 
                String tosend = "";
                String details;
                details = scn.nextLine();
                if(!details.equals("Exit")) {
                if(details.equals("1")) {
                    tosend+=details+" ";
                    System.out.println("Enter your phone number");
                    details = scn.nextLine();
                    while(details.length()<10) {
                        System.out.println("Enter valid phone number:");
                        details = scn.nextLine();
                    }
                    tosend+=details;
                }
                if(details.equals("2")) {
                tosend+=details+" ";
                System.out.println("Enter your phone number:");
                details = scn.nextLine();
                while(details.length()<10) {
                    System.out.println("Enter valid phone number:");
                    details = scn.nextLine();
                }
                tosend+=details+" ";
                System.out.println("Enter your recipent phone number:");
                details = scn.nextLine();
                while((tosend.equals("2 "+details+" ")) || details.length()<10  ) {
                    System.out.println("Enter valid recipient phone number:");
                    details = scn.nextLine();
                }
                tosend+=details+" ";
                System.out.println("Enter money:");
                details = scn.nextLine();
                while(Integer.parseInt(details)<0) {
                    System.out.println("Enter amount:");
                    details = scn.nextLine();
                }
                tosend+=details+" ";
                System.out.println("Reason:");
                details = scn.nextLine();
                tosend+=details;
                }
                if(details.equals("3")) {
                    tosend+=details+" ";
                    System.out.println("Enter your phone number:");
                    details = scn.nextLine();
                    while(details.length()<10) {
                        System.out.println("Enter valid phone number:");
                        details = scn.nextLine();
                    }
                    tosend+=details;
                    System.out.println("----------------------------------------\nTransaction History\nPhnum\tRec_Phnum\tMoney\tReason\n");
                }
                }
                else {
                    tosend=details;
                }
                dos.writeUTF(tosend); 
                  
                // If client sends exit,close this connection  
                // and then break from the while loop 
                if(tosend.equals("Exit")) 
                { 
                    System.out.println("Closing this connection : " + s); 
                    s.close(); 
                    System.out.println("Connection closed"); 
                    break; 
                } 
                  
                String received = dis.readUTF(); 
                System.out.println(received); 
                System.out.println("----------------------------------------"); 
            } 
              
            // closing resources 
            scn.close(); 
            dis.close(); 
            dos.close(); 
        }catch(Exception e){ 
            e.printStackTrace(); 
        } 
    } 
}
