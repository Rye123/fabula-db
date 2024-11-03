<script setup>
import { ref } from "vue";

const props = defineProps({
  pClass: {
    name: String,
    sourcebook: String,
    description: String,
    benefits: {
      hpBonus: Number,
      mpBonus: Number,
      ipBonus: Number,
      martial: {
        melee: Boolean,
        ranged: Boolean,
        armor: Boolean,
        shield: Boolean
      },
      rituals: {
        arcanism: Boolean,
        chimerism: Boolean,
        elementalism: Boolean,
        entropism: Boolean,
        ritualism: Boolean,
        spiritism: Boolean
      },
      initiateProjects: Boolean,
      custom: String
    }
  }
});

const pClass = ref(props.pClass);
</script>

<template>
  <h3>{{pClass.name}}</h3>
  <div><i>{{pClass.sourcebook}}</i></div>
  <div v-html="pClass.description"></div>
</template>

<style scoped>

</style>
