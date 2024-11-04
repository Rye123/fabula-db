<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <h1><RouterLink to="/">fabula-db</RouterLink></h1>
    <nav>
      <RouterLink to="/classes">classes</RouterLink>
      <RouterLink to="/skills">skills</RouterLink>
    </nav>
  </header>
  <hr />
  <br />
  <RouterView />
</template>

<style scoped>
nav * {
  font-size: 1.1rem;
}

.router-link-active {
  background-color: hsla(160, 100%, 37%, 0.3);
}
</style>
