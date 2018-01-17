<template>
    <div v-if="group" class="uk-panel">
        <h3 class="uk-panel-title"><i class="uk-icon-gear"></i>组详情</h3>
        <div class='uk-panel uk-panel-box uk-panel-box-primary'>
            <h3 class="uk-panel-title">{{ group.name }}</h3>
            <div class="uk-panel-badge">
                <button class='uk-button' data-uk-modal="{target:'#modify-one'}"><i class="uk-icon-edit"></i><span class='uk-hidden-small'>修改</span></button>
                <button class='uk-button' @click.prevent='delOne'><i class="uk-icon-trash"></i><span class='uk-hidden-small'>删除</span></button>
            </div>
            <div class="uk-panel uk-panel-box">
                <p> 描述：{{ group.desc }}</p>
                <p> 联系人： <a v-link="{name:'user',params:{name:group.contact}}">{{ group.contact }}</a></p>
            </div>
        </div>
        <div id="modify-one" class="uk-modal" aria-hidden="true" style="display: none; overflow-y: scroll;">
            <div class="uk-modal-dialog uk-display-block">
                <button type="button" class="uk-modal-close uk-close"></button>
                <div class="uk-modal-header">
                    <h2>修改组</h2>
                </div>
                <form class="uk-form uk-form-horizontal">
                    <div class="uk-form-row">
                        <label class="uk-form-label" >描述</label>
                        <div class="uk-form-controls">
                            <textarea cols="30" rows="3" placeholder="组描述" v-model="group.desc"></textarea>
                        </div>
                    </div>
                    <div class="uk-form-row">
                        <label class="uk-form-label">联系人</label>
                        <div class="uk-form-controls">
                            <select v-model="group.contact">
                                <option v-for='user in users' value='{{ user.name }}'>{{ user.formalname?user.formalname:user.name }}</option>
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
    var common = require('../../common/common.js');

    export default {
        methods: {
            saveModify: function (e) {
                var ths = this;
                common.post(common.APIGroup(this.$route.params.id), this.$data.group, function(response){
                    UIkit.notify('修改完成！', {status: 'success'});
                    var modal = UIkit.modal("#modify-one");
                    if ( modal.isActive() ) {
                        modal.hide();
                    }
                    ths.getGroup();
                });
            },
            delOne: function (v) {
                var ths = this;
                common.del(common.APIGroup(this.$route.params.id), function(response){
                    ths.$route.router.go({ path: '/groups' });
                });
            },
            getGroup: function (v) {
                var ths = this;
                common.get(common.APIGroup(this.$route.params.id), function(response) {
                    ths.$data.group = response.data.payload;
                })
            },
            getUsers: function (v) {
                var ths = this;
                common.get(common.APIUsers(), function(response){
                    ths.$data.users = response.data.payload;
                });
            },
        },
        attached: function () {
            this.getUsers();
            this.getGroup();
        },
        data() {
            return {
                users: [],
                group: undefined,
            }
        },
    }
</script>
