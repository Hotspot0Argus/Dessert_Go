<script>
  export default {
    props: {
      width: {
        default: 100
      },
      fixWidth: {
        type: Boolean,
        default: true
      },
      prop: {},
      label: {
        type: String
      },
      type: {
        type: String
      },
      align: {
        type: String,
        default: 'left'
      },
      oneline: {
        type: Boolean,
        default: false
      },
      customHeader: {
        type: Boolean,
        default: false
      }
    },
    created () {
      this.$options.render = h => h('div', this.$slots.default)
      this.$parent.addColumn({
        renderHeader: () => {
          return this.$slots.header ? this.$slots.header : this.label
        },
        renderCell: (row) => {
          return this.$scopedSlots.default ? this.$scopedSlots.default(row) : row.data[this.prop]
        },
        width: this.type === 'selection' ? '54' : this.width,
        prop: this.prop,
        label: this.label,
        type: this.type,
        align: this.align,
        oneline: this.oneline,
        fixWidth: this.fixWidth,
        customHeader: this.customHeader
      })
    }
  }
</script>
