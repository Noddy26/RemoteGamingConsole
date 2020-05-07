package Code.Activitys;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.remotegamingapp.R;


import Code.Services.ControllerService;
import Code.Services.SocketService;

public class LoginActivity extends AppCompatActivity {

    public static boolean Loggedin;
    private static LoginActivity ins;
    Intent intentSocketService;
    Button btnSend;
    EditText username;
    EditText password;
    String client;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login_activity);
        ins = this;
        intentSocketService= new Intent(LoginActivity.this, SocketService.class);
        startService(intentSocketService);

        intentSocketService= new Intent(LoginActivity.this, ControllerService.class);
        startService(intentSocketService);

        username = findViewById(R.id.username);
        password = findViewById(R.id.password);
        btnSend = findViewById(R.id.buttonlog);

        btnSend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
//                client = username.getText().toString().trim();
////                String user = client;
////                String pass = password.getText().toString().trim();
////                String message = user + "+" + pass + "+Android";
////                if (!message.isEmpty()) {
////                    Intent intentGoSocketService = new Intent("SendMessage");
////                    intentGoSocketService.putExtra("sendmessage", message);
////                    sendBroadcast(intentGoSocketService);
////                }
                getReply("Access Granted");
            }
        });
    }
    public void forgot_pass(View item){
        System.out.println("");
    }
    public static LoginActivity getInstace() {
        return ins;
    }

    public void getReply(final String reply) {
        if (reply.contains("Access Granted")){
            Loggedin = true;
            Toast.makeText(LoginActivity.this, "Welcome " + client, Toast.LENGTH_SHORT).show();
            Intent myIntent = new Intent(LoginActivity.this, MainActivity.class);
            myIntent.putExtra("Username", client);
            LoginActivity.this.startActivity(myIntent);
        }
        else if(reply.equals("server off")){
            System.out.println("server off");
            Toast.makeText(LoginActivity.this, "Server not responding", Toast.LENGTH_LONG).show();
        }
        else{
            Toast.makeText(LoginActivity.this, "Details incorrect", Toast.LENGTH_LONG).show();
        }
    }

}
