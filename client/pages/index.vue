<template class="custom-background">
  <v-row>
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

      <br></br>

      <v-row>
        <Features />
      </v-row>

      <br></br>




    </v-container>

    <!-- <v-footer class="bg-indigo-lighten-1 text-center d-flex flex-column">

      <div class="pt-0">
        You agree to access and use the Website and any
        Products and Services in accordance with these
        Terms and all applicable laws.
        We grant You the right to access and use the
        Services via the Website. This right is non-exclusive,
        non-transferable, and subject to these Terms (which
        may be amended from time to time) and all other
        terms and conditions are expressly excluded unless
        otherwise agreed in writing.
      </div>

      <v-divider></v-divider>

      <div>
        {{ new Date().getFullYear() }} — <strong>MCS2</strong>
      </div>
    </v-footer> -->
  </v-row>
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

<style  scoped>
.custom-background {
  background-color: #F9FBE7;
  /* Replace with your desired color */
}
</style>