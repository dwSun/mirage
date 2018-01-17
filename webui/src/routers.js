export default (router) => router.map({
    '/': {
        auth: true,
        component: function (resolve) {
            require(['./components/Home.vue'], resolve)
        }
    },
    '/login': {
        name: 'login',
        component: function (resolve) {
            require(['./components/Login.vue'], resolve)
        }
    },
    '/logout': {
        auth: true,
        component: function (resolve) {
            require(['./components/Logout.vue'], resolve)
        }
    },
    '/users': {
        auth: true,
        level:100,
        component: function (resolve) {
            require(['./components/user/UserList.vue'], resolve)
        }
    },
    '/user/:name': {
        auth: true,
        name: 'user',
        component: function (resolve) {
            require(['./components/user/User.vue'], resolve)
        }
    },
    '/groups': {
        auth: true,
        level: 10,
        component: function (resolve) {
            require(['./components/group/GroupList.vue'], resolve)
        }
    },
    '/group/:id': {
        auth: true,
        name: 'group',
        level: 10,
        component: function (resolve) {
            require(['./components/group/Group.vue'], resolve)
        }
    },
    '/sysconfig': {
        auth: true,
        level: 10,
        component: function (resolve) {
            require(['./components/SystemConfig.vue'], resolve)
        }
    },
    '/qrcode': {
        auth: true,
        level: 10,
        component: function (resolve) {
            require(['./components/component/Qrcode.vue'], resolve)
        }
    },
})
