<template>
    <v-card class="mx-auto" max-width="344" title="User Registration" style=" width: 60rem;">
        <v-container>
            <v-form ref="form" v-model="valid" lazy-validation>

                <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>

                <v-text-field v-model="subject" :counter="25" :rules="subjectRules" label="Subject" required></v-text-field>


                <v-textarea v-model="message" :counter="250" :rules="messageRules" label="Message" required></v-textarea>


                <!-- <v-select v-model="select" :items="items" :rules="[v => !!v || 'Item is required']" label="Item"
            required></v-select> -->

                <v-checkbox v-model="checkbox" :rules="[v => !!v || 'You must agree to continue!']"
                    label="I agree to the terms and conditions" required></v-checkbox>

                <v-btn :disabled="!valid" color="success" @click="validate">
                    Submit
                </v-btn>

                <v-btn color="error" @click="reset">
                    Reset Form
                </v-btn>

                <!-- <v-btn color="warning" @click="resetValidation">
            Reset Validation
        </v-btn> -->
            </v-form>
        </v-container>
    </v-card>
</template>

<script>
export default {
    data: () => ({
        valid: true,
        subject: '',
        subjectRules: [
            v => !!v || 'Subject is required',
            v => (v && v.length <= 25) || 'Subject must be less than 25 characters'
        ],
        message: '',
        messageRules: [
            v => !!v || 'Message is required',
            v => (v && v.length <= 250) || 'Message must be less than 250 characters'
        ],
        email: '',
        emailRules: [
            v => !!v || 'E-mail is required',
            v => /.+@.+/.test(v) || 'E-mail must be valid'
        ],
        select: null,
        items: [
            'Item 1',
            'Item 2',
            'Item 3',
            'Item 4'
        ],
        checkbox: false
    }),

    methods: {
        validate() {
            if (this.$refs.form.validate()) {
                this.snackbar = true
                alert("Form Submitted")
            }
        },
        reset() {
            this.$refs.form.reset()
        },
        resetValidation() {
            this.$refs.form.resetValidation()
        }
    }
}
</script>