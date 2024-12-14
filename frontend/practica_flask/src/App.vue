<script setup>
import { RouterLink, RouterView } from 'vue-router'
import headerCOMP from './components/COMPheader.vue';
</script>

<template>
    <div>
      <headerCOMP></headerCOMP>
    </div>
    <div>
      <RouterView />
    </div>
    <div>

    </div>

</template>

<style scoped>

</style>
