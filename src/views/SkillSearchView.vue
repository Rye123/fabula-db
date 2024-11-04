<script setup>
import {computed, onMounted, ref} from 'vue'
import SkillItem from "@/components/SkillItem.vue";
import showdown from 'showdown'
import sanitizeHtml from 'sanitize-html'

const fileSkills = new URL('/data/skills.json', import.meta.url);
const skills = ref(null);

const filterName = ref("");
const filterReq = ref("");
const filterDesc = ref("");
const filterClassSkills = ref(true);
const filterHeroicSkills = ref(true);
const filteredSkills = computed(() => {
  if (!filterClassSkills.value && !filterHeroicSkills.value)
    return [];
  return skills.value.filter(skill => {
    if (!filterHeroicSkills.value)
      if (skill.isHeroicSkill)
        return false;

    if (!filterClassSkills.value)
      if (!skill.isHeroicSkill)
        return false;

    if (!skill.name.toLowerCase().includes(filterName.value.toLowerCase()))
      return false;
    if (!skill.unformattedDescription.toLowerCase().includes(filterDesc.value.toLowerCase()))
      return false;
    // TODO: Split requirements into CSV
    if (!skill.requirements.toLowerCase().includes(filterReq.value.toLowerCase()))
      return false;
    return true;
  }).sort((s1, s2) => s1.name > s2.name);
});

onMounted(async () => {
  skills.value = await fetch(fileSkills)
      .then(res => res.json())
      .then(skillsJSON => {
        // Convert and sanitise Markdown descriptions
        // For unformatted description (for filtering), we want to
        // replace all newlines with space since that's easier to search by
        const converter = new showdown.Converter();
        return skillsJSON.map(skillJSON => {
          var finalDesc = "";
          var unformattedDesc = "";
          var paras = skillJSON.description.split("\n");
          for (var para of paras) {
            var desc = converter.makeHtml(para);
            desc = sanitizeHtml(desc, {
              allowedTags: [ 'b', 'strong', 'i', 'em', 'br', 'ul', 'li' ],
              allowedAttributes: {},
              disallowedTagsMode: 'discard'
            });
            finalDesc += "<div>" + desc + "</div>";

            unformattedDesc += " " + sanitizeHtml(desc.toLowerCase(), {
              allowedTags: [],
              allowedAttributes: {},
              disallowedTagsMode: 'discard'
            });
          }

          skillJSON["description"] = finalDesc;
          skillJSON["unformattedDescription"] = unformattedDesc;

          return skillJSON;
        });
      })
})
</script>

<template>
    <div class="view">
      <h1>Skills</h1>
      <div>
        <h2>Filter</h2>
        <strong>Name</strong>: <input type="text" v-model="filterName" /> <br />
        <strong>Requirements</strong>: <input type="text" v-model="filterReq" /> <br />
        <strong>Description</strong>: <input type="text" v-model="filterDesc" /> <br />
        <strong>Skill Type</strong>:
        <ul>
          <li><input type="checkbox" v-model="filterClassSkills" /> Include Class Skills</li>
          <li><input type="checkbox" v-model="filterHeroicSkills" /> Include Heroic Skills</li>
        </ul>
      </div>
      <br />
      <hr />
      <br />
      <div v-if="skills">
        <ul>
          <li v-for="skill in filteredSkills" v-bind:key="skill.name">
            <SkillItem :skill=skill />
          </li>
        </ul>
      </div>
      <div v-else>Loading...</div>
    </div>
</template>

<style scoped>

</style>
