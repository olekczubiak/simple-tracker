<template>
  <Nav/>
<div class="row">
    <SlideBar/>

    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
    <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
        <h1 class="h2">Urzadzenia:</h1>
    </div>
    <!-- Tutaj muszą się wyświetlać funkcje -->
    
  <div class="row mb-2">  
    <!-- Tutaj jak coś musi być pętla for obejmująca urzadzenia -->
    <div class="col-md-6">
      <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
        <div class="col p-4 d-flex flex-column position-static">
          <strong class="d-inline-block mb-2 text-primary">
            Live
            </strong>
          <h3 class="mb-0">
            {{deviceName}} {{deviceGpsName}}
            </h3>
          <div class="mb-1 text-muted">
            Data i czas ostatniej aktualizacji: {{liveDate}} {{liveTime}}
            </div>
          <p class="card-text mb-auto">
            Pozycja urzadzenia to: {{liveLat}}, {{liveLong}}
          </p>
          <a href="" class="stretched-link">
            Zobacz na mapie
            </a>
        </div>
      </div>
    </div>
  </div>

    </main>
</div>
</template>

<script>
import Nav from "@/components/Nav.vue"
import SlideBar from "@/components/SlideBar.vue"

export default {
    name: 'Panel',
    data() {
      return {
        deviceName: "Nazwa urządzenia",
        deviceGpsName: "Nazwa GPS",
        liveDate: "Data",
        liveTime: "Godzina",
        liveLat: "Lat",
        liveLong: "Log"
      }
    },
    components: {
      Nav,
      SlideBar
    },
    async created() {
    const myToken = localStorage.getItem('user-token');
    // GET request using fetch with async/await
    const getPoz = await fetch('http://localhost:8000/api/live', {
          method: 'GET',
          headers: {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + myToken
          }});
    const data = await getPoz.json();
    // console.log(data);
    this.liveDate= data.my_date;
    this.liveTime = data.time;
    this.liveLat = data.latitude;
    this.liveLong = data.longitude;

    const getDevice = await fetch('http://localhost:8000/api/device', {
          method: 'GET',
          headers: {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + myToken
          }});
    const deviceData = await getDevice.json();
    for (let index = 0; index < deviceData.length; index++) {
      const element = deviceData[index];
      this.deviceName = element.device_name;
      this.deviceGpsName = element.gps_name;
    }
  }
  }
</script>
