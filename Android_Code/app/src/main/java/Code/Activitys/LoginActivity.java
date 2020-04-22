package Code.Activitys;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.remotegamingapp.R;

import Code.Services.SocketService;

public class LoginActivity extends AppCompatActivity {

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

        username = findViewById(R.id.username);
        password = findViewById(R.id.password);
        btnSend = findViewById(R.id.button2);

        btnSend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                client = username.getText().toString().trim();
                String user = client;
                String pass = password.getText().toString().trim();
                String message = user + "+" + pass;
                if (!message.isEmpty()) {
                    Intent intentGoSocketService = new Intent("SendMessage");
                    intentGoSocketService.putExtra("sendmessage", message);
                    sendBroadcast(intentGoSocketService);
                }
            }
        });
    }
    public void forgot_pass(View item){
        System.out.println("fuck yes");
    }
    public static LoginActivity getInstace() {
        return ins;
    }

    public void getReply(final String reply) {
        if (reply.contains("Access Granted")){
            Toast.makeText(LoginActivity.this, "Welcome " + client, Toast.LENGTH_SHORT).show();
            Intent myIntent = new Intent(LoginActivity.this, MainActivity.class);
            myIntent.putExtra("Username", client);
            LoginActivity.this.startActivity(myIntent);
        }
        else{
            Toast.makeText(LoginActivity.this, "Details incorrect", Toast.LENGTH_LONG).show();
        }
    }

}
