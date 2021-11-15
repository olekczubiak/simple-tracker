<template>
    <Nav/>
    <SlideBar/>
    
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
    <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
        <h1 class="h2">Storna panelu:</h1>
    </div>
    <MonthlyCalendar/>


    </main>
</template>

<script>
import Nav from "@/components/Nav.vue"
import SlideBar from "@/components/SlideBar.vue"
import MonthlyCalendar from '@/components/MonthlyCalendar.vue'

export default {
    name: "Calendar",
    components: {
        Nav,
        SlideBar,
        MonthlyCalendar
    }
}
</script>

<style>

</style>