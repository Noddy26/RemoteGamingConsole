package Code.Services;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.concurrent.BlockingDeque;
import java.util.concurrent.LinkedBlockingDeque;

import android.app.Service;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Binder;
import android.os.IBinder;

import Code.Activitys.LoginActivity;
import Code.Activitys.MainActivity;


public class StreamService extends Service {

    private final BlockingDeque<Byte> queue = new LinkedBlockingDeque<Byte>();
    public static final String SERVER_IP = "192.168.1.13";
    public static final int SERVER_PORT = 2005;
    private DataInputStream input;
    Socket socket;

    @Override
    public IBinder onBind(Intent intent) {
        return myBinder;
    }

    private final IBinder myBinder = new LocalBinder();

    public class LocalBinder extends Binder {
        public StreamService getService() {
            return StreamService.this;
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
    class Thread2 implements Runnable {
        @Override
        public void run() {

            int count;
            byte[] buffer = new byte[8192];

            try {
                while ((count = input.read(buffer)) > 0)
                {
                    System.out.println(buffer);
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
                System.out.println(socket.isConnected());
                input = new DataInputStream(new BufferedInputStream(socket.getInputStream()));
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
            if (action.equals("ReceiveMessage")){
                try {
                    String mess = intent.getStringExtra("receivemessage");
                    if (mess != null)
                        if (!LoginActivity.Loggedin) {
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