// modules
import modul from './modules/configs'
// plugins
import plugin from './plugins/plugin'
import loggerPlugin from './plugins/logger'



export default ({
  strict: true,
  modules: {
    templates: modul,
  },
  plugins: [
    plugin (),
    loggerPlugin()
  ]
})
