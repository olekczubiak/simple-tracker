<template>
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
        <p>Analiza pracy w danym dniu:</p>
        <div class="search-by-date">
        <input v-model="myData" type="data" class="form-control" placeholder="RRRR-MM-DD" required>
        <button class="w-100 btn btn-lg btn-primary" @click="getListOfPoz">Szukaj!</button>
        </div>
        <!-- <div class="search-for-resp">
            <p> Ile razu odpalono dzisiaj urządzenie <b>{{numOfPowerOn}}</b></p>
            <p> Pierwszy rekord dnia: <b>{{firstDayRecord}}</b></p>
            <p> Ostatni rekord dnia: <b>{{lastDayRecord}}</b></p>
            <p> Czas pracy w dniu:  <b>{{workingTime}}</b></p>
            <p> Lista z czasem: {{listWithTime}}</p>
            <p> Lista z pozycjami {{listWithPoz}}</p>
        </div> -->
    
    <div class="row mb-2">  
    <!-- Tutaj jak coś musi być pętla for obejmująca urzadzenia -->
        <div class="col-md-6">
            <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
                <div class="col p-4 d-flex flex-column position-static">
                    <strong class="d-inline-block mb-2 text-primary">
                    Rekord 1
                    </strong>
                    <h3 class="mb-0">
                        Player
                    </h3>
                    <div class="mb-1 text-muted">
                        {{toPlayer}}
                    </div>
                    <p class="card-text mb-auto">
                        <button @click="getPlayer" class="btn btn-secondary btn-sm">Start</button>
                        <!-- <button type="button" class="btn btn-secondary btn-sm">Small button</button> -->
                    </p>
                    
                </div>
            </div>
            
        </div>

    </div>




        </main>
</template>

<script>

export default {
    name: "AnalizeTime",
    data() {
        return {
            myData: "2021-10-30",
            firstDayRecord: "",
            lastDayRecord: "",
            numOfPowerOn: 0,
            workingTime: "",
            listWithTime: [],
            listWithPoz: [],
            toPlayer: "Podaj datę by uzyskac info o godzinie i czasie",
        }
    },

    methods: {
        getListOfPoz() {
            const myToken = localStorage.getItem('user-token');
            const myLink = "https://tracker.toadres.pl/api/list/day?day=" + this.myData;

            const getDailyPoz = fetch(myLink, {
                method: 'GET',
                headers: {
                    'accept': 'application/json',
                    'Authorization': 'Bearer ' + myToken
                }}
                )
                .then(response => response.json())
                .then(data => {
                    // console.log(data)
                    // dodanie czasów i poz do list
                    for (let index = 0; index < data.length; index++) {
                        const element = data[index];
                        this.listWithTime.push(element.time);
                        this.listWithPoz.push(element.latitude + "," + element.longitude);
                    }




                    // Obliczenia zwiazane z czasem
                    const date1 = new Date( this.myData + " " + data[0].time);
                    const date2 = new Date(this.myData + " " + data.slice(-1)[0].time);

                    const timeDiff = (date2 - date1);
                    const min = Math.floor((timeDiff/1000/60) << 0);
                    const sec = Math.floor((timeDiff/1000) % 60);
                    // console.log(min + " min " + sec + " sec")
                    this.workingTime = min + " min " + sec + " sec"

                    this.firstDayRecord = "Godzina: " + data[0].time + " latitude: " + data[0].latitude + " longitude: " + data[0].longitude;
                    this.lastDayRecord = "Godzina: " + data.slice(-1)[0].time + " latitude: " + data.slice(-1)[0].latitude + " longitude: " + data.slice(-1)[0].longitude;
                    });
        },
        getPlayer() {
            if (this.listWithTime.length == 0){
                alert("Załaduj listę zeby zaczac")
            } else {
                for (let index = 0; index < this.listWithTime.length; index++) {
                    const time = this.listWithTime[index];
                    const poz = this.listWithPoz[index];
                    const data = "Godzina " + time + " Pozycja " + poz ;
                    this.toPlayer = data
                }
                
                console.log(this.listWithTime.length)
                console.log("załadowane")

            }
            
        }
    }
}


</script>

<style>
.search-by-date{
    margin-top: 5px;
    margin-bottom: 5px;
    width: 30%;
}
.search-by-date input[type="data"] {
    margin-bottom: 10px;
}

</style>