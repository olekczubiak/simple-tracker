<template>
        <p>Analiza pracy w danym dniu:</p>
        <div class="search-by-date">
        <input v-model="myData" type="data" class="form-control" placeholder="RRRR-MM-DD" required>
        <button class="w-100 btn btn-lg btn-primary" @click="getListOfPoz">Szukaj!</button>
        <div class="checkbox-for-show-map">
            <input type="checkbox" id="checkbox" v-model="checked">
            <label for="checkbox" id="label-for-checkbox-to-show-map"> Zaznacz jezeli chcesz pokazać mapę</label>
        </div>
        <p>Ile razu włączono urządzenie: <b>{{numOfPowerOn}}</b></p>
        <div v-if="isButtonToChooseTimeChecked==false" class="selecting-time-for-alalyze">
            <h1>Dostępne czasy: </h1>
            <div id="availableTimesId"></div>
            <input v-model="selectedTime" type="data" class="form-control" placeholder="Wybierz czas">
            <button class="w-100 btn btn-lg btn-primary" @click="SelectMyTime">Wybierz!</button>
        </div>
        </div>
    <div v-if="numOfPowerOn!=0 && isButtonToChooseTimeChecked==true" class="row mb-2">  
        <!-- Tutaj podstawowej info -->
        <div class="col-md-6">
            <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
                <div class="col p-4 d-flex flex-column position-static">
                    <strong class="d-inline-block mb-2 text-primary">
                    Info
                    </strong>
                    <h3 class="mb-0">
                        Czas pracy w dniu:  <b>{{workingTime}}</b>
                    </h3>
                    <div class="mb-1 text-muted">
                        <p> Pierwszy rekord dnia: <b>{{firstDayRecord}}</b></p>
                        <p> Ostatni rekord dnia: <b>{{lastDayRecord}}</b></p>
                    </div>
                    <div v-if="checked == true" >
                        <div id="route-map-content"></div>
                        <!-- <p> To jest mapa</p> -->
                        <div id="button-to-turn-on-the-map">
                            <button class="w-100 btn btn-lg btn-primary" @click="turnOnTheMap">Włącz mapę</button>
                        </div>
                    </div>
                    

                </div>
            </div>
            
        </div>

        <!-- Tutaj player -->
        <div class="col-md-6">
            <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
                <div class="col p-4 d-flex flex-column position-static">
                    <strong class="d-inline-block mb-2 text-primary">
                        Player
                    </strong>
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
                        <button @click="readTime" class="btn btn-secondary btn-sm" id="readtime-button">Załaduj godzine</button> 
                        <br>
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
            myData: "2021-11-25", 
            firstDayRecord: "",
            lastDayRecord: "",
            workingTime: "",
            numOfPowerOn: 0,
            listWithTime: [],
            listWithPoz: [],
            listWithLng: [],
            listWithLat: [],
            toPlayer: "Podaj datę by uzyskac info o godzinie i czasie",
            playerSpeed: [1, 2, 5, 10, 20, 40],
            selectedSpeed: 1,
            routeSrc: "",
            checked: false,
            playerTime: "",
            indexToStart: "",
            selectedTime: "",
            AfterClickOnButtonTime: 99,
            isButtonToChooseTimeChecked: false,

        }
    },

    methods: {
        getListOfPoz() {
            this.numOfPowerOn = 0;
            this.listWithTime = [];
            this.listWithPoz = [];
            this.listWithLng = [];
            this.listWithLat = [];
            this.isButtonToChooseTimeChecked = false;
            const myToken = localStorage.getItem('user-token');
            const myLink = "https://tracker.toadres.pl/api/list/day?day=" + this.myData;

            fetch(myLink, {
                method: 'GET',
                headers: {
                    'accept': 'application/json',
                    'Authorization': 'Bearer ' + myToken
                }}
                )
                .then(response => response.json())
                .then(data => {
                    for (let index = 0; index < data.length; index++) {
                        const element = data[index];
                        this.listWithTime.push(element.time);
                        this.listWithPoz.push(element.latitude + "," + element.longitude);
                        this.listWithLat.push(element.latitude);
                        this.listWithLng.push(element.longitude)
                    }

                    // Zamienienie listy czasowej z [x, 1, 2, 3, x, 1, 2] na [[1,2,3], [1,2]]
                    const listOfArrays = [];
                    const listOfArraysLat = [];
                    const listOfArraysLng = [];
                    const listOfArraysPoz = [];
                    var myArray = this.listWithTime.join("!").split("XX:XX:XX");
                    myArray.shift();
                    for (let index = 0; index < myArray.length; index++) {
                        const element = myArray[index];
                        var signsInArray = element.split("!");
                        signsInArray.pop();
                        signsInArray.shift();
                        listOfArrays.push(signsInArray);
                        const myFirstIndex = this.listWithTime.indexOf(signsInArray[0])
                        const myLastIndex = this.listWithTime.indexOf(signsInArray.slice(-1)[0]) + 1


                        const myNewListOfLat = this.listWithLat.slice(myFirstIndex, myLastIndex)
                        const myNewListOfLng = this.listWithLng.slice(myFirstIndex, myLastIndex)
                        const myNewListOfPoz = this.listWithPoz.slice(myFirstIndex, myLastIndex)

                        listOfArraysLat.push(myNewListOfLat)
                        listOfArraysLng.push(myNewListOfLng)
                        listOfArraysPoz.push(myNewListOfPoz)
                    }
                    this.numOfPowerOn = listOfArrays.length;

                    // Wybranie odpowieniego czasu
                    var availableTimes = "";
                    for (let index = 0; index < listOfArrays.length; index++) {
                        const element = listOfArrays[index];
                        availableTimes += "Wpisz <b>" + index + "</b> By wybrac analizę od godziny: <b>" + element[0] + "</b> <br>"
                        
                    }
                    document.getElementById("availableTimesId").innerHTML = availableTimes

                    // Nadpisanie lokalnej listy do globalnej
                    this.listWithTime = listOfArrays;
                    this.listWithPoz = listOfArraysPoz;
                    this.listWithLat = listOfArraysLat;
                    this.listWithLng = listOfArraysLng;

                    // To debug
                    // console.log(this.listWithTime[this.AfterClickOnButtonTime]);
                    // console.log(this.listWithTime);
                    // console.log(this.listWithPoz);
                    // console.log(this.listWithLng);
                    // console.log(this.listWithLat);





                    });
        },
        getPlayer() {
            if (this.listWithTime.length == 0){
                alert("Wybierz dzien, aby zacząć!!!")
            } else {
                if (this.playerTime == "") {
                    this.toPlayer = "";
                    this.listWithTime[this.AfterClickOnButtonTime].forEach((element,i) => {
                                    this.timer1 = setTimeout(
                                        function(){
                                            const data = element;
                                            document.getElementById("time-content").innerHTML = data;
                                        }
                                    , i * 1200 * (1/this.selectedSpeed) );
                    });
                    this.listWithPoz[this.AfterClickOnButtonTime].forEach((element,i) => {
                                    this.timer2 = setTimeout(
                                        function(){
                                            const data = "Pozycja " + element;
                                            const map = "//www.google.com/maps/embed/v1/place?key=AIzaSyCFcWFS_zSfHFCh5HV7qIwFrx_uwrfV5Kk&q=" + element;
                                            const mapIframe = "<iframe width=\"600\" height=\"450\" style=\"border:0\" allowfullscreen src=" + map + ">";
                                            document.getElementById("poz-content").innerHTML = data;
                                            document.getElementById("map-content").innerHTML = mapIframe;
                                        }
                                    , i * 1200 * (1/this.selectedSpeed));
                    });
                } else {
                    for (let index = 0; index < this.timer2 + this.timer1; index++) {
                        clearTimeout(index);
                    }
                    this.listWithTime[this.AfterClickOnButtonTime].slice(this.indexToStart, this.listWithTime[this.AfterClickOnButtonTime].length).forEach((element,i) => {
                                    this.timer1 = setTimeout(
                                        function(){
                                            const data = element;
                                            document.getElementById("time-content").innerHTML = data;
                                        }
                                    , i * 1200 * (1/this.selectedSpeed) );
                    });
                    this.listWithPoz[this.AfterClickOnButtonTime].slice(this.indexToStart, this.listWithTime[this.AfterClickOnButtonTime].length).forEach((element,i) => {
                                    this.timer2 = setTimeout(
                                        function(){
                                            const data = "Pozycja " + element;
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
            for (let index = 0; index < this.timer2 + this.timer1; index++) {
                clearTimeout(index);
            }
            this.playerTime = "";
            // document.getElementById("time-content").innerHTML = "";
            // document.getElementById("poz-content").innerHTML = "";
        },
        stopPlayer() {
            this.toPlayer = "Zastopowałeś odtwarzanie, kliknij START!!";
            for (let index = 0; index < this.timer2 + this.timer1; index++) {
                clearTimeout(index);
            }

            const myTimer =  document.getElementById("time-content").innerHTML;
            this.indexToStart = this.listWithTime[this.AfterClickOnButtonTime].indexOf(myTimer);
            this.playerTime = myTimer
        },
        readTime() {
            this.indexToStart = this.listWithTime[this.AfterClickOnButtonTime].indexOf(this.playerTime);
            if (this.indexToStart == -1){
                alert("Nie ma podanej godziny!")
            }
        },
        SelectMyTime() {
            if (this.selectedTime == "" || this.selectedTime >= this.numOfPowerOn) {
                alert("Wybierz poprawny czas")
            } else {
                this.AfterClickOnButtonTime = this.selectedTime;
                this.isButtonToChooseTimeChecked = true;

                const date1 = new Date( this.myData + " " + this.listWithTime[this.AfterClickOnButtonTime][0]);
                const date2 = new Date(this.myData + " " + this.listWithTime[this.AfterClickOnButtonTime].slice(-1)[0]);

                const timeDiff = (date2 - date1);
                const min = Math.floor((timeDiff/1000/60) << 0);
                const sec = Math.floor((timeDiff/1000) % 60);

                this.workingTime = min + " min " + sec + " sec"

                this.firstDayRecord = "Godzina: " + this.listWithTime[this.AfterClickOnButtonTime][0] + " latitude: " + this.listWithLat[this.AfterClickOnButtonTime][0] + " longitude: " + this.listWithLng[this.AfterClickOnButtonTime][0];
                this.lastDayRecord = "Godzina: " + this.listWithTime[this.AfterClickOnButtonTime].slice(-1)[0] + " latitude: " + this.listWithLat[this.AfterClickOnButtonTime].slice(-1)[0] + " longitude: " + this.listWithLng[this.AfterClickOnButtonTime].slice(-1)[0];
            }
        },
        turnOnTheMap() {
                const map = "//www.google.com/maps/embed/v1/directions?origin=" + this.listWithLat[this.AfterClickOnButtonTime][0]+ "," + this.listWithLng[this.AfterClickOnButtonTime][0] + "&destination=" + this.listWithLat[this.AfterClickOnButtonTime].slice(-1)[0] + "," + this.listWithLng[this.AfterClickOnButtonTime].slice(-1)[0] + "&key=AIzaSyCFcWFS_zSfHFCh5HV7qIwFrx_uwrfV5Kk";

                let mapIframe = "<iframe width=\"600\" height=\"450\" style=\"border:0\" allowfullscreen src=" + map + ">";
                document.getElementById("route-map-content").innerHTML = mapIframe;
                document.getElementById("button-to-turn-on-the-map").innerHTML = "";
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
    margin-top: 5px;
    /* float: right; */
    margin-left: auto; 
    margin-right: 0;
    font-size: 15px;
}
#speed-selector {
    margin-top: 5px;
}
</style>