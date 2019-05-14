/* eslint-disable */
import FlexTableSelection from './FlexTableSelection.vue'

export default {
  components: {FlexTableSelection},
  props: {
    dataset: {
      default: function () {
        return []
      }
    },
    columns: {
      type: Array
    },
    height: {
      default: 0
    },
    fixedHeader: {
      type: Boolean,
      default: true
    }
  },
  mounted () {
    this.rows = []
    this.dataset.length && this.dataset.forEach((data, index) => {
      this.rows.push({
        data: data,
        active: false,
        index: index
      })
    })
  },
  watch: {
    dataset (dataset) {
      this.rows = []
      this.selectAll = false
      dataset.length && dataset.forEach((data, index) => {
        this.rows.push({
          data: data,
          active: false,
          index: index,
          show: data._show && true
        })
      })
    }
  },
  data () {
    return {
      rows: [],
      selectAll: false
    }
  },
  render (h) {
    return (
      <div class="flex-table">
        <div class={{'flex-table-head-wrapper': true, 'auto-height': this.height === 'auto'}} ref={'flex-table-head-wrapper-' + this.uniqId}>
          <div class={{'flex-table-row flex-table-head': true, 'is-active': this.selectAll}}>
            {
              this.columns.length && this._l(this.columns, (column, $index) =>
                <div class={{'flex-table-cell-wrapper': true, 'fixwidth': column.fixWidth}}
                     style={{
                       'width': column.width + 'px',
                       'justify-content': (column.align)
                     }}>
                  {
                    column.type === 'selection'
                      ? (
                        <div class="flex-table-cell "
                             on-click={($event) => this.toggleAllSelection($event)}>
                          <flex-table-selection></flex-table-selection>
                        </div>)
                      : (
                        <div class={{'flex-table-cell': !column.customHeader}}>
                          {column.renderHeader()}
                        </div>)
                  }
                </div>
              )
            }
          </div>
        </div>
        <div class={{'flex-table-body-wrapper': true, 'auto-height': this.height === 'auto'}} style={{'max-height': this.height ? this.height : 'auto'}}
             on-scroll={($event) => this.handleBodyScroll($event)}>
          <div class="flex-table-body">
            {
              !this.rows.length
                ? (
                  <div class="card-content">
                    <span class="tag is-fullwidth">无记录</span>
                  </div>
                )
                : this._l(this.rows, (row, $rindex) =>
                  <div style={{'is-hidden': !row._show}} class={this.getRowClass(row)} key={"r" + row.data._id ? row.data._id : Math.random()}>
                    {
                      this._l(this.columns, (column, $cindex) =>
                        <div class={{
                          'flex-table-cell-wrapper': true,
                          'oneline': (column.oneline !== false) && true,
                          'fixwidth': column.fixWidth
                        }} style={{
                          'width': column.width + 'px',
                          'justify-content': (column.align)
                        }}>
                          {
                            column.type === 'selection'
                              ? (
                                <div class="flex-table-cell"
                                     on-click={($event) => this.handleRowClick($event, row)}>
                                  <flex-table-selection></flex-table-selection>
                                </div>)
                              : (
                                <div class="flex-table-cell">
                                  {column.type === 'index' ? ($rindex + 1) : column.renderCell(row)}
                                </div>)
                          }
                        </div>
                      )
                    }
                  </div>
                )
            }
          </div>
        </div>
      </div>
    )
  },
  methods: {
    addColumn (column) {
      this.columns.push(column)
    },
    getRowClass (row) {
      return 'flex-table-row ' + (row.active ? 'is-active' : '')
    },
    handleRowClick ($event, row) {
      row.active = !row.active
      this.selectAll = this.rows.reduce(((ret, row) => row.active && ret), true)
      this.$parent.selectionChange(this.rows.filter(row => row.active).map(row => row.data))
      $event && $event.preventDefault()
      return false
    },
    toggleSelection (item) {
      const row = _.find(this.rows, {'data': item})
      this.handleRowClick(null, row)
    },
    toggleAllSelection () {
      this.selectAll = !this.selectAll
      this.rows.forEach(row => row.active = this.selectAll)
      this.$parent.selectionChange(this.rows.filter(row => row.active).map(row => row.data))
    },
    handleBodyScroll ($event) {
      this.$refs['flex-table-head-wrapper-' + this.uniqId].scrollLeft = $event.target.scrollLeft
    }
  }
}
