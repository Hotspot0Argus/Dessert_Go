<template>
  <div>
    <div id="head">
		  <h1 id="text1">Dessert GO!</h1>
	  </div>
    <table id="button" border="0">
      <tr>
        <td><router-link to="/"><el-button type="success">首页</el-button></router-link></td>
        <td><router-link to="/List_dd"><el-button type="success">订单管理</el-button></router-link></td>
        <td><router-link to="/List_cd"><el-button type="success">菜单管理</el-button></router-link></td>
        <td><router-link to="/List_yg"><el-button type="success">员工管理</el-button></router-link></td>
        <td><router-link to="/List_rz"><el-button type="success">日志管理</el-button></router-link></td>
        <td><router-link to="/system"><el-button type="success">系统信息</el-button></router-link></td>
        <td><router-link to="/other"><el-button type="success">其他</el-button></router-link></td>
      </tr>
    </table>
  </div>
</template>

<script>
  export default {

  }
</script>

<style scoped>
div#head{
  margin:0px auto;
	border:5px #803003 soild;
	width:800px;
	height:70px;
	background-image:url(../assets/back_cake.jpg);
}

h1#text1{
	margin-top:50px;
	padding-top:20px;
	top:30px;
	font-size:30px;
	color:#AAFF66;
  margin-top:0px;
	margin-left:-275px;
	z-index:1;
	filter:glow(color=#ff0000, strength=5);
	text-shadow:5px 5px 5px #FF0000;
}

table#button{
  margin:0px auto;
}
</style>
