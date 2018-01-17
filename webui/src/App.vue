<template>
    <div>
        <nav class="uk-navbar" data-uk-sticky="{animation:'uk-animation-fade'}">
            <a href="#" class="uk-navbar-brand uk-hidden-small">Mirage</a>
            <ul class="uk-navbar-nav" v-if="user_logined">
                <li v-show='user_info.level < 100'><a v-link="{ path: '/users' }">用户管理</a></li>
                <li v-show='user_info.level < 100'><a v-link="{ path: '/groups' }">组管理</a></li>
                <li v-show='user_info.level < 10'><a v-link="{ path: '/sysconfig' }">系统设置</a></li>
                <li class="uk-parent" data-uk-dropdown="" aria-haspopup="true" aria-expanded="false">
                    <a href="">功能<i class="uk-icon-caret-down"></i></a>
                    <div class="uk-dropdown uk-dropdown-navbar uk-dropdown-bottom" style="top: 40px; left: 0px;">
                        <items-menu></items-menu>
                    </div>
                </li>
            </ul>
            <div class="uk-navbar-flip">
                <ul class="uk-navbar-nav">
                    <li class="uk-parent" data-uk-dropdown>
                        <a class='uk-margin-right'>
                            <div class="uk-icon-user uk-icon-medium">
                            </div>
                        </a>
                        <div class="uk-dropdown">
                            <ul class="uk-nav uk-nav-navbar">
                                <li v-if='user_logined'><a v-link="{name:'user',params:{name:user_info.name}}">用户 [{{ user_info.name }}]</a> </li>
                                <li v-if='user_logined'><a v-link="{path:'/logout'}">注销</a></li>
                                <li v-if='!user_logined'><a v-link="{path:'/login'}">登录</a> </li>
                            </ul>
                        </div>
                    </li>
                </ul>
            </div>
        </nav>
        <br />
        <div class="uk-panel uk-panel-box uk-panel-box-hover">
            <router-view>
            </router-view>
        </div>
        <back-to-top></back-to-top>
    </div>
</template>

<script>
    var ItemsMenu = require('./components/MenuItems.vue')

    var BackToTop = require('./components/BackTop.vue')
    import store from './vuex/store.js';
    import * as actions from './vuex/actions.js'
    import * as getters from './vuex/getters.js'

    export default {
        components: {
            'back-to-top': BackToTop,
            'items-menu': ItemsMenu
        },
        methods: {
            logout: function (e) {
                this.user_logout();
            },
        },
        store: store,
        vuex: {
            actions,
            getters
        },
    }
</script>
