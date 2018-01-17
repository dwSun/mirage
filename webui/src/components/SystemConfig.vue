<template>
    <div class='uk-panel'>
        <h3 class="uk-panel-title"><i class="uk-icon-gear"></i>系统设置</h3>
        <div class="uk-panel-badge">
            <button class='uk-button' @click.prevent='saveModify'><i class="uk-icon-save"></i>保存</button>
            <div class='uk-button'><i class="uk-icon-trash"></i>取消</div>
        </div>
        <br />
        <div class='uk-panel uk-panel-box'>
            <form class="uk-form uk-form-horizontal">
                <div class="uk-form-row">
                    <span class="uk-form-label">分页</span>
                    <div class="uk-form-controls uk-form-controls-text">
                        <input type="number" id="form-h-mix5" min="10" max="100" v-model="sysconfig.pitems" class="uk-form-width-small">
                        <label for="form-h-mix4">条</label>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    import * as actions from '../vuex/actions'
    import * as getters from '../vuex/getters';
    var common = require('../common/common.js');

    export default {
        vuex: {
            actions,
            getters
        },
        methods: {
            saveModify: function (e) {
                var ths = this;
                common.post(common.APISysConfig(), this.$data.sysconfig, function(response) {
                    UIkit.notify('修改完成！', {status: 'success'});
                    ths.setSysConfig(ths.$data.sysconfig);
                    ths.getSysConfig();
                });
            },
            getSysConfig: function (v) {
                var ths = this;
                common.get(common.APISysConfig(), function(response) {
                    ths.$data.sysconfig = response.data.payload;
                });
            },
        },
        attached: function () {
            this.getSysConfig();
        },
        data() {
            return {
                sysconfig: {
                    pitems: 20,
                },
            }
        },
    }
</script>
