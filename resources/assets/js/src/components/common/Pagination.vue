<template>
  <div class="pagination">
    <el-button class="button is-static is-small fix"><i class="fa fa-table is-icon"></i>{{ pagination.total }}</el-button>
    <el-button :disabled="page <= 1" class="button fix is-small" @click="pageChange(page - 1)">上一页</el-button>
    <a v-show="page > blockLimit / 2 + 1" class="button is-small" @click="pageChange(1)">
      <i class="fa is-icon fa-angle-double-left"></i>1</a>
    <a class="button is-small page" :class="{'is-active': block === page}" v-for="block in blocks"
       @click="pageChange(block)"><span class="active-block">{{ block }}</span></a>
    <a v-show="page < total - (blockLimit / 2) + 1" class="button is-small" @click="pageChange(total)"><i
      class="fa is-icon fa-angle-double-right"></i>{{ total }}</a>
    <el-button :disabled="page >= total" class="button fix is-small" @click="pageChange(page + 1)">下一页</el-button>

    <select @change="perPageChange" class="input fix is-small" v-model="pagination.limit">
      <option v-for="i in [10, 20, max]" :value="i">{{ i }} / 页</option>
    </select>
  </div>
</template>
<style scoped>
  .pagination {
    padding: 10px;
    justify-content: center;
    margin: 0;
    width: 100%;
    transition: opacity .1s;
    display: flex;

  }

  .button {
    margin: 1px;
    display: inline-flex;
    flex-grow: 0;
    border: none;
    box-shadow: none;
  }

  .button.is-active {
    background: #209cee;
    color: white;
  }

  .fix {
    flex-grow: 0;
    flex-basis: 100px;
  }

  .button {
    background-color: rgb(245, 245, 245);
  }

  select {
    width: auto;
  }
</style>
<script>
  export default {
    props: {
      'pagination': {type: Object},
      'blockLimit': {type: Number, default: 8},
      'max': {type: Number, default: 50}
    },
    data () {
      return {
        perPage: this.perpage
      }
    },
    computed: {
      total () {
        return parseInt(this.pagination.total / this.pagination.limit) + (parseInt(this.pagination.total % this.pagination.limit) ? 1 : 0)
      },
      page () {
        return parseInt(this.pagination.offset / this.pagination.limit) + 1
      },
      perpage () {
        return parseInt(this.pagination.limit)
      },
      blocks () {
        let start = this.page - (this.blockLimit / 2)
        if (start < 1) start = 1
        const blocks = []
        for (let i = start; i <= this.total && i < start + this.blockLimit; i++) {
          blocks.push(i)
        }

        return blocks
      }
    },
    methods: {
      pageChange (page) {
        this.$emit('pageChange', page)
      },
      perPageChange (event) {
        this.perPage = event.target.value
        this.$emit('perPageChange', parseInt(event.target.value))
      }
    }
  }
</script>
