<template>
  <Nav/>
<div class="row">
  <SlideBar/>

  <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
  <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <h1 class="h2">Urzadzenia:</h1>

    
  <!-- Default switch -->
  
    <div class="form-check form-switch">
      <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault" />
      <label class="form-check-label" for="flexSwitchCheckDefault">Automatyczne odswiezanie rekordow</label>
    </div>

  </div>
  
  <GetLivePoz/>
  </main>
</div>
</template>

<script>
import Nav from "@/components/Nav.vue"
import SlideBar from "@/components/SlideBar.vue"
import GetLivePoz from "@/components/GetLivePoz.vue"


export default {
    name: 'Panel',
    components: {
      Nav,
      SlideBar,
      GetLivePoz,
    },
  }
</script>
