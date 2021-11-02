<template>
  <Claim/>
</template>

<script>
import Claim from '../components/Claim.vue'

export default {
    name: "Home",
    components: {
      Claim
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Montserrat:300,400,600,800');
.wrapper{
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-family: 'Montserrat', sans-serif;
  margin: 0;
  padding: 0;
  margin: 0;
  position: relative;
  width: 100%;
  min-height: 100vh;
  padding: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

</style>