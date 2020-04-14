package com.example.gamingserver.ui.login;

import android.annotation.SuppressLint;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.Toast;

import com.example.gamingserver.R;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

@SuppressLint("SetTextI18n")
public class LoginActivity extends AppCompatActivity {
    Thread Thread1 = null;
    EditText username;
    EditText password;
    Button btnSend;
    String SERVER_IP;
    Socket socket;
    int SERVER_PORT;
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
        btnSend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String user = username.getText().toString().trim();
                String pass = password.getText().toString().trim();
                String message = user + "+" + pass;
                if (!message.isEmpty()) {
                    new Thread(new Thread3(message)).start();
                }
            }
        });
    }
    private PrintWriter output;
    private BufferedReader input;
    class Thread1 implements Runnable {
        public void run() {
            try {
                socket = new Socket(SERVER_IP, SERVER_PORT);
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
            while (true) {
                try {
                    final String message = input.readLine();
                    if (message != null) {
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                if (message.equals("Access Granted")){
                                    Toast.makeText(LoginActivity.this, "welcome", Toast.LENGTH_LONG).show();
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
                    System.out.println("what");
                    e.printStackTrace();
                }
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
    @SuppressLint("ShowToast")
    protected void onPause() {
        super.onPause();
        new Thread(new Thread3("Connection Term")).start();
    }
    @SuppressLint("ShowToast")
    @Override
    protected void onStop() {
        super.onStop();
        new Thread(new Thread3("Connection Term")).start();
    }
}