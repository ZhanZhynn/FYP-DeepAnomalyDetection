<template>
    <div>
        <v-toolbar elevation="0">
            <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->

            <div style="width:9rem;">
                <h1>
                    <!-- <a href="/" style="text-decoration: none; color: black">MCS2</a> -->
                    <router-link to="/" style="text-decoration: none; color: black">MSC2</router-link>
                </h1>
            </div>

            <!-- <v-spacer></v-spacer> -->
            <v-toolbar-items>
                <v-btn text v-for="item in menuItems" :key="item.title" :to="item.path">
                    {{ item.title }}
                </v-btn>
                <!-- <v-icon>{{ item.icon }}</v-icon> -->

                <!-- 
                <router-link tag="v-btn" v-for="item in menuItems" :key="item.title" :to="item.path">
                    {{ item.title }}
                </router-link> -->

            </v-toolbar-items>
        </v-toolbar>
    </div>
</template>

<script>
import { RouterLink } from 'vue-router';

export default {
    data() {
        return {
            menuItems: [
                // { title: "DummyAnalyze", path: "/dummyanalyze", icon: "mdi-home" },
                { title: "Analyse", path: "/upload", icon: "mdi-home" },
                // { title: 'Features', path: '/index1', icon: 'mdi-home' },
                { title: "Support", path: "/contactus", icon: "mdi-magnify-heart" },
                { title: "Change Log", path: "/changelog", icon: "mdi-dots-vertical" },
                { title: "Live Chat", path: "/chat", icon: "mdi-dots-vertical" }

            ]
        };
    },
    components: { RouterLink }
};

</script>

<style scoped>
h5 {
    color: #c0c0c0;
}

.nav-bar {
    border: 2px solid #ffffff;
    background-color: #535353;
}

.nav-bar__v-btn--function-key {
    height: 90%;
    width: 90%;
}

.nav-bar__v-btn--simulator {
    height: 90%;
    width: 80%;
}

.nav-bar__v-chip--plc {
    width: 70%;
    min-width: fit-content;
}

.nav-bar__tvm {
    height: 90%;
    width: 40%;
    margin: auto;
}

.nav-bar__operation {
    height: 90%;
    width: 90%;
    margin: auto;
}

.nav-bar__cutterhead {
    height: 90%;
    width: 100%;
    margin: auto;
}

.nav-bar__ring {
    height: 80%;
    width: 10%;
    margin: auto;
}

.nav-bar__date-time {
    color: #000000;
}

.text-decoration--none {
    text-decoration: none;
}
</style>