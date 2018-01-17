import Vue from 'vue'
import VueX from 'vuex'
import mutations from './mutations'

Vue.use(VueX)

const state = {
  logined:false,
  msgs:[],
  user:{
      name:'',
      id:'',
      logined:false
  },
  firstRun:true,
  sysconfig:{},
}

const store = new VueX.Store({
  state,
  mutations
})

if (module.hot) {
    module.hot.accept(['./mutations'], () => {
    const mutations = require('./mutations').default
    store.hotUpdate({
      mutations
    })
  })
}

export default store
