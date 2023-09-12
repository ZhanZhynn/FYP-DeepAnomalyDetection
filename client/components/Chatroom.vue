<template>
    <v-container>

        <!-- center contact in v-card -->
        <v-card class="pa-2" outlined height="500px">
            <!-- 
            <div v-for="(fact, index) in messages" :key="index">
                {{ fact }}
            </div> -->

            <v-virtual-scroll :items="messages" height="500px" item-height="20px">
                <template v-slot:default="{ item }">
                    {{ item }}
                </template>
            </v-virtual-scroll>


        </v-card>
    </v-container>
</template>

<script>
import SocketioService from '../pages/socketio.service.js';

export default {
    data() {
        return {
            messages: [],
        };
    },

    mounted() {
        SocketioService.setupSocketConnection();
        const socket = SocketioService.socket;

        socket.on('chat1response', (data) => {
            // Assuming 'data' is a single message string received from the server
            this.messages.push(data.message);
        });

    },
    //implement socket.io
    created() {
        // SocketioService.setupSocketConnection();
        SocketioService.setupSocketConnection();
        // socket.on('chat1Response', this.handleChat1Response);
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

        getMessage1() {
            const socket = SocketioService.socket;

            const data = "Hello from client!"
            // socket.emit('chat2', data);
            // SocketioService.sendToFastAPI();


            // socket.on('my broadcast', (data) => {
            //     console.log(data);
            // });

            console.log('emitt1111ed!')
            //get the responded data from socketio
            //
            // const data = "Hello from client!"

            // socket.on('chat1response', this.handleChat1Response);
            // this.messages.push('asd');


        },

        handleChat1Response(data) {
            console.log("hehehehe " + data.message);
            // Add the received message to the messages array
            // const textData = new TextDecoder('utf-8').decode(data);
            this.messages.push(data.message);
        },
    },

    destroyed() {
        // Remove Socket.IO event listeners when the component is destroyed
        // this.$socket.off('chat1Response', this.handleChat1Response);
        // Remove other event listeners if needed
        // this.$socket.off('anotherEvent', this.handleAnotherEvent);
    },
}

</script>