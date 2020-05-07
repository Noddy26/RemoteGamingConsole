package Code.Methods;

import android.content.Intent;
import android.view.InputDevice;
import java.util.ArrayList;


public class BluetoothController extends Thread {

    public void getGameControllerIds() {
        ArrayList<Integer> gameControllerDeviceIds = new ArrayList<Integer>();
        int[] deviceIds = InputDevice.getDeviceIds();
        for (int deviceId : deviceIds) {
            InputDevice dev = InputDevice.getDevice(deviceId);
            int sources = dev.getSources();

            if (((sources & InputDevice.SOURCE_GAMEPAD) == InputDevice.SOURCE_GAMEPAD)
                    || ((sources & InputDevice.SOURCE_JOYSTICK)
                    == InputDevice.SOURCE_JOYSTICK)) {
                if (!gameControllerDeviceIds.contains(deviceId)) {
                    gameControllerDeviceIds.add(deviceId);
                }
            }
        }
//        String message =
//        Intent intentGoSocketService = new Intent("SendMessage");
//        intentGoSocketService.putExtra("sendmessage", message);
//        sendBroadcast(intentGoSocketService);
//        return gameControllerDeviceIds;
    }
}