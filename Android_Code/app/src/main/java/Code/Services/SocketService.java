package Code.Services;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

import android.app.Service;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Binder;
import android.os.IBinder;

import Code.Activitys.LoginActivity;
import Code.Activitys.MainActivity;


public class SocketService extends Service {

    public static final String SERVER_IP = "192.168.1.13";
    public static final int SERVER_PORT = 2003;
    private PrintWriter output;
    private BufferedReader input;
    Socket socket;

    @Override
    public IBinder onBind(Intent intent) {
        return myBinder;
    }

    private final IBinder myBinder = new LocalBinder();

    public class LocalBinder extends Binder {
        public SocketService getService() {
            return SocketService.this;
        }
    }
    @Override
    public void onCreate() {
        //super.onCreate();
        System.out.println("onCreate");
        IntentFilter filter = new IntentFilter();
        filter.addAction("SendMessage");
        filter.addAction("ReceiveMessage");
        registerReceiver(receiver, filter);

    }
    class Thread3 implements Runnable {
        private String message;

        Thread3(String message) {
            System.out.println("Thread");
            this.message = message;
        }
        @Override
        public void run() {
            System.out.println("sending");
            output.write(message);
            output.flush();
            new Thread(new Thread2()).start();

        }

    }
    class Thread2 implements Runnable {
        @Override
        public void run() {
            final String message;
            try {
                message = input.readLine();

                System.out.println(message);
                if (message != null) {
                    Intent intentGoSocketService = new Intent("ReceiveMessage");
                    intentGoSocketService.putExtra("receivemessage", message);
                    sendBroadcast(intentGoSocketService);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    @Override
    public int onStartCommand(Intent intent,int flags, int startId){
        super.onStartCommand(intent, flags, startId);
        System.out.println("service started");
        Runnable connect = new connectSocket();
        new Thread(connect).start();
        return START_STICKY;
    }
    class connectSocket implements Runnable {
        @Override
        public void run() {
            try {
                System.out.println("connecting");
                socket = new Socket(SERVER_IP, SERVER_PORT);
                output = new PrintWriter(socket.getOutputStream());
                input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    @Override
    public void onDestroy() {
        super.onDestroy();
        try {
            socket.close();
            unregisterReceiver(receiver);
        } catch (Exception e) {
            e.printStackTrace();
        }
        socket = null;
    }

    private final BroadcastReceiver receiver = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if (action.equals("SendMessage")){
                String send_message = intent.getStringExtra("sendmessage");
                if (send_message != null)
                    new Thread(new Thread3(send_message)).start();
            }
            else if (action.equals("ReceiveMessage")){
                try {
                    String mess = intent.getStringExtra("receivemessage");
                    if (mess != null)
                        if (!MainActivity.Loggedin) {
                            LoginActivity.getInstace().getReply(mess);
                        }else{
                            MainActivity.getInstace().getReply(mess);
                        }
                        System.out.println("hello");
                } catch (Exception e) {
                    System.out.println("error");
                    System.out.println(e);
                }
            }

        }
    };
}