<script setup>
import {computed, ref} from 'vue'
import SkillItem from "@/components/SkillItem.vue";
const API_URL = "http://127.0.0.1:5000/api/";

const skillsResp = await fetch(API_URL + "skill/");
const skills = ref(null);
skills.value = await skillsResp.json();

const filterName = ref("");
const filterReq = ref("");
const filterDesc = ref("");
const filteredSkills = computed(() => {
  if (filterName.value === "" && filterReq.value === "" && filterDesc.value === "")
    return skills.value;
  return Object.fromEntries(Object.entries(skills.value).filter(([, skill]) => {
    if (!skill.name.toLowerCase().includes(filterName.value.toLowerCase()))
      return false;
    if (!skill.description.toLowerCase().includes(filterDesc.value.toLowerCase()))
      return false;
    // TODO: Split requirements into CSV
    if (!skill.requirements.toLowerCase().includes(filterReq.value.toLowerCase()))
      return false;
    return true;
  }));
})
</script>

<template>
    <header>
      <h1>Skills</h1>
    </header>

    <main>
      <div>
        <h2>Filter</h2>
        <strong>Name</strong>: <input type="text" v-model="filterName" /> <br />
        <strong>Requirements</strong>: <input type="text" v-model="filterReq" /> <br />
        <strong>Description</strong>: <input type="text" v-model="filterDesc" /> <br />
      </div>
      <ul v-if="skills">
        <li v-for="skill in filteredSkills" v-bind:key="skill.name">
          <SkillItem :skill=skill />
        </li>
      </ul>
      <div v-else>Loading...</div>
    </main>
</template>

<style scoped>

</style>
