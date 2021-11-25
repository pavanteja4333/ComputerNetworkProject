package case_study;

import java.io.*; 
 
import java.net.*; 
  
// Server class 
public class Server  
{ 
    public static void main(String[] args) throws IOException  
    { 
        // server is listening on port 8080
        ServerSocket ss = new ServerSocket(8080); 
          
        // running infinite loop for getting 
        // client request 
        while (true)  
        { 
            Socket s = null; 
              
            try 
            { 
                // socket object to receive incoming client requests 
                s = ss.accept(); 
                  
                System.out.println("A new client is connected : " + s); 
                  
                // obtaining input and out streams 
                DataInputStream dis = new DataInputStream(s.getInputStream()); 
                DataOutputStream dos = new DataOutputStream(s.getOutputStream()); 
                  
                System.out.println("Assigning new thread for this client"); 
  
                // create a new thread object 
                Thread t = new ClientHandler(s, dis, dos); 
  
                // Invoking the start() method 
                t.start(); 
                  
            } 
            catch (Exception e){ 
                ss.close(); 
                e.printStackTrace(); 
            } 
        } 
    } 
} 
  
// ClientHandler class 
class ClientHandler extends Thread  
{ 
    
    final DataInputStream dis; 
    final DataOutputStream dos; 
    final Socket s; 
      
  
    // Constructor 
    public ClientHandler(Socket s, DataInputStream dis, DataOutputStream dos)  
    { 
        this.s = s; 
        this.dis = dis; 
        this.dos = dos; 
    } 
  
    @Override
    public void run()  
    { 
        String received; 
        String toreturn; 
        while (true)  
        { 
            try { 
  
                // MENU
                dos.writeUTF("E-Payment Service\nMenu\n1.Check Your balance\n2.Make payment\n3.View Transaction History\nSelect and option or .. Type Exit to terminate connection."); 
                  
                // receive the answer from client 
                received = dis.readUTF(); 
                  
                if(received.equals("Exit")) 
                {  
                    System.out.println("Client " + this.s + " sends exit..."); 
                    System.out.println("Closing this connection."); 
                    this.s.close(); 
                    System.out.println("Connection closed"); 
                    break; 
                } 
                
//                System.out.println(received);
                String[] data = received.split(" ");
                File fileToBeModified = new File("C:\\Users\\PhaniTeja\\Desktop\\Payment.txt");
                File Transactionsfile = new File("C:\\Users\\PhaniTeja\\Desktop\\transaction.txt");
                String contents = "";
                BufferedReader reader = null;
                FileWriter writer = null;
                
                if(data[0].equals("1")) {
                    reader = new BufferedReader(new FileReader(fileToBeModified)); 
                    String line = reader.readLine();
                     
                    while (line != null) 
                    {
                        String[] filecont = line.split(" ");
                        if(filecont[0].equals(data[1])) {
                            contents = "Your Balance is: "+filecont[1];
                            break;
                        }
                        line = reader.readLine();
                    }
                    if(contents.length()==0) {
                        contents= "Invalid Phone number";
                    }
                    toreturn =  contents;
                    dos.writeUTF(toreturn);
                    
                }
                if(data[0].equals("2")) {
//                  System.out.println("2 selected");
                    reader = new BufferedReader(new FileReader(fileToBeModified)); 
                    String line = reader.readLine();
                    int flag=0; 
                    while (line != null) 
                    {
                        String[] filecont = line.split(" ");
                        if(filecont[0].equals(data[1]) && Integer.parseInt(filecont[1])>=Integer.parseInt(data[3])) {
                            int bal = Integer.parseInt(filecont[1]);
                            bal = bal-Integer.parseInt(data[3]);
                            contents = contents + filecont[0]+" "+String.valueOf(bal) + System.lineSeparator();
                            flag++;
                        }
                        else if(filecont[0].equals(data[2])) {
                            int bal = Integer.parseInt(filecont[1]);
                            bal = bal+Integer.parseInt(data[3]);
                            contents = contents + filecont[0]+" "+String.valueOf(bal) + System.lineSeparator();
                            flag++;
                        }
                        else {
                            contents = contents + line + System.lineSeparator();
                        }
                        line = reader.readLine();
                    }
                    if(flag==2) {
                        writer = new FileWriter(fileToBeModified);
                        writer.write(contents);
                        writer.close();
//                        System.out.println(contents);
                        contents="";
                        reader = new BufferedReader(new FileReader(Transactionsfile)); 
                        line = reader.readLine();
                        while (line != null) 
                        {
                            contents = contents + line + System.lineSeparator();
                             
                            line = reader.readLine();
                        }
                        String temp="";
                        
                        for(int i=1;i<data.length;++i) {
                            temp=temp+data[i]+" ";
                        }
                        contents = contents+ temp +System.lineSeparator();
                        writer = new FileWriter(Transactionsfile);
                        writer.write(contents);
                        writer.close();
                        dos.writeUTF("Payment succesful!");
                        
                        //
                        
                    }
                    else {
                        dos.writeUTF("Payment Not succesful...");
                    }
                }
                
                if(data[0].equals("3")) {
                    reader = new BufferedReader(new FileReader(Transactionsfile)); 
                    contents="";
                    String line = reader.readLine();
                    while (line != null) 
                    {
                        
                        String[] t = line.split(" ");
                        if(t[0].equals(data[1])) {
                        contents = contents + line + System.lineSeparator();
                        } 
                        line = reader.readLine();
                    }
                    
                    if(contents.length()==0) {
                        dos.writeUTF("Oops your Transaction History seems to be empty!!!....");
                        
                    }
                    else {
                        dos.writeUTF(contents);
                    }
               
            }
            }catch (IOException e) { 
                e.printStackTrace(); 
            } 
        } 
          
        try
        { 
            // closing resources 
            this.dis.close(); 
            this.dos.close(); 
              
        }catch(IOException e){ 
            e.printStackTrace(); 
        }  
} 
}
