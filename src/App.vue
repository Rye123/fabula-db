<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <header>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/classes">Classes</RouterLink>
        <RouterLink to="/skills">Skills</RouterLink>
      </nav>
    </header>

    <RouterView />
</template>

<style scoped>

</style>
