<template>
    <div class="heroImage"/>
</template>

<script>
export default {
    name: 'heroImage',
}
</script>

<style>
.heroImage {
    position: fixed;
    top: 0;
    z-index: -1;
    width: 100%;
    height: 100vh;
    background-image: url('../assets/heroimage.jpeg');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: 80% 0%;
}

</style>