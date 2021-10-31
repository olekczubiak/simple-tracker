<template>
    <div class="wrapper">
        <HeroImage/>
        <h1 class="claim">Tracker</h1>
        <p class="subclaim">
            Popraw produktywnosc przez monitoring i analize swoich pojazdow. <br>
            Poznaj miasto i wybierz pore dnia dopasowana do siebie. 
        </p>
        <p class="subclaim">
            Aplikacja do monitorowania i analizowania pojazdow w zdefiniowanej przestrzenii.
        </p>
        <router-link class="button-28" to="/login"> Zaloguj się! </router-link>
        <router-link class="button-28" to="/panel"> Panel </router-link>
    </div>
</template>

<script >
import HeroImage from './HeroImage.vue'

export default {
  name: 'Claim',
  components: {
    HeroImage
  }
}

</script>

<style>
    .wrapper {
        display: flex;
        text-align: center;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: black;
    }
    .claim {
        font-size: 50px;
        margin: 0px;
    }
    .subclaim {
        margin-top: 15px 0 0 0;
        font-size: 15px;
    }

    .button-28 {
    appearance: none;
    background-color: transparent;
    border: 2px solid #1A1A1A;
    border-radius: 15px;
    box-sizing: border-box;
    color: #3B3B3B;
    cursor: pointer;
    display: inline-block;
    font-family: Roobert,-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
    font-size: 16px;
    font-weight: 600;
    line-height: normal;
    margin: 0;
    min-height: 20px;
    min-width: 0;
    outline: none;
    padding: 16px 24px;
    text-align: center;
    text-decoration: none;
    transition: all 300ms cubic-bezier(.23, 1, 0.32, 1);
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
    margin-top: 5px;
    width: 15%;
    will-change: transform;
    }

    .button-28:disabled {
    pointer-events: none;
    }

    .button-28:hover {
    color: #fff;
    background-color: #1A1A1A;
    box-shadow: rgba(0, 0, 0, 0.25) 0 8px 15px;
    transform: translateY(-2px);
    }

    .button-28:active {
    box-shadow: none;
    transform: translateY(0);
    }
</style>