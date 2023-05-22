<template>
    <v-card class="mx-auto" max-width="344" title="User Registration" style=" width: 48rem;">
        <v-container>
            <v-text-field v-model="email" color="primary" label="Email" variant="underlined"></v-text-field>

            <v-text-field v-model="subject" color="primary" label="Subject" variant="underlined"></v-text-field>

            <v-text-field v-model="message" color="primary" label="Message" variant="underlined"></v-text-field>

            <!-- <v-text-field v-model="password" color="primary" label="Password" placeholder="Enter your password"
                variant="underlined"></v-text-field> -->

            <v-checkbox v-model="terms" color="secondary" label="I agree to site terms and conditions"></v-checkbox>
        </v-container>

        <v-divider></v-divider>

        <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn color="success">
                Submit

                <v-icon icon="mdi-chevron-right" end></v-icon>
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
export default {
    data: () => ({
        email: null,
        subject: null,
        message: null,
        terms: false,
    }),
}
</script>