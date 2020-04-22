package Code.Activitys;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import com.example.remotegamingapp.R;


public class MainActivity extends AppCompatActivity {

    public static boolean Loggedin;
    private static final int SECOND_ACTIVITY_REQUEST_CODE = 0;
    private static MainActivity input;
    Button start;
    Button stop;
    Button video_quaility;
    Button bluetooth;
    Button Logout;


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu_top, menu);
        return true;
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_activity);
        Loggedin = true;
        input = this;
//        start = findViewById(R.id.);
//        stop = findViewById(R.id.stop);
        video_quaility = findViewById(R.id.video);
//        bluetooth =  findViewById(R.id.Bluetooth);
//        Logout = findViewById(R.id.logout);

    }

    public void Start_stream(MenuItem item) {
        stop = findViewById(R.id.stop);
        stop.setEnabled(true);
        System.out.println("start");
        Intent myIntent = new Intent(this, StreamActivity.class);
        startActivityForResult(myIntent, SECOND_ACTIVITY_REQUEST_CODE);
    }

    public void stop_stream(MenuItem item) {
        stop = findViewById(R.id.stop);
        stop.setEnabled(false);
        Intent myIntent = new Intent(this, MainActivity.class);
        startActivityForResult(myIntent, SECOND_ACTIVITY_REQUEST_CODE);
        System.out.println("stop");
    }

    public void controller(MenuItem item) {
        System.out.println("bluetooth");
    }

    public void Video_Quality(MenuItem item) {
        Toast.makeText(MainActivity.this, "Video Quality", Toast.LENGTH_SHORT).show();
        Intent myIntent = new Intent(this, VideoActivity.class);
        startActivityForResult(myIntent, SECOND_ACTIVITY_REQUEST_CODE);
    }

    public void logout(MenuItem item) {
        Loggedin = false;
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
}
