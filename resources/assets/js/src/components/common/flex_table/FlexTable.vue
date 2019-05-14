<template>
  <div class="flex-table-wrapper">
    <data-table
      :ref="'flex-table-' + uniqId"
      :dataset="dataset"
      :columns="columns"
      :height="height"
      :fixedHeader="fixedHeader"></data-table>
    <div v-show="false">
      <slot></slot>
    </div>
  </div>
</template>
<script>
  import DataTable from './FlexTable.js'

  export default {
    mounted () {
      this.addColumnDown = true
    },
    components: {DataTable},
    props: ['dataset', 'height', 'fixedHeader'],
    data () {
      return {
        _columns: [],
        columns: [],
        addColumnDown: false
      }
    },
    methods: {
      selectionChange (selectedData) {
        this.$emit('selection-change', selectedData)
      },
      toggleSelection (item) {
        this.$refs['flex-table-' + this.uniqId].toggleSelection(item)
      },
      addColumn (column) {
        if (!this.addColumnDown) this.columns.push(column)
      }
    }
  }
</script>
