<script setup>
import { ref } from 'vue'
const API_URL = "http://127.0.0.1:5000/api/"

const skillsResp = await fetch(API_URL + "skill/")
const skills = ref(null);
skills.value = await skillsResp.json();
</script>

<template>
    <header>
    </header>

    <main>
      <ul v-if="skills">
        <li v-for="skill in skills" v-bind:key="skill.name">
          <h1 v-if="skill.maxSkillLevel !== 1">{{ skill.name }} (✦{{ skill.maxSkillLevel }})<br /></h1>
          <h1 v-else>{{ skill.name }}<br /></h1>
          <div><i>{{ skill.requirements }}</i></div>
          <div v-html="skill.description"></div>
        </li>
      </ul>
      <div v-else>Loading...</div>
    </main>
</template>

<style scoped>

</style>
