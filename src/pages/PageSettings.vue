<script setup lang="ts">
import { reactive } from "vue";

import ButtonAsync from "@/components/common/ButtonAsync.vue";
import ModalChangeHandle from "@/components/ModalChangeHandle.vue";
import { updateSettings,useSettings } from "@/lib/settings";
import { deleteSession } from "@/lib/bsky";

const settings = useSettings();
const state = reactive({
  showsModalChangeHandle: false,
  loadingModalChangeHandle: false,
});
const logout = () => {
  deleteSession();
  location.reload();
};
</script>

<template>
  <div class = "">
  <div class="form-group">
    <label class="form-switch">
      <input
        type="checkbox"
        :checked="settings.enableRelativeTime"
        @change="
          updateSettings({
            enableRelativeTime: !settings.enableRelativeTime,
          })
        "
      />
      <i class="form-icon"></i>Enable relative time
    </label>
  </div>
  <div>

<ButtonAsync
  class="btn btn-link change-handle" 
  :force-loading="state.loadingModalChangeHandle"
  @click="state.showsModalChangeHandle = true"
>
  Edit your handle...
</ButtonAsync>

  </div>
<button class="btn btn-link logout-button" @click="logout">
  Logout
</button>
  <Suspense
    @pending="state.loadingModalChangeHandle = true"
    @resolve="state.loadingModalChangeHandle = false"
    @fallback="state.loadingModalChangeHandle = false"
  >
    <ModalChangeHandle
      v-if="state.showsModalChangeHandle"
      @close="state.showsModalChangeHandle = false"
    />
  </Suspense>
  </div>
</template>

<style scoped>
.btn-link.logout-button {
  padding: 8px 16px; 
  font-size: 16px; 
  background-image: linear-gradient(145deg, #b8d8be, #b8d8be); 
  color: black;
  border: none; 
  border-radius: 5px; 
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); 
  transition: all 0.3s ease; 
  cursor: pointer; 
  margin-top: 30px;
}
.btn-link.logout-button:hover, .btn-link.logout-button:focus {
  background-image: linear-gradient(to right, #b8d8be, #b8d8be); 
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3); 
}

.btn-link.change-handle {
  padding: 8px 16px; 
  font-size: 16px; 
  background-image: linear-gradient(145deg, #b8d8be, #b8d8be); 
  color: black;
  border: none; 
  border-radius: 5px; 
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); 
  transition: all 0.3s ease;
  cursor: pointer;
  margin-top: .9em; 
}
  .btn-link.change-handle:hover .btn-link.change-handle:focus {
  background-image: linear-gradient(to right, #b8d8be, #b8d8be); 
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}
.settings {
  position: absolute;
  margin-left: 100px;
}
</style>
