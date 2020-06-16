export default function () {
  return store => {
    let dispatch = store.dispatch
      
    store.subscribe((mutation, state) => {
      let payload = mutation.payload

      switch (mutation.type) {
        case 'templates/DELETE_PARAM':
          setTimeout(dispatch('templates/getListPatterns'), 1000)
          break
        case 'templates/SAVE_PARAM':
          setTimeout(dispatch('templates/getListPatterns'), 1000)
          break
      }
    })
  }
}