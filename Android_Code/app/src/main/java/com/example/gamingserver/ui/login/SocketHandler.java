package com.example.gamingserver.ui.login;

import java.net.Socket;

public class SocketHandler {
    private static Socket socket;

    public static synchronized Socket getSocket(){
        return socket;
    }

    static synchronized void setSocket(Socket socket){
        SocketHandler.socket = socket;
    }
}
