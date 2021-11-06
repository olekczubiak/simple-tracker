<template>
    <Nav/>
        <div class="row">
    <SlideBar/>

    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
    <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
        <h1 class="h2">Monitorowanie:</h1>

        <button @click="Refresh" type="button" class="btn btn-outline-dark">Refresh!</button>

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
    methods: {
        Refresh() {
            window.location.reload();
        },
        // startRefresh() {
        //     const MyTimeout = window.setTimeout(function() {
        //             window.location.reload();
        //         }, 5000)
        // }
    }
}

</script>
