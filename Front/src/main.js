import './assets/main.css'
import { createApp } from 'vue'
import store from './store/index.js'
import PrimeVue from 'primevue/config';

import App from './App.vue'
import router from './router/index.js'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

const app = createApp(App)

app.use(router)
app.use(store)
app.use(PrimeVue)


app.mount('#app')
