//package Code.Services;
//
//import android.app.Service;
//import android.content.Intent;
//import android.content.IntentFilter;
//import android.os.Binder;
//import android.os.IBinder;
//import android.view.InputDevice;
//import android.view.MotionEvent;
//
//import java.util.ArrayList;
//import java.util.List;
//
//import Code.Methods.Controllermethod;
//
//
//public abstract class ControllerService extends Service {
//
//    @Override
//    public IBinder onBind(Intent intent) {
//        return myBinder;
//    }
//
//    private final IBinder myBinder = new ControllerService.LocalBinder();
//
//    public class LocalBinder extends Binder {
//        public ControllerService getService() {
//            return ControllerService.this;
//        }
//    }
//    @Override
//    public void onCreate() {
//        //super.onCreate();
//        System.out.println("onCreate");
//        ArrayList<Integer> Ids = getGameControllerIds();
//
//
//    }
//    public ArrayList<Integer> getGameControllerIds() {
//        ArrayList<Integer> gameControllerDeviceIds = new ArrayList<Integer>();
//        int[] deviceIds = InputDevice.getDeviceIds();
//        for (int deviceId : deviceIds) {
//            InputDevice dev = InputDevice.getDevice(deviceId);
//            int sources = dev.getSources();
//            if (((sources & InputDevice.SOURCE_GAMEPAD) == InputDevice.SOURCE_GAMEPAD)
//                    || ((sources & InputDevice.SOURCE_JOYSTICK)
//                    == InputDevice.SOURCE_JOYSTICK)) {
//                if (!gameControllerDeviceIds.contains(deviceId)) {
//                    gameControllerDeviceIds.add(deviceId);
//                }
//            }
//        }
//        return gameControllerDeviceIds;
//    }
//    public void motion(){
//        public List<InputDevice.MotionRange> getMotionRanges (int, int){
//
//        }
//
//    }
//
//}