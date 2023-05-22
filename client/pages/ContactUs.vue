<template>
    <v-row>
        <v-container>

            <v-row class="text-center mt-5 mb-10" align="center" justify="center">
                <h1>Got questions?
                    <br>
                    We'll help.
                </h1>
            </v-row>


            <v-row class="mb-10" justify="center" align="center">
                <!-- <v-card class="justify-center" style="height: 24rem; width: 48rem;"> -->
                <!-- <Enquiry2 /> -->
                <ContactCard />
                <!-- </v-card> -->
            </v-row>


            <v-row class="mb-10 mx-auto">
                <h2>FAQ</h2>
                <!-- <v-card class="justify-center" style="height: 24rem; width: 48rem;"> -->
                <!-- <Enquiry2 /> -->
                <FAQpanel />
                <!-- </v-card> -->
            </v-row>
        </v-container>




    </v-row>
</template>

<script>
import Enquiry2 from "../components/Enquiry2.vue";
import ContactCard from "../components/ContactCard.vue";
import FAQpanel from "../components/FAQpanel.vue";

export default {
    components: {
        Enquiry2,
        ContactCard,
        FAQpanel
    }
}

</script>

<style></style>