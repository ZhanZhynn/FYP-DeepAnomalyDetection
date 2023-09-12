<template>
    <v-row>
        <v-container>
            <h2>Chuckroom 1.0</h2>
            <p>Some awesome chuck facts.</p>
            <Chatroom />
            <v-btn color="success" @click="getMessage(0)">
                Get Chuck Norris Facts
            </v-btn>
            <v-btn color="error" @click="stopMessage">
                Stop Chuck Norris Facts
            </v-btn>
            {{ keepGenerating }}

        </v-container>
    </v-row>
</template>


<script >

import Chatroom from '../components/Chatroom.vue'
import { io } from 'socket.io-client';
import SocketioService from '../pages/socketio.service.js';




export default {
    data() {
        return {
            keepGenerating: localStorage.getItem('keepGenerating'),

        }

    },
    //implement socket.io
    mounted() {
        SocketioService.setupSocketConnection();
        this.getMessage(1);

    },

    components: {
        Chatroom
    },

    methods: {
        // Setup() {
        //     // Access the socket from SocketioService
        //     const socket = SocketioService.socket;
        //     console.log("started");

        //     socket.on('connection', (message) => {
        //         console.log("asd");
        //     });
        // },

        //sleep function
        sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        },


        async getMessage(num) {

            // if null
            // localStorage.setItem('keepGenerating', true);
            // this.keepGenerating = true;
            await this.sleep(1000); // Sleep for 1 second


            this.keepGeneratingStr = localStorage.getItem('keepGenerating');
            if (this.keepGeneratingStr == 'true') {
                this.keepGenerating = true;
                console.log('reconnected');
            } else {
                this.keepGenerating = false;
            }


            if (num == 0) { //from button click
                localStorage.setItem('keepGenerating', true);
                this.keepGenerating = true;
            }




            // this.keepGenerating = true;

            const socket = SocketioService.socket;

            const data1 = "Hello from client!"

            // socket.emit('chat2', data1);


            // keep emiting until stop button is pressed
            // check whether socket is connected
            // if (socket.connected) {

            // console.log("mountedddd ", this.keepGenerating);

            while (this.keepGenerating == true) {
                await this.sleep(500); // Sleep for 1 second
                console.log("calling api...")
                socket.emit('chat2', data1);
                //sleep for 1 second
                await this.sleep(5000); // Sleep for 1 second

            }

            console.log('emitted!')
        },

        stopMessage() {
            localStorage.setItem('keepGenerating', false);
            this.keepGenerating = false;

            const socket = SocketioService.socket;
            const data1 = "Stop from client!"


            socket.emit('stopGenerate', data1);

            // socket.on('my broadcast', (data) => {
            //     console.log(data);
            // });
            console.log('emitted stopppppp!')
        }
    }
}

</script>

<style></style>