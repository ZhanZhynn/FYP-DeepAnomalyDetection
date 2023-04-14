import Vue from 'vue';
import Router from 'vue-router';
import ContactUs from '../pages/ContactUs.vue';
import upload from '../pages/upload.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/ContactUs',
            name: 'ContactUs',
            component: ContactUs,
        },
        {
            path: '/upload',
            name: 'upload',
            component: upload,
        },


        {
            path: '/dummyanalyze',
            name: 'dummyanalyze',
            component: dummyanalyze,
        },
    ],
});