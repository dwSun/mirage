<template>
    <div class="uk-panel">
        <h3 class="uk-panel-title"><i class="uk-icon-gear"></i>组列表</h3>
        <div class="uk-panel-badge">
            <button class='uk-button' data-uk-modal="{target:'#create-one'}"><i class="uk-icon-file"></i><span class='uk-hidden-small'>新增</span></button>
        </div>
        <br />
        <div v-for="msg in messages" class="uk-alert uk-alert-danger" data-uk-alert="">
            <a href="#" class="uk-alert-close uk-close"></a>
            <p>{{ msg }}</p>
        </div>

        <ul v-if="groups.length != 0" class="uk-grid uk-grid-small uk-grid-width-large-1-2 uk-grid-width-small-1-1 uk-grid-width-medium-1-2" data-uk-grid-margin data-uk-grid-match="{target:'.uk-panel'}">
            <li v-for='group in groups' class="uk-panel">
                <div class='uk-panel uk-panel-box uk-panel-box-primary'>
                    <h3 class="uk-panel-title">{{ group.name }}</h3>
                    <div class="uk-panel-badge">
                        <a class='uk-button' v-link="{name:'group',params:{id:group.id}}"><i class="uk-icon-info-circle"></i><span class='uk-hidden-small'>详情</span></a>
                    </div>
                    <div> 描述：{{ group.desc }}</div>
                    <div> 用户数量：{{ group.users }}</div>
                </div>
            </li>
        </ul>
        <div v-if="groups.length == 0" class="uk-text-center">
            <h3><i class="uk-icon-spinner uk-icon-spin"></i>loading...</h3>
        </div>
        <div id="create-one" class="uk-modal" aria-hidden="true" style="display: none; overflow-y: scroll;">
            <div class="uk-modal-dialog uk-display-block">
                <button type="button" class="uk-modal-close uk-close"></button>
                <div class="uk-modal-header">
                    <h2>新建组</h2>
                </div>
                <form class="uk-form uk-form-horizontal">
                    <div class="uk-form-row">
                        <span class="uk-form-label">组名</span>
                        <div class="uk-form-controls">
                            <input type="text" placeholder="组名称" v-model="newGroup.name" title="系统内唯一的组名">
                            <button class='uk-button' @click.prevent='check'>检查</button>
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label" >描述</label>
                        <div class="uk-form-controls">
                            <textarea cols="30" rows="3" placeholder="组描述" v-model="newGroup.desc"></textarea>
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label">联系人</label>
                        <div class="uk-form-controls">
                            <select v-model="newGroup.contact">
                                <option v-for='user in users' value='{{ user.name }}'>{{ user.formalname?user.formalname:user.name }}</option>
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
                newGroup:{
                    name:'',
                    contact:'',
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
                this.$http.get(common.APIGroup(this.$data.newGroup.name)).then((response) => {
                    if(200 == response.data.status && response.data.payload){
                        UIkit.notify('组名 已经存在', {status: 'warning'});
                    }else{
                        UIkit.notify('组名 可以使用', {status: 'success'});
                    }
                }, (response) => {
                    UIkit.notify('callfaield', {status: 'warning'});
                });
            },
            saveNew: function (e) {
                var ths = this;
                common.put(common.APIGroup(),this.$data.newGroup, function(response){
                    UIkit.notify('新组已添加！', {status: 'success'});
                    var modal = UIkit.modal("#create-one");
                    if(modal.isActive()){
                        modal.hide();
                    }
                    ths.getGroups();
                });
            },
            getUsers: function (v) {
                var ths = this;
                common.get(common.APIUsers(), function(response){
                    ths.$data.users = response.data.payload;
                });
            },
            getGroups: function (v) {
                var ths = this;
                common.get(common.APIGroup(), function(response){
                    ths.$data.groups = response.data.payload;
                });
            },
        },
        attached: function () {
            this.getUsers();
            this.getGroups();
        },
    }
</script>
