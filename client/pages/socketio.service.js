import { io } from 'socket.io-client';

class SocketioService {
    socket = null;

    constructor() {
        this.socket = null;
        // this.storedSocketURL = localStorage.getItem('socketURL');
        // this.storedSocketOptions = JSON.parse(localStorage.getItem('socketOptions'));

    }

    setupSocketConnection() {
        try {
            this.socket = io("ws://127.0.0.1:8000/", {
                path: "/ws/socket.io",
                autoConnect: false,
                // auth: {
                //     token: "123",
                // },
            });
            this.socket.connect();


            this.socket.on("connect", () => {
                console.log("Socket connectedddd!");
                this.socket.emit("chat", "Hello FastAPI");
            });

            this.socket.on("error", (error) => {
                console.error("Socket error:", error);
            });

            this.socket.on("disconnect", (reason) => {
                console.warn("Socket disconnected:", reason);
                console.log("Socket disconnected:", reason);
                this.socket.emit("disconnect1", reason);
            });
        } catch (error) {
            console.error("Socket connection error:", error);
        }
    }

    sendToFastAPI() {
        // this.socket.connect();
        console.log("sendToFastAPI");
        this.socket.emit("chat1", "Hello FastAPI");

    }


}

export default new SocketioService();

//https://github.com/tiangolo/fastapi/issues/3670
