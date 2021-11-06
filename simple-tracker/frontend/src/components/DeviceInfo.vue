<template>
    <div class="col-md-6">
    <h2>Twoje urzadzenie:</h2>
    <ul class="list">
        <li class="text-muted">Urzadzenie: <b>{{device}} </b> </li>
        <li class="text-muted">Moduł GPS: <b>{{gps}} </b> </li>
        <li class="text-muted">Numer ID właściciela: <b>{{ownerId}} </b> </li>
        <li class="text-muted">Opis: <b>{{desc}} </b> </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: "DeviceInfo",
    data() {
        return {
            device: "",
            gps: "",
            ownerId: "",
            desc: "",
        }
    },
    async created() {
        const myToken = localStorage.getItem('user-token');
        const getDevice = await fetch('https://tracker.toadres.pl/api/device', {
            method: 'GET',
            headers: {
                'accept': 'application/json',
                'Authorization': 'Bearer ' + myToken
            }});
            const deviceData = await getDevice.json();
            for (let index = 0; index < deviceData.length; index++) {
                const element = deviceData[index];
                this.device = element.device_name;
                this.gps = element.gps_name;
                this.ownerId = element.owner_id;
                this.desc = element.description;
            }
    }
}
</script>

<style>

</style>