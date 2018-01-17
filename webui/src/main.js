var Vue = require('vue')
var VueRouter = require('vue-router')
var VueResource = require('vue-resource');

Vue.use(VueRouter)
Vue.use(VueResource);

Vue.http.options.credentials = true;
Vue.http.headers.common['SESID'] = SESID;

var App = require('./App.vue')

import configRouter from './routers';
import store from './vuex/store.js'
import { user_logined } from './vuex/getters'
import { user_info } from './vuex/getters'
import { user_login } from './vuex/actions'

Vue.filter('userlevel', function (value) {
    if(value < 10)
        return '系统管理员';
    if(value < 100)
        return '组管理员';
    return '用户';
})

Vue.filter('gender', function (value) {
    var gender = {
        "Male": "男",
        "Female": "女",
    };
    return gender[value];
})

var router = new VueRouter()
router.beforeEach(function (transition) {
    //user_login(store);
    document.body.scrollTop = 0;
    if (transition.to.auth) {
        if (!user_logined(store.state)) {
            console.log('not logined');
            const redirect = encodeURIComponent(transition.to.path);
            transition.redirect({
                name: 'login',
                query: {
                    redirect
                }
            });
        }
        if (transition.to.level) {
            if (user_info(store.state).level >= transition.to.level) {
                UIkit.notify('您无权查看该页面', {
                    status: 'warning'
                });
                transition.abort();
            }
        }
    }
    transition.next();
})

configRouter(router);

router.start(Vue.extend(App), '#app')
