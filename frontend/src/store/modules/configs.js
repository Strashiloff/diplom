const axios = require('axios')

export default {
  namespaced: true,
  state: {
    templates: {
      buf: {
        "postgres:12": "PostgresSQL 12",
        "mariadb:10.3": "MariaDB 10.3",
        php: "PHP",
        python: "Python",
        node: "Node JS",

      },
      listpatterns: null,
      sendpattern: null,
    }
  },
  actions: {
    getListPatterns:  async ({ commit }) => {
      let result = await axios.post('http://127.0.0.1:5000/list')
      console.log(result)
      if (result.status == 200) commit('GET_LIST_PATTERNS', result.data)
    },

    saveParam: async ({ commit }, item) => {
      let result = await axios.post('http://localhost:5000/', item)
      if (result.status == 200) commit('SAVE_PARAM')
    },
    deleteParam: async ({ state, commit }, item) => {
      console.log('item', item)
      let result = await axios.post('http://localhost:5000/delete', item)
      if (result.status == 200) commit('DELETE_PARAM')
    }
  },
  mutations: {
    GET_LIST_PATTERNS:(state, payload) => { state.templates.listpatterns = payload },
    SAVE_PARAM: (state, payload) => {  },
    DELETE_PARAM: (state, payload) => { },
  },
  getters: {
    getListPatterns: state => state.templates.listpatterns,
    // getPatterByName: state =>
    getBufName: state => (key, param) => {
      let res = state.templates.buf[param]
      if (res != undefined) return res
      if (key == 'option') {
        if (param == '') return 'нет'
        return param
      }
      if (key == 'interface') {
        if (param) return 'включен'
        return 'выключен'
      }
      return param
    },
  }
}