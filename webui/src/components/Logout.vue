<template>
    <div class="uk-panel">
        <p>尝试注销</p>
    </div>
</template>

<script>
    import {
        user_logout
    } from '../vuex/actions'

    export default {
        attached: function () {
            this.logout();
        },
        vuex: {
            actions: {
                logout: user_logout,
            }
        }
    }
</script>
