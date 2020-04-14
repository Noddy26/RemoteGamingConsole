package com.example.gamingserver.ui.login;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.gamingserver.R;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.sql.SQLOutput;

@SuppressLint("SetTextI18n")
public class LoginActivity extends AppCompatActivity {
    Thread Thread1 = null;
    EditText username;
    EditText password;
    Button btnSend;
    String SERVER_IP;
    Socket socket;
    boolean Login = false;
    int SERVER_PORT;

//    @Override
//    public boolean onCreateOptionsMenu(Menu menu) {
//        MenuInflater inflater = getMenuInflater();
//        inflater.inflate(R.menu.menu_top, menu);
//        return true;
//    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        username = findViewById(R.id.username);
        password = findViewById(R.id.password);
        btnSend = findViewById(R.id.btnSend);
        SERVER_IP = "192.168.1.13";
        SERVER_PORT = 2003;
        Thread1 = new Thread(new Thread1());
        Thread1.start();
        System.out.println("hello");
        btnSend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String user = username.getText().toString().trim();
                String pass = password.getText().toString().trim();
                String message = user + "+" + pass;
                if (!message.isEmpty()) {
                    new Thread(new Thread3(message)).start();
                }
                if (Login){
                    System.out.println("well done");
                }
            }
        });
    }
    private PrintWriter output;
    private BufferedReader input;

    public void Start_stream(MenuItem item) {
    }

    class Thread1 implements Runnable {
        public void run() {
            try {
                socket = new Socket(SERVER_IP, SERVER_PORT);
                SocketHandler.setSocket(socket);
                output = new PrintWriter(socket.getOutputStream());
                input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                runOnUiThread(new Runnable() {
                    @SuppressLint("ShowToast")
                    @Override
                    public void run() {
                        Toast.makeText(LoginActivity.this, "Connected to server", Toast.LENGTH_LONG).show();
                    }
                });
                new Thread(new Thread2()).start();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    class Thread2 implements Runnable {
        @Override
        public void run() {
            try {
                final String message = input.readLine();
                System.out.println(message);
                if (message != null) {
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            if (message.equals("Access Granted")){
                                Toast.makeText(LoginActivity.this, "welcome", Toast.LENGTH_LONG).show();
                                Intent myIntent = new Intent(LoginActivity.this, MainActivity.class);
                                LoginActivity.this.startActivity(myIntent);
                            }
                            else{
                                Toast.makeText(LoginActivity.this, "User Details incorrect", Toast.LENGTH_LONG).show();
                            }
                        }
                    });
                } else {
                    Thread1 = new Thread(new Thread1());
                    Thread1.start();
                    return;
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    class Thread3 implements Runnable {
        private String message;
        Thread3(String message) {
            this.message = message;
        }
        @Override
        public void run() {
            output.write(message);
            output.flush();
            runOnUiThread(new Runnable() {
                @SuppressLint("ShowToast")
                @Override
                public void run() {
                    Toast.makeText(LoginActivity.this, "Checking..", Toast.LENGTH_SHORT).show();
                    System.out.println("communicating with server");
                    new Thread(new Thread2()).start();
            }
            });
        }
    }
    @Override
    protected void onPause() {
        super.onPause();
        //new Thread(new Thread3("Connection Term")).start();
        System.out.println("onpause");
    }
    @Override
    protected void onStop() {
        super.onStop();
        System.out.println("onStop");
        new Thread(new Thread3("Connection Term")).start();
    }
    @Override
    protected void onDestroy() {
        super.onDestroy();
        System.out.println("onDestory");
        new Thread(new Thread3("Connection Term")).start();
    }
}