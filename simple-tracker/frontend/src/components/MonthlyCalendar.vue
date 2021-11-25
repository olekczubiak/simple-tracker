<template>
    <p>Wybierz miesiąc w którym chcesz zobaczyć ile razy włączono urządzenie:</p>
        <form>
            <div class="row">
                <div class="col-sm-4">
                    <div class="form-group">
                        <div class="input-group">
                            <select v-model="month" class="form-select" aria-label="Default select example">
                                <option v-for="month in monthSelected" :key="month"  > {{month}}</option>
                            </select>
                            <button @click="getEventsFromMonth" type="button" class="btn btn-outline-dark">Szukaj!</button>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    <br>
    <div v-if="active==false">
        <h2>{{infoIsMonthActive}}</h2>
    </div>

    <div v-if="active==true" >
    <table class="table mt-4">
    <thead>
        <tr>
        <th scope="col">#</th>
        <th scope="col">Dzień</th>
        <th scope="col">Ile razy włączono urządzenie</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="item, index in items[0]" :key="item">
        <th scope="row">{{index + 1}}</th>
        <td>{{item.Day}}.{{month}}</td>
        <td><b>{{item.Num}}</b></td>
        </tr>
    </tbody>
    </table>
    </div>
</template>

<script>
export default {
    name: "MonthlyCalendar",
    data() {
        return {
            month: "",
            monthSelected: ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec" ],
            infoIsMonthActive: "",
            items: [],
            active: Boolean,

        }
    },
    methods: {
        getEventsFromMonth() {
            const indexofMonth = this.monthSelected.indexOf(this.month) + 1;
            const myToken = localStorage.getItem('user-token');
            fetch('https://tracker.toadres.pl/api/list/monthly?month=' + indexofMonth, {
            method: 'GET',
            headers: {
                'accept': 'application/json',
                'Authorization': 'Bearer ' + myToken
            }})
            .then(response => response.json())
            .then(data => {
                if (data.length == 0) {
                    this.infoIsMonthActive = "Brak aktywności w danym miesiącu!!!"
                    this.active = false
                } else {
                    this.infoIsMonthActive = ""
                    this.items.push(data)
                    this.active = true
                }
            });
            console.log(this.itemschro, )
            // for (let index = 0; index < deviceData.length; index++) {
            //     const element = deviceData[index];
            //     this.device = element.device_name;
            //     this.gps = element.gps_name;
            //     this.ownerId = element.owner_id;
            //     this.desc = element.description;
            // }
            // console.log(indexofMonth)
        }
    }

}
</script>

<style>
</style>