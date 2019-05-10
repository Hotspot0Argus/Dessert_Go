let Vue

const _setData = function (obj, key, value) {
  if (value && value.sessionState) {
    const state = value.sessionState
    delete value.sessionState
    Object.defineProperty(value, 'sessionState', {value: state, enumerable: false})
  }
  Vue.set(obj, key, value)
}

class Session {

  // ============================================================================
  // 通用

  get (name) {
    const value = this.getData(name)
    if (value.sessionState && value.sessionState === 'none') {
      return null
    }
    return value
  }

  getData (name) {
    let props = name.split('.')
    let session = this.session
    for (let i = 0; i < props.length; i++) {
      if (session[props[i]] === undefined) {
        _setData(session, props[i], {sessionState: 'none'})
        return session[props[i]]
      }

      if ((i === props.length - 1)) {
        return session[props[i]]
      }
      session = session[props[i]]
    }
    return {sessionState: 'none'}
  }

  set (name, data) {
    const props = name.split('.')
    let session = this.session
    for (let i = 0; i < props.length; i++) {
      if (i === props.length - 1) {
        return _setData(session, props[i], data)
      }
      if (session.hasOwnProperty(props[i])) {
        session = session[props[i]]
      } else {
        break
      }
    }
  }

  remove (name) {
    return this.set(name, {sessionState: 'none'})
  }
}

export default {
  SessionData: Session
}
