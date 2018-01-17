import * as mutations from './mutation-types'

export default {
    [mutations.USER_LOGOUT](state) {
        state.user.name = '';
        state.user.id = '';
        state.user.logined = false;
    },
    [mutations.USER_LOGIN](state, user) {
        state.user.name = user.name;
        state.user.id = user.id;
        state.user.level = user.level;
        state.user.logined = true;
    },
    [mutations.SYS_CONFIG](state, sysCfg) {
        state.sysconfig.pitems = sysCfg.pitems;
    },
}
