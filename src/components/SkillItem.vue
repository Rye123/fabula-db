<script setup>
import { ref } from "vue";

const props = defineProps({
  skill: {
    name: String,
    sourcebook: String,
    requirements: String,
    description: String,
    maxSkillLevel: Number
  }
});

const skill = ref(props.skill);
</script>

<template>
  <h3 v-if="skill.isHeroicSkill">{{ skill.name }}  (<i>Heroic</i>)</h3>
  <h3 v-else>
    <span v-if="skill.maxSkillLevel !== 1">{{ skill.name }} (✦{{ skill.maxSkillLevel }})</span>
    <span v-else>{{ skill.name }}</span>
  </h3>
  <div><em>{{ skill.sourcebook }}</em></div>
  <div>Prerequisites: <i>{{ skill.requirements }}</i></div>
  <div v-html="skill.description"></div>
</template>

<style scoped>

</style>
