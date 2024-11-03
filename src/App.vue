<script setup>
import SkillSearch from "@/components/SkillSearch.vue";

</script>

<template>
    <header>

    </header>

    <main>
      <Suspense><SkillSearch :skills="() => $refs['dataSkills']" /></Suspense>
    </main>
</template>

<style scoped>

</style>
