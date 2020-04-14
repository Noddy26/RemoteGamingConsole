package com.example.gamingserver.ui.login;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.gamingserver.R;

public class MainActivity extends AppCompatActivity {

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
        start = findViewById(R.id.Stream);
        stop = findViewById(R.id.stop);
        video_quaility = findViewById(R.id.quaility);
        bluetooth =  findViewById(R.id.Bluetooth);
        Logout = findViewById(R.id.logout);
        String quality = null, frames = null;
        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            quality = extras.getString("Resolution");
            frames = extras.getString("Frames");
        }
        System.out.println(quality);
        System.out.println(frames);

    }

    public void Start_stream(MenuItem item) {
        stop = findViewById(R.id.stop);
        stop.setEnabled(true);
        System.out.println("start");
    }

    public void stop_stream(MenuItem item) {
        stop = findViewById(R.id.stop);
        stop.setEnabled(false);
        System.out.println("stop");
    }

    public void controller(MenuItem item) {
        System.out.println("bluetooth");
    }

    public void Video_Quality(MenuItem item) {
        Toast.makeText(MainActivity.this, "Video Quality", Toast.LENGTH_SHORT).show();
        Intent myIntent = new Intent(MainActivity.this, VideoActivity.class);
        MainActivity.this.startActivity(myIntent);
    }

    public void logout(MenuItem item) {
        Toast.makeText(MainActivity.this, "LoggedOut", Toast.LENGTH_SHORT).show();
        Intent Intent = new Intent(MainActivity.this, LoginActivity.class);
        MainActivity.this.startActivity(Intent);
    }

}
