<template>
    <v-card>
        <v-card-actions class="justify-center" style="height: 24rem;">
            <div>
                <v-file-input v-model="file" label="Upload File" prepend-icon="" multiple outlined show-size counter
                    color="primary" accept="text/xlsx"></v-file-input>
                <p>accepted file: .xlsx</p>
            </div>
            <p>{{ msg }}</p>
        </v-card-actions>
    </v-card>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Ping',
    data() {
        return {
            msg: '',
        };
    },
    methods: {
        getMessage() {
            const path = 'http://localhost:5000/upload';
            axios.get(path)
                .then((res) => {
                    this.msg = res.data;
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        },
    },
    created() {
        this.getMessage();
    },
};
</script>

<style></style>