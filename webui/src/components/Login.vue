<template>
<div class='uk-panel'>
    <div class='uk-grid uk-grid-width-1-1'>
        <div class="uk-container uk-container-center">
            <form id='frmlogin' class="uk-form">
                <div class='uk-grid uk-grid-width-1-1 uk-grid-small' data-uk-grid-margin>
                    <label class="uk-form-label uk-text-center" for="uname">用户名:</label>
                    <input id='uname' type="text" name="uname" placeholder="User Name">
                    <br />
                    <label class="uk-form-label uk-text-center" for="upass">密码:</label>
                    <input id='upass' type="password" name="upass" placeholder="Password">
                    <input type="hidden" name="secret" placeholder="Password input">
                </div>
                <div class="uk-grid uk-grid-width-1-3">
                    <button class='uk-button' @click.prevent="login()">登录</button>
                    <button class='uk-button' @click.prevent="clr()">取消</button>
                    <button class='uk-button' @click.prevent="ver()">验证</button>
                </div>
            </form>
        </div>
        <div v-if='loginMsg' class="uk-alert uk-alert-success" data-uk-alert="">
            <p>{{ loginMsg }}</p>
            <div class="uk-progress uk-progress-striped uk-active">
                <div id='logbar' class="uk-progress-bar" style="width: 0%;">{{ loginMsg }}</div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import * as actions from '../vuex/actions'
import * as getters from '../vuex/getters';
var common = require('../common/common.js');

export default {
    data() {
        return {
            loginMsg: "",
        }
    },
    computed: {
        secret: function () {
            return 'secret code';
        }
    },
    attached: function () {
        if (this.user_logined) {
            this.goBack();
        } else {
            this.ver();
        }
    },
    methods: {
        clr: function () {
            this.messages = [];
        },
        goBack: function () {
            const redirect = decodeURIComponent(this.$route.query.redirect || '/');
            console.log(redirect);
            this.$route.router.go(redirect);
        },
        ver: function () {
            var modal = UIkit.modal.blockUI("Loading...");
            var ths = this;
            this.$http.get(common.APIUserInfo()).then((response) => {
                if (200 == response.data.status && response.data.payload) {
                    console.log('user logined ........');
                    var user = {
                        logined: true,
                        name: response.data.payload.name,
                        id: response.data.payload.id,
                        level: response.data.payload.level
                    };
                    this.user_login(user);

                    common.get(common.APISysConfig(), function(response){
                        console.log('sysconfig loaded');
                        ths.setSysConfig(response.data.payload);
                        ths.goBack();
                    });
                } else {
                    this.user_logout();
                    console.log(response.data.msg);
                    UIkit.notify('未登录用户', {
                        status: 'danger'
                    });
                }
            }, (response) => {
                UIkit.notify('callfaield', {
                    status: 'danger'
                });
                this.user_logout();
            });
            modal.hide();
        },
        login: function () {
            var loginData =$('#frmlogin').serializeObject();
            console.log(loginData);
            if(!loginData['uname'] && ! loginData['upass']){
                UIkit.notify('用户名和密码不能为空', {status: 'warning'});
                return;
            }
            var ths = this;


            loginData['upass'] = common.sha(loginData['uname'] + loginData['upass'])

            common.post(common.APILogin(), loginData, function (response) {
                if (response.data.status == 200) {
                    var count = 0;
                    ths.ver();
                    if(ths.$route.params.redirect){
                        ths.goBack();
                    }
                } else {
                    ths.$data.loginMsg = data.msg;
                }
            });
        }
    },
    vuex: {
        actions,
        getters
    }
}
</script>
