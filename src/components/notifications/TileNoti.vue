<script setup lang="ts">
import { PropType } from "vue";

import Avatar from "@/components/common/Avatar.vue";
import Username from "@/components/common/Username.vue";
import { Notification } from "@/lib/bsky";

import TileNotiLike from "./TileNoti/TileNotiLike.vue";
import TileNotiRepost from "./TileNoti/TileNotiRepost.vue";

defineProps({
  noti: {
    type: Object as PropType<Notification.Any>,
    required: true,
  },
});
</script>

<template>
  <div class ="notifications-container">
  <TileNotiLike v-if="noti.reason === 'like'" :noti="noti" />
  <TileNotiRepost v-else-if="noti.reason === 'repost'" :noti="noti" />
  <article
    v-else-if="noti.reason === 'mention' || noti.reason === 'reply'"
    class="tile tile-noti "
  >
    <div class="tile-icon">
      <Avatar
        :src="noti.author.avatar"
        :handle="noti.author.handle"
        :display-name="noti.author.displayName"
      />
    </div>
    <div class="tile-content mt-1">
      <div class="tile-title">
        <Username class="ml-2" :user="noti.author" /><span
          class="text-dark ml-1"
          >{{ noti.reason === "mention" ? "mentioned" : "replied" }}:</span
        >
      </div>
      <div class="tile-subtitle pre-line p-2">
        {{ noti.record.text }}
      </div>
    </div>
  </article>
  </div>
</template>

<style scoped>
.tile-noti {
  padding: 0.8rem 0.4rem 0.6rem;
  border-bottom: 1px solid #e3e3e3;
  margin-top: 0; /* Add this line to ensure no top margin */
}
.notifications-container {
  top:0;
  margin-top: 0;
}
body {
  padding:0;
  margin:0;
}



</style>