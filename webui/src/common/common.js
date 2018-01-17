var Vue = require('vue');
var VueResource = require('vue-resource');

Vue.use(VueResource);

Vue.http.options.credentials = true;
Vue.http.headers.common['SESID'] = SESID;

//var APIRoot = '/api/';
var APIRoot = '//127.0.0.1:5000/api/'
var siteTitle = 'Mirage';
var siteTitleShort = 'Mirage';

export var APILogin = function () {
    return APIRoot + 'login/';
}

export var APILogout = function () {
    return APIRoot + 'logout/';
}

export var APIUserInfo = function () {
    return APIRoot + 'user/';
}


export var APIUsers = function (name) {
    if(name)
        return APIRoot + 'users/'+name+'/';
    else {
        return APIRoot + 'users/';
    }
}

export var APIGroup = function (id) {
    if(id)
        return APIRoot + 'group/'+id+'/';
    else {
        return APIRoot + 'group/';
    }
}

export var APISysConfig = function () {
    return APIRoot + 'sysconfig/';
}

$.fn.serializeObject = function () {
    var o = {};
    var a = this.serializeArray();
    $.each(a, function () {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
}

export var get = function(url, action){
    Vue.http.get(url).then((response) => {
        if(200 == response.data.status && response.data.payload){
            action(response);
        }else{
            UIkit.notify(response.data.msg, {status: 'danger'});
        }
    }, (response) => {
        UIkit.notify('callfaield', {status: 'danger'});
    });
}

export var del = function(url, action){
    Vue.http.delete(url).then((response) => {
        if(200 == response.data.status && response.data.payload){
            action(response);
        }else{
            UIkit.notify(response.data.msg, {status: 'danger'});
        }
    }, (response) => {
        UIkit.notify('callfaield', {status: 'danger'});
    });
}

export var post = function(url, data, action){
    Vue.http.post(url, data).then((response) => {
        if(200 == response.data.status && response.data.payload){
            action(response);
        }else{
            UIkit.notify(response.data.msg, {status: 'danger'});
        }
    }, (response) => {
        UIkit.notify('callfaield', {status: 'danger'});
    });
}

export var put = function(url, data, action){
    Vue.http.put(url, data).then((response) => {
        if(200 == response.data.status && response.data.payload){
            action(response);
        }else{
            UIkit.notify(response.data.msg, {status: 'danger'});
        }
    }, (response) => {
        UIkit.notify('callfaield', {status: 'danger'});
    });
}

export var sha = function(text) {
    var shaObj = new jsSHA("SHA-256", "TEXT");
    shaObj.update(text);
    return shaObj.getHash('B64');
}

/*
$(function(){
    $("body").on("click", "div.uk-button", function(){
        UIkit.notify('功能暂未实现！');
    });
})
*/
