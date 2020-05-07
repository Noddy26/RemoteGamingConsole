package Code.Activitys;

import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Set;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothClass;
import android.bluetooth.BluetoothDevice;
import android.content.IntentFilter;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.remotegamingapp.R;

import Code.Braodcasters.BluetoothBroadcaster;


public class BluetoothActivity extends AppCompatActivity {

    ListView listViewPaired;
    ListView listViewDetected;
    ArrayList<String> arrayListpaired;
    ArrayList<String> arrayListDevices;
    ArrayAdapter<String> adapter, detectedAdapter;

    BluetoothDevice bdDevice, connDevice;
    ArrayList<BluetoothDevice> arrayListPairedBluetoothDevices;
    ArrayList<BluetoothDevice> arrayListBluetoothDevices;
    BluetoothAdapter bluetoothAdapter = null;

    private static BluetoothActivity input;

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.blue_menu_top, menu);
        return true;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.bluetooth_activity);
        input = this;
        listViewDetected = (ListView) findViewById(R.id.listViewDetected);
        listViewPaired = (ListView) findViewById(R.id.listViewPaired);
        arrayListpaired = new ArrayList<String>();
        arrayListDevices = new ArrayList<String>();

        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();

        arrayListPairedBluetoothDevices = new ArrayList<BluetoothDevice>();
        arrayListBluetoothDevices = new ArrayList<BluetoothDevice>();

        detectedAdapter = new ArrayAdapter<String>( BluetoothActivity.this, android.R.layout.simple_list_item_single_choice);
        listViewDetected.setAdapter(detectedAdapter);
        adapter= new ArrayAdapter<String>( BluetoothActivity.this, android.R.layout.simple_list_item_1, arrayListpaired);

        listViewPaired.setAdapter(adapter);
        getPairedDevices();

        listViewPaired.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                connDevice =  arrayListPairedBluetoothDevices.get(position);
                Boolean bool = false;
                try {
                    Class cl = Class.forName("android.bluetooth.BluetoothDevice");
                    Class[] par = {};
                    Method method = cl.getMethod("createBond", par);
                    Object[] args = {};
                    bool = (Boolean) method.invoke(connDevice);
                    String name = connDevice.getName();
                    if (bool.booleanValue() == true)
                        Toast.makeText(BluetoothActivity.this,"Connected to " + name, Toast.LENGTH_SHORT).show();
                    else
                        Toast.makeText(BluetoothActivity.this,"Can not Connect to " + name, Toast.LENGTH_SHORT).show();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        listViewDetected.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                bdDevice = arrayListBluetoothDevices.get(position);
                Boolean isBonded = false;
                try {
                    isBonded = createBond(bdDevice);
                    if (isBonded) {
                        Toast.makeText(BluetoothActivity.this, "Connecting to device", Toast.LENGTH_SHORT).show();
                        arrayListpaired.add(bdDevice.getName() + "\n" + bdDevice.getAddress());
                        adapter.notifyDataSetChanged();
                        getPairedDevices();
                        adapter.notifyDataSetChanged();
                    } else
                        Toast.makeText(BluetoothActivity.this, "Can not find device", Toast.LENGTH_SHORT).show();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });

    }
    public void bluetooth_on(MenuItem item) {
        onBluetooth();
    }
    public void bluetooth_off(MenuItem item) {
        offBluetooth();
    }
    public void bluetooth_scan(MenuItem item) {
        startSearching();
    }

    public boolean createBond(BluetoothDevice btDevice) throws Exception {
        Class class1 = Class.forName("android.bluetooth.BluetoothDevice");
        Method createBondMethod = class1.getMethod("createBond");
        Boolean returnValue = (Boolean) createBondMethod.invoke(btDevice);
        String name = btDevice.getName();
        Toast.makeText(BluetoothActivity.this, name + " paired", Toast.LENGTH_SHORT).show();
        return returnValue.booleanValue();
    }

    private void startSearching() {
        Toast.makeText(this,"Starting Search", Toast.LENGTH_SHORT).show();
        registerReceiver(new BluetoothBroadcaster(), new IntentFilter(BluetoothDevice.ACTION_FOUND));
        bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        bluetoothAdapter.startDiscovery();
    }
    private void onBluetooth() {
        if(!bluetoothAdapter.isEnabled())
            bluetoothAdapter.enable();
        else
            Toast.makeText(this,"Bluetooth already On", Toast.LENGTH_SHORT).show();
    }
    private void offBluetooth() {
        if(bluetoothAdapter.isEnabled())
            bluetoothAdapter.disable();
        else
            Toast.makeText(this,"Bluetooth already off", Toast.LENGTH_SHORT).show();
    }
    public static BluetoothActivity getInstace() {
        return input;
    }
    public void updateFoundBluetoothDevices( BluetoothDevice devices ) {
        arrayListDevices.add(devices.getName() + "\n" + devices.getAddress());
        System.out.println(arrayListDevices);
        arrayListBluetoothDevices.add(devices);
        listViewDetected.setAdapter(new ArrayAdapter<String>(BluetoothActivity.this,
                android.R.layout.simple_list_item_1, arrayListDevices));
    }
    private void getPairedDevices() {
        Set<BluetoothDevice> pairedDevice = bluetoothAdapter.getBondedDevices();
        if(pairedDevice.size()>0)
        {
            for(BluetoothDevice device : pairedDevice) {
                arrayListpaired.add(device.getName() + "\n" + device.getAddress());
                arrayListPairedBluetoothDevices.add(device);
            }
        }
        adapter.notifyDataSetChanged();
    }

}