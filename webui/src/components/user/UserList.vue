<template>
    <div class="uk-panel">
        <h3 class="uk-panel-title"><i class="uk-icon-gear"></i>用户列表</h3>
        <div class="uk-panel-badge">
            <button class='uk-button' data-uk-modal="{target:'#create-one'}" @click.prevent='getGroups'><i class="uk-icon-file"></i><span class='uk-hidden-small'>新增</span></button>
        </div>
        <br />
        <ul v-if="users.length != 0" class="uk-grid uk-grid-small uk-grid-width-large-1-2 uk-grid-width-small-1-1 uk-grid-width-medium-1-2" data-uk-grid-margin data-uk-grid-match="{target:'.uk-panel'}">
            <li v-for='user in users' class="uk-panel">
                <div class='uk-panel uk-panel-box uk-panel-box-primary'>
                    <h3 class="uk-panel-title">{{ user.name }}</h3>
                    <div class="uk-panel-badge">
                        <a class='uk-button' v-link="{name:'user',params:{name:user.name}}"><i class="uk-icon-info-circle"></i><span class='uk-hidden-small'>详情</span></a>
                    </div>
                    <div class="uk-grid uk-grid-small uk-grid-width-1-2">
                        <p> 姓名：{{ user.formalname }}</p>
                        <p> 等级：{{ user.level | userlevel }}</p>
                    </div>
                    <div class="uk-grid uk-grid-small uk-grid-width-1-2">
                        <p> 描述：{{ user.desc }}</p>
                        <p v-if="user_info.level < 10"> 隶属组：
                            <a v-if="user.group" v-link="{name:'group',params:{id:user.group}}">
                                {{ user.groupname }}
                            </a>
                            <span v-else>无</span>
                        </p>
                    </div>
                </div>
            </li>
        </ul>
        <div v-if="users.length == 0" class="uk-text-center">
            <h3><i class="uk-icon-spinner uk-icon-spin"></i>loading...</h3>
        </div>
        <div id="create-one" class="uk-modal" aria-hidden="true" style="display: none; overflow-y: scroll;">
            <div class="uk-modal-dialog uk-display-block">
                <button type="button" class="uk-modal-close uk-close"></button>
                <div class="uk-modal-header">
                    <h2>新建用户</h2>
                </div>
                <form class="uk-form uk-form-horizontal">
                    <div class="uk-form-row">
                        <span class="uk-form-label">用户名</span>
                        <div class="uk-form-controls">
                            <input type="text" placeholder="用户名称" v-model="newUser.name" title="系统内唯一的用户名，同时也是登录名">
                            <div class='uk-button' @click.prevent='check'>检查</div>
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label" >用户姓名</label>
                        <div class="uk-form-controls">
                            <input type="text" placeholder="用户姓名" v-model="newUser.formalname">
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label">用户性别</label>
                        <div class="uk-form-controls">
                            <select v-model="newUser.gender">
                                <option value='Male'>男</option>
                                <option value='Female'>女</option>
                            </select>
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label" for="form-h-ip">用户密码</label>
                        <div class="uk-form-controls">
                            <input class='{{ passok }}' type="password" id="form-h-ip" placeholder="用户密码" v-model="newUser.pasd">
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label" for="form-h-ip">确认密码</label>
                        <div class="uk-form-controls">
                            <input class='{{ passok }}' type="password" id="form-h-ip" placeholder="确认密码" v-model="newUser.pasdre">
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label" >描述</label>
                        <div class="uk-form-controls">
                            <textarea cols="30" rows="3" placeholder="用户描述" v-model="newUser.desc"></textarea>
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label">用户类型</label>
                        <div class="uk-form-controls uk-form-controls-text">
                            <select v-model="newUser.level">
                                <option v-if="user_info.level<10" value=0>系统管理员</option>
                                <option v-if="user_info.level<10" value=10>组管理员</option>
                                <option value=100>用户</option>
                            </select>
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label" >联系电话</label>
                        <div class="uk-form-controls">
                            <input type="text" placeholder="联系电话" v-model="newUser.phone">
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label" >联系地址</label>
                        <div class="uk-form-controls">
                            <input type="text" placeholder="联系地址" v-model="newUser.address">
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label" >EMail</label>
                        <div class="uk-form-controls">
                            <input class='{{ emailok }}' type="text" placeholder="EMail联系地址" v-model="newUser.email">
                        </div>
                    </div>
                    <div v-if="user_info.level<10" class="uk-form-row">
                        <label class="uk-form-label">隶属组</label>
                        <div class="uk-form-controls">
                            <select v-model="newUser.group">
                                <option v-for='group in groups' value='{{ group.id }}'>{{ group.name }}</option>
                            </select>
                        </div>
                    </div>
                </form>
                <div class="uk-modal-footer uk-text-right">
                    <button type="button" class="uk-button uk-modal-close">取消</button>
                    <button type="button" class="uk-button uk-button-primary" @click.prevent='saveNew'>保存</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import store from '../../vuex/store';
    import * as getters from '../../vuex/getters';
    var common = require('../../common/common.js');

    export default {
        data() {
            return {
                newUser:{
                    name:'',
                    pasd:'',
                    level:100,
                    formalname:'',
                    phone:'',
                    address:'',
                    gender: 'Male',
                    email:'',
                    desc:'',
                },
                users: [],
                groups: [],
            }
        },
        store: store,
        vuex: {
            getters
        },
        methods: {
            check: function (e) {
                this.$http.get(common.APIUsers(this.$data.newUser.name)).then((response) => {
                    if(200 == response.data.status && response.data.payload){
                        UIkit.notify('用户名 已经存在', {status: 'warning'});
                    }else{
                        UIkit.notify('用户名 可以使用', {status: 'success'});
                    }
                }, (response) => {
                    UIkit.notify('callfaield', {status: 'warning'});
                });
            },
            saveNew: function (e) {
                var ths = this;
                var user = $.extend({}, this.$data.newUser);
                user.pasd = common.sha(user.name + user.pasd)
                common.put(common.APIUsers(), user, function() {
                    UIkit.notify('新用户已添加！', {status: 'success'});
                    var modal = UIkit.modal("#create-one");
                    if ( modal.isActive() ) {
                        modal.hide();
                    }
                    ths.getUsers();
                });
            },
            getUsers: function (v) {
                var ths = this;
                common.get(common.APIUsers(), function(response) {
                    ths.$data.users = response.data.payload;
                });
            },
            getGroups: function (v) {
                if(this.user_info.level<10){
                    var ths = this;
                    common.get(common.APIGroup(), function(response) {
                        ths.$data.groups = response.data.payload;
                    });
                }
            },
        },
        computed:{
            passok: function () {
                if (this.$data.newUser.pasd == this.$data.newUser.pasdre) {
                    return '';
                }
                return 'uk-form-danger';
            },
        },
        attached: function () {
            this.getUsers();
        },
    }
</script>
