var Vue = require('vue')
var VueResource = require('vue-resource');

Vue.use(VueResource);

Vue.http.options.credentials = true;
Vue.http.headers.common['SESID'] = SESID;

var common = require('../common/common.js');

import * as mutations from './mutation-types'

export const user_login = function ({dispatch},user)  {
    console.log('user_login');
    dispatch(mutations.USER_LOGIN, user);
};

export const user_logout = function ({dispatch})  {
    console.log('注销登录');
    console.log(dispatch);
    Vue.http.get(common.APILogout()).then((response) => {
        if(200 == response.data.status){
            console.log('user_logouted');
            console.log(response.data);
            if (response.data.status != 200) {
                console.log('logout error');
                console.log(response.data.msg);
            }
            dispatch(mutations.USER_LOGOUT);
            window.location='/';
        }else{
            console.log(response.data.msg);
        }
    }, (response) => {
        UIkit.notify('callfaield', {status: 'danger'});
        console.log('error');
        dispatch(mutations.USER_LOGOUT);
    });
};

export const setSysConfig = function ({dispatch},sysCfg)  {
    console.log('setSysConfig');
    dispatch(mutations.SYS_CONFIG, sysCfg);
};
