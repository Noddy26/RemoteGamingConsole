package Code.Activitys;

import android.bluetooth.BluetoothDevice;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.os.Message;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import com.example.remotegamingapp.R;


public class MainActivity extends AppCompatActivity {

    private static final int SECOND_ACTIVITY_REQUEST_CODE = 0;
    private static MainActivity input;
    private boolean stream_started = false;


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu_top, menu);
        return true;
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        if (LoginActivity.Loggedin){
            super.onCreate(savedInstanceState);
            setContentView(R.layout.main_activity);
        }
        input = this;
    }

    public void Start_stream(MenuItem item) {
        System.out.println("start");
        Intent intentGoSocketService = new Intent("StartStreamingServer");
        intentGoSocketService.putExtra("sendmessage", "Start");
        sendBroadcast(intentGoSocketService);
        stream_started = true;
        Intent myIntent = new Intent(this, StreamActivity.class);
        startActivityForResult(myIntent, SECOND_ACTIVITY_REQUEST_CODE);
    }

    public void stop_stream(MenuItem item) {
        if (stream_started){
            Intent myIntent = new Intent(this, MainActivity.class);
            startActivityForResult(myIntent, SECOND_ACTIVITY_REQUEST_CODE);
            System.out.println("stop");
            stream_started = false;
        }
        Toast.makeText(this, "Stream not started", Toast.LENGTH_SHORT).show();
    }

    public void Scan(MenuItem item) {
        Toast.makeText(MainActivity.this, "Bluetooth setup", Toast.LENGTH_SHORT).show();
        Intent myIntent = new Intent(this, BluetoothActivity.class);
        startActivityForResult(myIntent, SECOND_ACTIVITY_REQUEST_CODE);
    }
    public void conn(MenuItem item) {
        System.out.println("bluetooth");
    }

    public void Cast(MenuItem item){
        System.out.println("casting");
    }

    public void video_quality(MenuItem item) {
        Toast.makeText(MainActivity.this, "Video Quality", Toast.LENGTH_SHORT).show();
        Intent myIntent = new Intent(this, VideoActivity.class);
        startActivityForResult(myIntent, SECOND_ACTIVITY_REQUEST_CODE);
    }

    public void Logout(MenuItem item) {
        LoginActivity.Loggedin = false;
        Toast.makeText(MainActivity.this, "LoggedOut", Toast.LENGTH_SHORT).show();
        Intent Intent = new Intent(MainActivity.this, LoginActivity.class);
        MainActivity.this.startActivity(Intent);
    }
    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == SECOND_ACTIVITY_REQUEST_CODE) {
            if (resultCode == RESULT_OK) {
                String quality ,frames;
                quality = data.getStringExtra("Resolution");
                frames = data.getStringExtra("Frames");
                System.out.println(quality);
                System.out.println(frames);
            }
        }
    }
    public static MainActivity getInstace() {
        return input;
    }

    public void getReply(final String reply) {
//        if (reply.contains("Access Granted")){
//            Toast.makeText(MainActivity.this, "Welcome " + client, Toast.LENGTH_SHORT).show();
//            Intent myIntent = new Intent(Activity.this, MainActivity.class);
//            myIntent.putExtra("Username", client);
//            MainActivity.this.startActivity(myIntent);
//        }
//        else{
//            Toast.makeText(MainActivity.this, "Details incorrect", Toast.LENGTH_LONG).show();
//        }
        System.out.println("process");
    }
    private BroadcastReceiver myReceiver = new BroadcastReceiver() {

        @Override
        public void onReceive(Context context, Intent intent) {
            Message msg = Message.obtain();
            String action = intent.getAction();
            if(BluetoothDevice.ACTION_FOUND.equals(action)){
                System.out.println("hello");
                //Found, add to a device list
            }
        }
    };


}
