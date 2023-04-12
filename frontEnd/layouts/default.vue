<template>
  <v-app>
    <NavBar />
    <router-view />
    <!-- <nuxt /> -->


    <v-footer class="bg-indigo-lighten-1 text-center d-flex flex-column">

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
    </v-footer>
  </v-app>
</template>

<script>
import NavBar from "../components/NavBar.vue";

export default {
  components: {
    NavBar,
  },
  name: 'DefaultLayout',
  data() {
  },
}
</script>


