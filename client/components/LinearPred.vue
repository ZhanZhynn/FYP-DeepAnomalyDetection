<template>
    <v-card>
        <!-- <v-card-actions class="justify-center" style="height: 24rem;">
            <div>
                <v-file-input v-model="file" label="Upload File" prepend-icon="" multiple outlined show-size counter
                    color="primary" accept="text/xlsx"></v-file-input>
                <p>accepted file: .xlsx</p>
            </div>


        </v-card-actions> -->

        <!-- <div>
            <label for="text-input">Enter some text:</label>
            <input type="text" id="text-input" v-model="text">
            <button @click="submit">Submit</button>
        </div>
        <p>{{ msg }}</p> -->

        <v-container>
            <v-form ref="form">

                <v-text-field v-model="text" label="Enter a number" required></v-text-field>
                <p>{{ msg }}</p>



                <!-- <v-textarea v-model="message" :counter="250" :rules="messageRules" label="Message" required></v-textarea> -->




                <!-- <v-select v-model="select" :items="items" :rules="[v => !!v || 'Item is required']" label="Item"
            required></v-select> -->


                <v-btn color="success" @click="submit">
                    Submit
                </v-btn>

                <v-btn color="error" @click="reset">
                    Reset Form
                </v-btn>


            </v-form>
        </v-container>

    </v-card>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Ping',
    data() {
        return {
            msg: 'No message yet',
            file: null,
            text: '',
        };
    },
    methods: {
        // getMessage() {
        //     const path = 'http://localhost:5000/upload';
        //     axios.get(path)
        //         .then((res) => {
        //             this.msg = res.data;
        //         })
        //         .catch((error) => {
        //             // eslint-disable-next-line
        //             console.error(error);
        //         });
        // },


        submit() {
            // send input to backend
            // const path = 'http://localhost:5000/upload';
            const path = '/upload';

            axios.post(path, {
                text: this.text,
            })
                .then((res) => {
                    this.msg = res.data;
                    console.log(res.data)
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
            // console.log(this.text)


        },

        getPrediction() {
            // const path = 'http://localhost:5000/upload';
            const path = '/upload';
            axios.get(path)
                .then((res) => {
                    this.msg = res.data;
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        },
        reset() {
            this.$refs.form.reset()
        },

    },
    created() {
        // this.getMessage();
    },
};
</script>

<style></style>