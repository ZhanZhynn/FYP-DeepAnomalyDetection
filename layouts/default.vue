<template>
  <v-app>
    <NavBar />
    <nuxt />
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


