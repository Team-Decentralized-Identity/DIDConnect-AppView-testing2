<script setup lang="ts">
import { reactive } from "vue";

import TileUser from "@/components/user/TileUser.vue";
import { ProfileView,searchActors } from "@/lib/bsky";

const state = reactive({
  query: "",
  sent: false,
  users: [] as ProfileView[],
});

const submit = async () => {
  if (state.query) {
    const [users] = await searchActors({ term: state.query });
    state.users = users;
    state.sent = true;
  } else {
    state.users = [];
    state.sent = false;
  }
};
</script>

<template>
  <form class="input-group my-2" @submit.prevent="submit">
    <input
      v-model="state.query"
      type="text"
      class="form-input"
      placeholder="Display name or handle..."
    />
    <button
      type="submit"
      class="btn btn-primary input-group-btn"
      @click="submit"
    >
      Search
    </button>
  </form>

  <template v-if="state.sent && state.users.length <= 0">
    <div class="empty">
      <p class="empty-title h5">No Users Found</p>
      <p class="empty-subtitle">Try a different search query again.</p>
    </div>
  </template>
  <template v-if="state.users.length > 0">
    <div class = "user-container">
      <TileUser
      v-for="user in state.users"
      :key="user.handle"
      class="py-2 my-2"
      :user="user"
    />

    </div>
 
  </template>
</template>


<style scoped>
.input-group {
  position: absolute;
  top: 0;
  left: 20;
  right: -10;
  width: 50%; /* Set the input group to full width */
  z-index: 1000; /* Ensure the search bar stays on top of other content */
  padding-bottom: 15px;
}
.tile:hover {
  background: #3e423e;
}

.user-container {
  padding-top: 50px;
}









</style>
