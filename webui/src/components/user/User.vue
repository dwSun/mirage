<template>
    <div v-if=user class="uk-panel">
        <h3 class="uk-panel-title"><i class="uk-icon-gear"></i>用户详情</h3>
        <div class='uk-panel uk-panel-box uk-panel-box-primary'>

            <h3 class="uk-panel-title">[{{ user.name }}]-{{ user.formalname }}</h3>
            <div class="uk-panel-badge">
                <button class='uk-button' data-uk-modal="{target:'#modify-one'}"><i class="uk-icon-edit"></i><span class='uk-hidden-small'>修改</span></button>
                <button v-if='user_info.name != user.name' class='uk-button' disabled="{{ user.inuse }}" @click.prevent='delOne'><i class="uk-icon-trash"></i><span class='uk-hidden-small'>删除</span></button>
            </div>

            <div class="uk-panel uk-panel-box uk-form uk-form-horizontal">
                <div class="uk-form-row">
                    <label class="uk-form-label" >用户姓名</label>
                    <div class="uk-form-controls">
                        <p>{{ user.formalname }}</p>
                    </div>
                </div>
                <div class="uk-form-row">
                    <label class="uk-form-label">用户性别</label>
                    <div class="uk-form-controls">
                        {{ user.gender|gender }}
                    </div>
                </div>
                <div class="uk-form-row">
                    <label class="uk-form-label" >描述</label>
                    <div class="uk-form-controls">
                        <p>{{ user.desc }}</p>
                    </div>
                </div>
                <div class="uk-form-row">
                    <label class="uk-form-label">用户等级</label>
                    <div class="uk-form-controls">
                        <p>{{ user.level|userlevel }}</p>
                    </div>
                </div>
                <div class="uk-form-row">
                    <label class="uk-form-label" >联系电话</label>
                    <div class="uk-form-controls">
                        <p>{{ user.phone }}</p>
                    </div>
                </div>
                <div class="uk-form-row">
                    <label class="uk-form-label" >联系地址</label>
                    <div class="uk-form-controls">
                        <p>{{ user.address }}</p>
                    </div>
                </div>
                <div class="uk-form-row">
                    <label class="uk-form-label" >EMail</label>
                    <div class="uk-form-controls">
                        <p>{{ user.email }}</p>
                    </div>
                </div>
                <div class="uk-form-row">
                    <label class="uk-form-label">隶属组</label>
                    <div class="uk-form-controls uk-form-controls-text">
                        <p v-if="!groupname">无</p>
                        <p v-if="groupname"><a v-link="{name:'group',params:{id:user.group}}">{{ groupname }}</a></p>
                    </div>
                </div>
            </div>
        </div>
        <div id="modify-one" class="uk-modal" aria-hidden="true" style="display: none; overflow-y: scroll;">
            <div class="uk-modal-dialog uk-display-block">
                <button type="button" class="uk-modal-close uk-close"></button>
                <div class="uk-modal-header">
                    <h2>修改用户</h2>
                </div>
                <form class="uk-form uk-form-horizontal">
                    <div class="uk-form-row">
                        <label class="uk-form-label" >用户姓名</label>
                        <div class="uk-form-controls">
                            <input type="text" placeholder="用户姓名" v-model="user.formalname">
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label">用户性别</label>
                        <div class="uk-form-controls">
                            <select v-model="user.gender">
                                <option value='Male'>男</option>
                                <option value='Female'>女</option>
                            </select>
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label" for="form-h-ip">用户密码</label>
                        <div class="uk-form-controls">
                            <input class='{{ passok }}' type="password" id="form-h-ip" placeholder="用户密码" v-model="user.pasd">
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label" for="form-h-ip">确认密码</label>
                        <div class="uk-form-controls">
                            <input class='{{ passok }}' type="password" id="form-h-ip" placeholder="确认密码" v-model="user.pasdre">
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label" >描述</label>
                        <div class="uk-form-controls">
                            <textarea cols="30" rows="3" placeholder="用户描述" v-model="user.desc"></textarea>
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label">用户类型</label>
                        <div class="uk-form-controls uk-form-controls-text">
                            <select v-model="user.level">
                                <option v-if="user_info.level < 10" value=0>系统管理员</option>
                                <option value=10>组管理员</option>
                                <option value=100>用户</option>
                            </select>
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label" >联系电话</label>
                        <div class="uk-form-controls">
                            <input type="text" placeholder="联系电话" v-model="user.phone">
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label" >联系地址</label>
                        <div class="uk-form-controls">
                            <input type="text" placeholder="联系地址" v-model="user.address">
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label" >EMail</label>
                        <div class="uk-form-controls">
                            <input type="text" placeholder="EMail联系地址" v-model="user.email">
                        </div>
                    </div>
                    <div v-if="user_info.level < 10" class="uk-form-row">
                        <label class="uk-form-label">隶属组</label>
                        <div class="uk-form-controls">
                            <select v-model="user.group">
                                <option v-for='group in groups' value='{{ group.id }}'>{{ group.name }}</option>
                            </select>
                        </div>
                    </div>
                </form>
                <div class="uk-modal-footer uk-text-right">
                    <button type="button" class="uk-button uk-modal-close">取消</button>
                    <button type="button" class="uk-button uk-button-primary" @click.prevent='saveModify'>保存</button>
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
        store: store,
        vuex: {
            getters
        },
        computed:{
            passok: function () {
                if (this.$data.user.pasd == this.$data.user.pasdre) {
                    return '';
                }
                return 'uk-form-danger';
            },
            groupname: function () {
                var thr = this;
                var cname = '';
                _.map(this.$data.groups,function(e){
                    if(e.id == thr.$data.user.group){
                        cname = e.name;
                    }
                });
                return cname;
            },
        },
        methods: {
            saveModify: function (e) {
                var ths = this;
                var user = $.extend({}, this.$data.user);
                user.pasd = common.sha(user.name + user.pasd)
                common.post(common.APIUsers(this.$route.params.name), user, function(response) {
                    UIkit.notify('修改完成！', {status: 'success'});
                    var modal = UIkit.modal("#modify-one");
                    if ( modal.isActive() ) {
                        modal.hide();
                    }
                    ths.getUser();
                })
            },
            getUser: function (v) {
                var ths = this;
                common.get(common.APIUsers(this.$route.params.name), function(response){
                    ths.$data.user = response.data.payload;
                    ths.$data.user.pasdre = ths.$data.user.pasd;
                    if(!ths.$data.user.group){
                        ths.$data.user.group = '';
                    }
                });
            },
            delOne: function (v) {
                var ths = this;
                common.del(common.APIUsers(this.$route.params.name), function(response) {
                    ths.$route.router.go({ path: '/users' });
                })
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
        attached: function () {
            this.getUser();
            this.getGroups();
        },
        data() {
            return {
                user: undefined,
                groups: [],
            }
        },
    }
</script>
