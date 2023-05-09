<template>
    <v-card>
        <v-container>
            <v-card-actions class="justify-center" style="height: 20rem;">
                <div>
                    <!-- <v-file-input v-model="file" label="Upload File" prepend-icon="" multiple outlined show-size counter
                    color="primary" accept="text/xlsx" name='file' @change="onFileSelected"></v-file-input> -->
                    <!-- <input type="file" ref="fileInput" @change="onFileSelected"> -->
                    <input class='file-input' type='file' name='file' accept='text/csv' @change="onFileSelected" />

                    <p>accepted file: .csv</p>
                    <div v-if="errorMessage" style="color: red;">{{ errorMessage }}</div>
                    <div>
                        <v-btn color="success" @click="submit" :disabled="isSubmitDisabled">
                            Submit
                        </v-btn>
                        <v-btn color="success" @click="getPrediction" :disabled="isDownloadDisabled">
                            Download File
                        </v-btn>
                    </div>
                </div>

                <!-- Add a table to show prediction result -->
                <!-- <v-simple-table>
                <template v-slot:default>
                    <thead>
                        <tr>
                            <th class="text-left">Prediction</th>
                            <th class="text-left">Probability</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in msg">
                            <td>{{ item[0] }}</td>
                            <td>{{ item[1] }}</td>
                        </tr>
                    </tbody>
                </template>
            </v-simple-table> -->

            </v-card-actions>

            <p>{{ msg }}</p>
            <p>{{ metrics }}</p>
            <p v-if="!isDownloadDisabled">File ready. Please download the excel file for more details.</p>


        </v-container>

    </v-card>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Ping',
    data() {
        return {
            msg: 'No file found. Please upload a csv file.',
            file: null,
            text: '',
            isDownloadDisabled: true,
            isSubmitDisabled: true,
            errorMessage: '',
            metrics: '',

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
        onFileSelected(event) {
            this.file = event.target.files[0]
            console.log(this.file)
            if (this.file.type !== 'text/csv') {
                this.errorMessage = 'Please select a CSV file.'
                this.file == null
                this.isSubmitDisabled = true;
                this.isDownloadDisabled = true;
                return
            }
            if (this.file == null) {
                this.isSubmitDisabled = true;
                this.isDownloadDisabled = true;
                this.file = null;
                this.errorMessage = 'Please upload a CSV file.';

            } else {
                this.isSubmitDisabled = false;
                this.isDownloadDisabled = true;
                this.errorMessage = '';

            }

        },


        submit() {
            // send input to backend
            this.isDownloadDisabled = true;   //disable download button
            this.msg = 'Processing...'
            this.metrics = ''
            const path = 'http://localhost:5000/upload';
            const formData = new FormData()
            console.log(this.file)
            formData.append('file', this.file)
            axios.post(path, formData, {
                // text: this.text,
                headers: {
                    'Content-Type': 'multipart/form-data'
                    // responseType: 'blob'
                    // responseType: 'arraybuffer'
                }
            })
                .then((res) => {
                    // this.msg = res.data.message;
                    // console.log(res.data)

                    // Create a URL for the blob response and download it
                    // const url = window.URL.createObjectURL(new Blob([res.data]));
                    // const link = document.createElement('a');
                    // link.href = url;
                    // link.setAttribute('download', 'excel_file.csv');
                    // document.body.appendChild(link);
                    // link.click();

                    this.msg = res.data.message;
                    this.metrics = res.data.metrics;

                    this.isDownloadDisabled = false;   //can download file now

                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
            // console.log(this.text)

        },

        getPrediction() {
            const path = 'http://localhost:5000/upload';
            axios({
                method: 'get',
                url: path,
                responseType: 'blob'
            })
                .then((res) => {
                    const url = window.URL.createObjectURL(new Blob([res.data]));
                    const link = document.createElement('a');
                    link.href = url;
                    link.setAttribute('download', 'excel_file.csv');
                    document.body.appendChild(link);
                    link.click();

                    // Handle the message
                    const message = response.data.message;
                    alert(message);
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        },

    },
    created() {
        // this.getMessage();
    },
};
</script>

<style></style>