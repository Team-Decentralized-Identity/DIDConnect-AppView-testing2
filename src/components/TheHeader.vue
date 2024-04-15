<script setup lang="ts">
import { useRoute } from "vue-router";

const route = useRoute();

const tabs = [
  {
    routeName: "index",
    label: "Home",
  },
  {
    routeName: "notifications",
    label: "Notifications",
  },
  {
    routeName: "search",
    label: "Search",
  },
  {
    routeName: "my-profile",
    label: "Profile",
  },
  {
    routeName: "settings",
    label: "Settings",
  },
];
</script>

<template>
  <div>
    <div v-if="route.name !== 'main'" class="columns col-oneline p-2">
      <div class="top-bar">
        <img src="/src/assets/Filled_DIDConnect_Logo.png" alt="DIDConnect Logo" style="height: 65px;">
        <span class="login-brand">DIDConnect</span>
      </div>

      <!-- Navigation Bar -->
      <aside class="navigation">
        <ul class="nav-list">
          <li v-for="tab in tabs" :key="tab.routeName" v-if="route.name !== 'login'">
            <RouterLink :to="{ name: tab.routeName }">
              {{ tab.label }}
            </RouterLink>
          </li>
         
        </ul>
      </aside>
    </div>
  </div>
</template>

<style scoped>
body {
  margin: 0;
  transition: background-color 0.3s, color 0.3s;
}

/* Navigation Bar */
.navigation {
  position: fixed;
  top: 8vh;
  left: 1.2%; 
  width: var(--nav-width);
  height: 100vh;
  padding: 1rem;
  box-sizing: border-box;
  cursor: pointer
}

.nav-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.nav-list li a {
 width: 100%; 
  text-align: left; 
  padding: 0; 
  color: inherit; 
  border: none; 
  font-size: 1.5rem; 
  cursor: pointer; 
  left: 1.2%;
  text-decoration: none;
}



</style>
