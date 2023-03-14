<template>
  <v-container>
    <v-row>
      <v-col cols="6">
        <v-card style="height: 24rem; align-self: center;">

          <v-card-actions class="justify-center">
            <!-- <img src="../static/icon.png" :width="250" aspect-ratio="1/1" /> -->
            <v-img src="https://blog.deemoney.com/content/images/2020/11/shutterstock_1456783511.jpg" height="200px"
              cover></v-img>
          </v-card-actions>
          <v-card-title class="justify-center">
            Financial Fraud Detection Software
          </v-card-title>
          <v-card-text class=text-center>
            100% Open Source and Free
          </v-card-text>
        </v-card>

      </v-col>
      <v-col cols="6">
        <Upload />
      </v-col>
    </v-row>

    <v-row>
      <Features />
    </v-row>




  </v-container>
</template>

<script>
import Upload from "../components/Upload.vue";
import Features from "../components/Features.vue";

export default {
  components: {
    Upload,
    Features
  }
}

</script>

<style  scoped></style>