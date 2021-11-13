<template>
        <p>Analiza pracy w danym dniu:</p>
        <div class="search-by-date">
        <input v-model="myData" type="data" class="form-control" placeholder="RRRR-MM-DD" required>
        <button class="w-100 btn btn-lg btn-primary" @click="getListOfPoz">Szukaj!</button>
        <input type="checkbox" id="checkbox" v-model="checked">
        <label for="checkbox" id="label-for-checkbox-to-show-map"> Zaznacz jezeli chcesz pokazać mapę</label>
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
                        <div v-if="checked==true" id="all-map-content"></div>
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
                    <div class="card-text mb-auto">
                        <button @click="getPlayer" class="btn btn-secondary btn-sm" id="start-button">Start</button>
                        <button @click="stopPlayer" class="btn btn-secondary btn-sm" id="stop-button">Stop</button>
                        <button @click="resetPlayer" class="btn btn-secondary btn-sm" id="reset-button">Reset</button>
                        <input v-model="playerTime" type="data" class="form-control" placeholder="Player time" id="input-player-timer">
                        <select v-model="selectedSpeed" style="width:6%;" id="speed-selector">
                            <option v-for="element in playerSpeed" v-bind:key="element" :selected="playerSpeed === element">{{ element }}</option>
                        </select>
                        <p id="info-about-speeed"> Wybierz predkość</p>
                    </div>
                    
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
            routeSrc: "",
            checked: false,
            playerTime: "",
            indexToStart: "",
        }
    },

    methods: {
        getListOfPoz() {
            this.listWithTime = [];
            this.listWithPoz = [];
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
                    // dodanie czasów i poz do list
                    for (let index = 0; index < data.length; index++) {
                        const element = data[index];
                        this.listWithTime.push(element.time);
                        this.listWithPoz.push(element.latitude + "," + element.longitude);
                    }

                    const date1 = new Date( this.myData + " " + data[0].time);
                    const date2 = new Date(this.myData + " " + data.slice(-1)[0].time);

                    const timeDiff = (date2 - date1);
                    const min = Math.floor((timeDiff/1000/60) << 0);
                    const sec = Math.floor((timeDiff/1000) % 60);
                    // console.log(min + " min " + sec + " sec")
                    this.workingTime = min + " min " + sec + " sec"

                    this.firstDayRecord = "Godzina: " + data[0].time + " latitude: " + data[0].latitude + " longitude: " + data[0].longitude;
                    this.lastDayRecord = "Godzina: " + data.slice(-1)[0].time + " latitude: " + data.slice(-1)[0].latitude + " longitude: " + data.slice(-1)[0].longitude;

                    const map = "//www.google.com/maps/embed/v1/directions?origin=" + data[0].latitude + "," + data[0].longitude + "&destination=" + data.slice(-1)[0].latitude + "," + data.slice(-1)[0].longitude + "&key=AIzaSyCFcWFS_zSfHFCh5HV7qIwFrx_uwrfV5Kk";
                    const mapIframe = "<iframe width=\"600\" height=\"450\" style=\"border:0\" allowfullscreen src=" + map + ">";
                    document.getElementById("all-map-content").innerHTML = mapIframe;
                    });
        },
        getPlayer() {
            if (this.listWithTime.length == 0){
                alert("Wybierz dzien, aby zacząć!!!")
            } else {
                if (this.playerTime == "") {
                    this.toPlayer = "";
                    this.listWithTime.forEach((element,i) => {
                                    this.timer1 = setTimeout(
                                        function(){
                                            const data = element;
                                            // console.log(data)
                                            document.getElementById("time-content").innerHTML = data;
                                        }
                                    , i * 1200 * (1/this.selectedSpeed) );
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
                } else {
                    for (let index = 0; index < this.timer2; index++) {
                        clearTimeout(index);
                    }
                    console.log("odpal od specyficznego momentu " + this.indexToStart)
                    this.listWithTime.slice(this.indexToStart, this.listWithTime.length).forEach((element,i) => {
                                    this.timer1 = setTimeout(
                                        function(){
                                            const data = element;
                                            document.getElementById("time-content").innerHTML = data;
                                        }
                                    , i * 1200 * (1/this.selectedSpeed) );
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
                
            }
            
        },
        resetPlayer() {
            this.toPlayer = "Przerwałeś odtwarzać, kliknij START!!";
            for (let index = 0; index < this.timer2; index++) {
                clearTimeout(index);
            }
            this.playerTime = "";
            // document.getElementById("time-content").innerHTML = "";
            // document.getElementById("poz-content").innerHTML = "";
        },
        stopPlayer() {
            this.toPlayer = "Zastopowałeś odtwarzanie, kliknij START!!";
            console.log('kliknieto stop');
            for (let index = 0; index < this.timer2; index++) {
                clearTimeout(index);
            }

            const myTimer =  document.getElementById("time-content").innerHTML;
            this.indexToStart = this.listWithTime.indexOf(myTimer);
            this.playerTime = myTimer
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
#reset-button {
    margin-left: 5px;
    margin-right: 5px;
}
#label-for-checkbox-to-show-map {
    margin-top: 5px;
    margin-left: 4px;
    margin-bottom: 5px;
}
#input-player-timer{
    width: 175px;
    margin-top: 5px;
    margin-bottom: 5px;
}
#info-about-speeed {
    float: right;
    margin-right: 550px;
    font-size: 15px;
}
</style>