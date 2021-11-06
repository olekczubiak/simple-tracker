<template>

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
        Pozycja urzadzenia to:  {{liveLong}}, {{liveLat}}
        </p>
    </div>
    <iframe
    width="600"
    height="450"
    style="border:0"
    loading="lazy"
    allowfullscreen
    :src="srcToGoogleMap"
    >
    </iframe>
    </div>
</div>

</div>
</template>

<script>
export default {
    name: "GetLivePoz",
    data() {
        return {
            srcToGoogleMap: "//www.google.com/maps/embed/v1/place?key=AIzaSyCFcWFS_zSfHFCh5HV7qIwFrx_uwrfV5Kk&q=łódź",
            deviceName: "Nazwa urządzenia",
            deviceGpsName: "Nazwa GPS",
            liveDate: "Data",
            liveTime: "Godzina",
            liveLat: "Lat",
            liveLong: "Log",
        }
    },
    async created() {
    const myToken = localStorage.getItem('user-token');
    // GET request using fetch with async/await
    const getPoz = await fetch('https://tracker.toadres.pl/api/live', {
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
    this.srcToGoogleMap = "//www.google.com/maps/embed/v1/place?key=AIzaSyCFcWFS_zSfHFCh5HV7qIwFrx_uwrfV5Kk&q=" + data.longitude + "," + data.latitude;

    const getDevice = await fetch('https://tracker.toadres.pl/api/device', {
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
    },

}
</script>

<style>

</style>