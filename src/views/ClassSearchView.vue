<script setup>
import {computed, onMounted, ref} from 'vue'
import ClassItem from "@/components/ClassItem.vue";
import showdown from 'showdown'
import sanitizeHtml from 'sanitize-html'

const fileClasses = new URL('/data/classes.json', import.meta.url);
const pClasses = ref(null);

const filterName = ref("");
const filteredClasses = computed(() => {
  if (filterName.value === "")
    return pClasses.value;
  return pClasses.value.filter(pClass => {
    if (!pClass.name.toLowerCase().includes(filterName.value.toLowerCase()))
      return false;
    return true;
  });
});

onMounted(async () => {
  pClasses.value = await fetch(fileClasses)
      .then(res => res.json())
      .then(classesJSON => {
        // Convert and sanitise Markdown descriptions
        // For unformatted description (for filtering), we want to
        // replace all newlines with space since that's easier to search by
        const converter = new showdown.Converter();
        return classesJSON.map(classJSON => {
          var finalDesc = "";
          var paras = classJSON.description.split("\n");
          for (var para of paras) {
            var desc = converter.makeHtml(para);
            desc = sanitizeHtml(desc, {
              allowedTags: [ 'b', 'strong', 'i', 'em', 'br' ],
              allowedAttributes: {},
              disallowedTagsMode: 'discard'
            });
            finalDesc += "<div>" + desc + "</div>";
          }

          classJSON["description"] = finalDesc;
          return classJSON;
        });
      })
})
</script>

<template>
  <div class="view">
    <h1>Classes</h1>
    <div class="filterBox">
      <h3>Filter</h3>
      <label>Name<br /> <input type="text" v-model="filterName" /></label>
    </div>
    <br />
    <div v-if="pClasses">
      <div class="classItem" v-for="pClass in filteredClasses" v-bind:key="pClass.name">
        <ClassItem :pClass=pClass />
      </div>
    </div>
    <div v-else>Loading...</div>
  </div>
</template>

<style scoped>
.classItem {
  padding-bottom: 1rem;
}
</style>