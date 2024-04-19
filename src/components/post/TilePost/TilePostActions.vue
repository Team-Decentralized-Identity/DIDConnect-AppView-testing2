<script setup lang="ts">
import { computed,PropType, ref } from "vue";

import InputPost from "@/components/post/InputPost.vue";
import TilePostActionButton from "@/components/post/TilePost/TilePostActionButton.vue";
import { FeedViewPost } from "@/lib/bsky";
import { useLikeMutation,useRepostMutation } from "@/lib/query";

const props = defineProps({
  feed: { type: Object as PropType<FeedViewPost>, required: true },
});

const { mutate: repost } = useRepostMutation();
const { mutate: upvote } = useLikeMutation();

const expandedInput = ref(false);
const heart = ref(false);
// Initialize likeCount with a fallback to 0 if undefined
const likeCount = ref(props.feed.post.likeCount ?? 0);

const post = computed(() => props.feed.post);
const toggleLike = () => {
  heart.value = !heart.value;
  const action = heart.value ? 'like' : 'unlike';
  if (heart.value) {
    likeCount.value++;
  } else {
    likeCount.value = Math.max(likeCount.value - 1, 0);
  }

  upvote({
    cid: post.value.cid,
    uri: post.value.uri,
    action: action  // Pass the action as part of the request
  });
}
</script>

<template>
  <div class="mt-2">
    <TilePostActionButton
      aria-label="reply"
      icon-class="bi bi-reply"
      @click="expandedInput = !expandedInput"
    >
      {{ post.replyCount }}
    </TilePostActionButton>
    <TilePostActionButton
      aria-label="repost"
      icon-class="bi bi-megaphone"
      @click="
        repost({
          cid: post.cid,
          uri: post.uri,
        })
      "
    >
      {{ post.repostCount }}
    </TilePostActionButton>
    <TilePostActionButton
      aria-label="like"
      icon-class="bi bi-heart"
      @click="
        upvote({
          cid: post.cid,
          uri: post.uri,
        })
      "
    >
      {{ post.likeCount }}
    </TilePostActionButton>
  </div>
  <div v-if="expandedInput" class="d-flex">
    <InputPost
      class="column"
      :reply-to="feed"
      @success="expandedInput = false"
    />
    <button
      class="btn btn-link btn-icon col-auto col-ml-auto mt-1"
      @click="expandedInput = false"
    >
      <i class="bi bi-x-lg"></i>
    </button>
  </div>
</template>
<style>
.bi-heart {
  background-color: transparent;
}</style>