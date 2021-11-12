<template>
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
        <!-- Tutaj podstawowej info -->
        <div class="col-md-6">
            <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
                <div class="col p-4 d-flex flex-column position-static">
                    <strong class="d-inline-block mb-2 text-primary">
                    Ile razu włączono urządzenie: <b>{{numOfPowerOn}}</b>
                    </strong>
                    <h3 class="mb-0">
                        Czas pracy w dniu:  <b>{{workingTime}}</b>
                    </h3>
                    <div class="mb-1 text-muted">
                        <p> Pierwszy rekord dnia: <b>{{firstDayRecord}}</b></p>
                        <p> Ostatni rekord dnia: <b>{{lastDayRecord}}</b></p>
                    </div>
                </div>
            </div>
            
        </div>

        <!-- Tutaj player -->
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
                        <div id="time-content"></div>
                        <div id="poz-content"></div>
                        <div id="map-content"></div>
                        {{toPlayer}}
                    </div>
                    <p class="card-text mb-auto">
                        <button @click="getPlayer" class="btn btn-secondary btn-sm" id="start-button">Start!</button>
                        <button @click="stopPlayer" class="btn btn-secondary btn-sm" id="stop-button">Stop!</button>
                        <select v-model="selectedSpeed" style="width:10%;"> -->
                            <option v-for="element in playerSpeed" v-bind:key="element" :selected="playerSpeed === element">{{ element }}</option>
                        </select>
                        
                    </p>
                    
                </div>
            </div>
            
        </div>

    </div>




</template>

<script>

export default {
    name: "AnalizeTime",
    data() {
        return {
            // Po testach datę trzeba usunać!!!!
            myData: "2021-10-30", 
            firstDayRecord: "",
            lastDayRecord: "",
            numOfPowerOn: 1,
            workingTime: "",
            listWithTime: [],
            listWithPoz: [],
            toPlayer: "Podaj datę by uzyskac info o godzinie i czasie",
            playerSpeed: [1, 2, 5, 10, 20, 40],
            selectedSpeed: 1,

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
                alert("Wybierz dzien, aby zacząć!!!")
            } else {
                
                this.toPlayer = "";

                this.listWithTime.forEach((element,i) => {
                                this.timer1 = setTimeout(
                                    function(){
                                        const data = "Godzina " + element;
                                        // console.log(data)
                                        document.getElementById("time-content").innerHTML = data;
                                    }
                                , i * 1200 * (1/this.selectedSpeed) );
                                console.log(this.selectedSpeed);
                });
                this.listWithPoz.forEach((element,i) => {
                                this.timer2 = setTimeout(
                                    function(){
                                        const data = "Pozycja " + element;
                                        // console.log(data)
                                        const map = "//www.google.com/maps/embed/v1/place?key=AIzaSyCFcWFS_zSfHFCh5HV7qIwFrx_uwrfV5Kk&q=" + element;
                                        const mapIframe = "<iframe width=\"600\" height=\"450\" style=\"border:0\" allowfullscreen src=" + map + ">";
                                        document.getElementById("poz-content").innerHTML = data;
                                        document.getElementById("map-content").innerHTML = mapIframe;
                                    }
                                , i * 1200 * (1/this.selectedSpeed));
                });
            }
            
        },
        stopPlayer() {
            this.toPlayer = "Przerwałeś odtwarzać, kliknij START!!";
            for (let index = 0; index < this.timer2; index++) {
                clearTimeout(index);
            }
            // document.getElementById("time-content").innerHTML = "";
            // document.getElementById("poz-content").innerHTML = "";
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
#start-button {
    margin-right: 5px;
}
#stop-button {
    margin-left: 5px;
    margin-right: 5px;
}
</style>