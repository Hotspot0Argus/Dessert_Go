import axios from 'axios'

const qs = require('qs')

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
let token = ''
axios.interceptors.request.use(
  config => {
    // 这里写死一个token，你需要在这里取到你设置好的token的值
    const token = token
    if (token) {
      config.headers.Authorization = token
    }
    return config
  },
  error => {
    return Promise.reject(error)
  })

const host = 'http://localhost:8080/api'

const $api = {
  async get (url, data) {
    try {
      let res = await axios.get(host + url, {
        params: data,
        headers: {'Authorization': token}
      })
      res = res.data
      return new Promise((resolve) => {
        if (res.status === 200) {
          resolve(res.data)
        } else {
          resolve(res.data)
        }
      })
    } catch (err) {
      console.log(err)
    }
  },
  async post (url, data) {
    try {
      let res = await axios.post(host + url, qs.stringify(data), {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Authorization': token
        }
      })
      res = res.data
      return new Promise((resolve, reject) => {
        if (res.status === 200) {
          resolve(res.data)
        } else {
          reject(res.data)
        }
      })
    } catch (err) {
      console.log(err)
    }
  },
  setToken (paToken) {
    token = paToken
  }
}
export { $api }
