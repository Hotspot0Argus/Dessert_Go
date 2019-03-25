import axios from 'axios'

const host = 'http://localhost:8080'
const qs = require('qs')
const $api = {
  async get (url, data) {
    try {
      let res = await axios.get(host + url, {params: data})
      res = res.data
      return new Promise((resolve) => {
        if (res.code === 0) {
          resolve(res)
        } else {
          resolve(res)
        }
      })
    } catch (err) {
      console.log(err)
    }
  },
  async post (url, data) {
    try {
      let res = await axios.post(host + url, qs.stringify(data))
      res = res.data
      return new Promise((resolve, reject) => {
        if (res.code === 0) {
          resolve(res)
        } else {
          reject(res)
        }
      })
    } catch (err) {
      console.log(err)
    }
  }
}
export { $api }
