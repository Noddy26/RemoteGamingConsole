package com.example.gamingserver.ui.login;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.Spinner;

import androidx.appcompat.app.AppCompatActivity;

import com.example.gamingserver.R;

import java.util.ArrayList;
import java.util.List;

public class VideoActivity extends AppCompatActivity {

    Spinner spinner, spinner2, spinner3;
    CheckBox check1, check2, check3;
    Button submit;
    VideoQuality quality;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.video_activity);
        addItemsOnSpinner2();
        check1 = findViewById(R.id.checkBox1);
        check2 = findViewById(R.id.checkBox2);
        check3 = findViewById(R.id.checkBox3);
        submit = findViewById(R.id.Submit);
        quality = new  VideoQuality();
        check1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(((CompoundButton) view).isChecked()){
                    check2.setEnabled(false);
                    check3.setEnabled(false);
                    String text = spinner.getSelectedItem().toString();
                    quality.setVideo("1920x1080");
                    quality.setFrames(text);
                } else {
                    check2.setEnabled(true);
                    check3.setEnabled(true);
                    quality.setVideo("");
                    quality.setFrames("");
                }
            }
        });
        check2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(((CompoundButton) view).isChecked()){
                    check1.setEnabled(false);
                    check3.setEnabled(false);
                    String text = spinner.getSelectedItem().toString();
                    quality.setVideo("1280x720");
                    quality.setFrames(text);
                } else {
                    check1.setEnabled(true);
                    check3.setEnabled(true);
                    quality.setVideo("");
                    quality.setFrames("");
                }
            }
        });
        check3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(((CompoundButton) view).isChecked()){
                    check2.setEnabled(false);
                    check1.setEnabled(false);
                    String text = spinner.getSelectedItem().toString();
                    quality.setVideo("720x480");
                    quality.setFrames(text);
                } else {
                    check2.setEnabled(true);
                    check1.setEnabled(true);
                    quality.setVideo("");
                    quality.setFrames("");
                }
            }
        });
        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent resultIntent = new Intent();
                resultIntent.putExtra("Resolution", quality.getVideo());
                resultIntent.putExtra("Frames", quality.getFrames());
                setResult(Activity.RESULT_OK, resultIntent);
                finish();
            }
        });
    }


    public void addItemsOnSpinner2() {
        spinner = findViewById(R.id.spinner);
        spinner2 = findViewById(R.id.spinner2);
        spinner3 = findViewById(R.id.spinner3);
        List<String> list1 = new ArrayList<String>();
        list1.add("30fps");
        list1.add("25fps");
        list1.add("15fps");
        ArrayAdapter<String> dataAdapter = new ArrayAdapter<String>(this,
                android.R.layout.simple_spinner_item, list1);
        ArrayAdapter<String> dataAdapter2 = new ArrayAdapter<String>(this,
                android.R.layout.simple_spinner_item, list1);
        ArrayAdapter<String> dataAdapter3 = new ArrayAdapter<String>(this,
                android.R.layout.simple_spinner_item, list1);
        dataAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        dataAdapter2.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        dataAdapter3.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(dataAdapter);
        spinner2.setAdapter(dataAdapter2);
        spinner3.setAdapter(dataAdapter3);
    }
}