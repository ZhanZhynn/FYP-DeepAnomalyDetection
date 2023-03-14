<template>
    <div>
        <v-toolbar elevation="0">
            <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->

            <h1><a href="/" style="text-decoration: none; color: black">App Name</a></h1>

            <v-spacer></v-spacer>
            <v-toolbar-items>
                <v-btn text v-for="item in menuItems" :key="item.title" :to="item.path">
                    <v-icon>{{ item.icon }}</v-icon>
                    {{ item.title }}
                </v-btn>
            </v-toolbar-items>
        </v-toolbar>
    </div>
</template>

<script>
export default {
    data() {
        return {
            menuItems: [
                { title: 'Home', path: '/index1', icon: 'mdi-magnify' },
                { title: 'Sign Up', path: '/signup', icon: 'mdi-magnify-heart' },
                { title: 'Sign In', path: '/signin', icon: 'mdi-dots-vertical' }
            ]
        }
    },
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