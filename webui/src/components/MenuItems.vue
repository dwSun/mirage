<template>
    <ul class="uk-nav uk-nav-navbar" v-if="user_logined">
        <li v-if='user_info.level<10'><a v-link="{ path: '/qrcode' }">Qrcode</a></li>
    </ul>
</template>

<script>
    import store from '../vuex/store';
    import * as getters from '../vuex/getters';

    export default {
        store: store,
        vuex: {
            getters
        },
    }
</script>
